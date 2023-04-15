import json
import logging
import datetime
import base64
import hashlib
import asyncio
import aiohttp
from AppSettings import AppSettings
from SplunkApi import SplunkApi
from typing import List, Dict, Any, Optional
from Models import (EventsApiKeyModel,
                    EventRequestModel,
                    EventResponseModel,
                    MemberResponseModel,
                    GroupResponseModel,
                    EventLogModel)

class BitwardenApi:
    Epoc = datetime.datetime(1970, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
    ApiClient: aiohttp.ClientSession()
    IdentityClient: aiohttp.ClientSession()
    DecodedToken: Optional[Dict[str, Any]]
    NextAuthAttempt: Optional[datetime.datetime]
    AccessToken: Optional[str]
    JsonOptions: json.JSONEncoder

    def init(
            self,
            splunkApi: SplunkApi,
            eventsApiKey: EventsApiKeyModel,
            appSettings: AppSettings,
            logger: logging.Logger):
        self.SplunkApi = splunkApi
        self.EventsApiKey = eventsApiKey
        self.AppSettings = appSettings
        self.Logger = logger
        self.ApiClient = aiohttp.ClientSession()
        self.IdentityClient = aiohttp.ClientSession()
        self.DecodedToken = None
        self.NextAuthAttempt = None
        self.AccessToken = None
        self.JsonOptions = json.JSONEncoder()

    async def printEventLogs(self) -> None:
        # implementation
        pass

    def dispose(self) -> None:
        # implementation
        pass

    async def getEvents(self, requestModel: EventRequestModel) -> List[EventResponseModel]:
        # implementation
        pass

    async def getMembers(self) -> List[MemberResponseModel]:
        # implementation
        pass

    async def getGroups(self) -> List[GroupResponseModel]:
        # implementation
        pass

    async def hydrateEvents(self, events: List[EventResponseModel]) -> List[EventLogModel]:
        # implementation
        pass

    async def handleTokenState(self) -> bool:
        # implementation
        pass

    def tokenNeedsRefresh(self, minutes: int = 5) -> bool:
        # implementation
        pass

    def decodeToken(self) -> Dict[str, Any]:
        # implementation
        pass

    @staticmethod
    def fromEpocSeconds(seconds: int) -> datetime.datetime:
        # implementation
        pass

    @staticmethod
    def base64UrlDecode(inputString: str) -> bytes:
        # implementation
        pass

    @staticmethod
    def computeObjectHash(event: EventResponseModel) -> bytes:
        # implementation
        pass
