import json
import logging
from datetime import datetime, timedelta, timezone
import base64
import hashlib
from typing import List, Optional
import aiohttp
from AppSettings import AppSettings
from SplunkApi import SplunkApi
from Models.EventsApiKeyModel import EventsApiKeyModel
from Models.EventRequestModel import EventRequestModel
from Models.EventResponseModel import EventResponseModel
from Models.EventLogModel import EventLogModel

class BitwardenApi:
    def __init__(
            self,
            appSettings: AppSettings,
            logger: logging.Logger,
            eventsApiKey: EventsApiKeyModel,
            accessToken: str,
            splunkApi: SplunkApi,
            nextAuthAttempt: Optional[datetime] = None):
        self._epoch = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self._appSettings = appSettings
        self._logger = logger
        self._eventsApiKey = eventsApiKey
        self._nextAuthAttempt = None
        self._accessToken = accessToken
        self._tokenNeedsRefresh = False
        self._splunkApi = SplunkApi(appSettings, logger)
        self._apiClient = aiohttp.ClientSession()
        self._identityClient = aiohttp.ClientSession()
        self._jsonOptions = {
            "indent": 4,
            "separators": (",", ": "),
            "sort_keys": False
        }

    async def PrintEventLogsAsync(self):
        """
            public async Task PrintEventLogsAsync()
            {
                var events = await GetEventsAsync();
                foreach (var e in events)
                {
                    Console.WriteLine(e);
                }
            }
        """
        lastEventLog, key = await self._splunkApi.GetLastLogDateAsync() if self._splunkApi.CanCallApi() else (None, None)
        requestModel = EventRequestModel()
        requestModel.start = lastEventLog if lastEventLog is not None else None
        requestModel.end = datetime.utcnow().replace(
            tzinfo=timezone.utc) + timedelta(hours=1)

        events = await self._GetEventsAsync(requestModel, [])
        if events is None or len(events['data']) == 0:
            return

        eventLogs = await self._HydrateEventsAsync(events or [])
        if eventLogs is None or len(eventLogs) == 0:
            return
        if self._splunkApi.CanCallApi():
            lastEventDate = eventLogs[-1].date
            if key is None:
                key = hashlib.sha256(lastEventDate.encode(
                    'utf-8')).hexdigest() if lastEventDate is not None else None
            await self._splunkApi.UpsertLastLogDateAsync(lastEventDate, key)

        eventLogList = []
        for eventLog in eventLogs:
            eventLog.hash = self.ComputeObjectHash(eventLog)
            # self._logger.debug(f"Event: {eventLog}")
            eventLogList.append(eventLog)
            print("\n---\n{}".format(eventLog))

        return eventLogList

    async def _GetEventsAsync(self, requestModel: EventRequestModel, responseModel: List[EventResponseModel]):
        """
            private async Task<List<EventResponseModel>> GetEventsAsync(EventRequestModel requestModel,
                List<EventResponseModel> responseList)
        """
        tokenStateReponse = await self._HandleTokenStateAsync()
        if tokenStateReponse is None:
            return None
        if requestModel is None:
            return None

        urlString = f"{self._appSettings.EventsApiUrl}/public/events"
        headers = {
            "Authorization": f"Bearer {self._accessToken}",
            "Accept": "application/json"
        }

        params = {
            "start": str(
                requestModel.start),
            "end": str(
                requestModel.end),
            "continuationToken": requestModel.continuationToken if requestModel.continuationToken is not None else "null",
        }

        # curlCommand = f"curl -X GET \"{urlString}\" -H \"Authorization: Bearer {self._accessToken}\" -H \"Accept: application/json\" -d \"start={params['start']}\" -d \"end={params['end']}\" -d \"continuationToken={params['continuationToken']}\""
        # self._logger.debug(f"curl command: {curlCommand}")
        async with self._apiClient.get(urlString, headers=headers, params=params) as response:
            if response.status != 200:
                self._logger.error(
                    f"Failed to get events. Status code: {response.status}")
                raise Exception(
                    f"Failed to get events. Status code: {response.status}")
            responseModel = await response.json()
            return responseModel

    async def _GetMembersAsync(self):# -> List[MemberResponseModel]:
        tokenStateResponse = await self._HandleTokenStateAsync()
        if not tokenStateResponse:
            return None

        responseList = []

        url = f"{self._appSettings.EventsApiUrl}/public/members"
        headers = {
            "Authorization": f"Bearer {self._accessToken}",
            "Accept": "application/json"
        }

        try:
            async with self._apiClient.get(url, headers=headers) as response:
                if response.status != 200:
                    self._logger.error(
                        f"Failed to get members. Status code: {response.status}")
                    return None

                responseModel = await response.json()
                if responseModel and "data" in responseModel:
                    responseList = responseModel["data"]

        except Exception as e:
            self._logger.error(e, "Failed to GET members.")
            return None

        return responseList

    async def _GetGroupsAsync(self):
        tokenStateReponse = await self._HandleTokenStateAsync()
        if tokenStateReponse is None:
            return None
        urlString = f"{self._appSettings.EventsApiUrl}/public/groups"
        headers = {
            "Authorization": f"Bearer {self._accessToken}",
            "Accept": "application/json"
        }

        async with self._apiClient.get(urlString, headers=headers) as response:
            if response.status != 200:
                self._logger.error(
                    f"Failed to get groups. Status code: {response.status}")
                return None
            responseModel = await response.json()
            return responseModel

    # -> List[EventLogModel]:
    async def _HydrateEventsAsync(self, events: List[EventResponseModel]):
        eventData = events['data'] # type: ignore
        eventLogs = []
        members = await self._GetMembersAsync()
        groups = await self._GetGroupsAsync()
        if not events or len(eventData) == 0:
            return eventLogs

        for event in eventData:
            event = EventResponseModel(
                type=event['type'],
                actingUserId=event['actingUserId'],
                installationId=event['installationId'],
                date=event['date'],
                device=event['device'],
                ipAddress=event['ipAddress'],
                itemId=event['itemId'],
                collectionId=event['collectionId'],
                groupId=event['groupId'],
                memberId=event['memberId'],
                policyId=event['policyId']
            )

            memberEmail = None
            groupName = None
            actingUserName = None
            actingUserEmail = None
            memberName = None

            if event.memberId is not None:
                # TODO: implement
                pass

            if event.groupId is not None:
                # TODO: implement
                pass

            if event.actingUserId is not None:
                # TODO: implement
                pass

            eventLogModel = EventLogModel(event=event)
            # TODO: implement

            eventLogs.append(eventLogModel)

            jsonEvent = json.dumps(event, default=lambda o: o.__dict__, sort_keys=False, indent=4)
            print(jsonEvent)

        return eventLogs

    async def _HandleTokenStateAsync(self):
        """
            private async Task<bool> HandleTokenStateAsync()
        """

        clientId = self._eventsApiKey.getClientId()
        clientSecret = self._eventsApiKey.getClientSecret()

        if clientId is None or clientSecret is None:
            self._logger.error("Client ID or secret is null")
            return False

        requestMessage = {
            "grant_type": "client_credentials",
            "scope": "api.organization",
            "client_id": clientId,
            "client_secret": clientSecret
        }

        urlString = f"{self._appSettings.IdentityUrl}/connect/token"

        async with self._apiClient.post(urlString, data=requestMessage) as response:
            if response.status != 200:
                self._logger.error(
                    f"Failed to get access token. Status code: {response.status}")
                self._nextAuthAttempt = datetime.utcnow() + timedelta(minutes=1)
                exit(1)
            responseModel = await response.json()
            self._accessToken = responseModel["access_token"]
            self._tokenNeedsRefresh = False
            self._nextAuthAttempt = None
            return True

    def TokenNeedsRefresh(self, minutes: int = 5):
        decoded = self.DecodeToken(self._accessToken)
        if decoded is None:
            return False
        exp = decoded["exp"]
        now = datetime.utcnow()
        if now > exp:
            return True
        return False

    def DecodeToken(self, token: str):
        """
            private JsonDocument DecodeToken()
        """
        if token is None or token == "":
            exception = Exception("Token is null or empty")
            self._logger.error(exception)
            raise exception
        parts = token.split(".")
        if len(parts) != 3:
            exception = Exception("Token must have 3 parts")
            self._logger.error(exception)
            raise exception
        decoded = base64.b64decode(parts[1])
        if decoded is None or decoded == "" or decoded.__str__.length < 1:
            exception = Exception("Token must have 3 parts")
            self._logger.error(exception)
            raise exception
        _decodedToken = json.loads(decoded)
        return _decodedToken

    def FromEpochSeconds(self, seconds: int):
        """
            private DateTime FromEpochSeconds(long seconds)
        """
        return self._epoch.fromtimestamp(seconds)

    def Base64UrlDecode(self, base64UrlEncodedString: str):
        """
            private static byte[] Base64UrlDecode(string input)
        """
        output = base64UrlEncodedString.replace("-", "+").replace("_", "/")
        switch = len(output) % 4
        if switch == 0:
            pass
        if switch == 2:
            output += "=="
        elif switch == 3:
            output += "="
        else:
            self._logger.error("Illegal base64url string!")
            raise Exception("Illegal base64url string!")
        return base64.b64decode(output) if output is not None else None

    def ComputeObjectHash(self, eventResponseModel: EventResponseModel):
        """
            private static byte[] Base64UrlDecode(string input)
        """
        # TODO: Implement
        hashBytes = hashlib.sha256(
            eventResponseModel.__str__().encode()).digest()
        return base64.b64encode(hashBytes).decode()
