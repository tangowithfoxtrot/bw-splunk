#!/usr/bin/env python3
"""
Splunk API client
"""

import asyncio
import datetime
import logging
import aiohttp
import json
import base64
from urllib.parse import urlparse, urlunparse
import xml.etree.ElementTree as ET
from AppSettings import AppSettings
from Models.EventsApiKeyModel import EventsApiKeyModel

class SplunkApi:
    def __init__(self, appSettings: AppSettings, logger: logging.Logger):
        self._appSettings = appSettings
        self._appNS = f"{appSettings.SplunkApiUrl}/servicesNS/nobody/bitwarden_event_logs/storage"
        self._authHeader = base64.b64encode(
            f"{appSettings.SplunkUsername}:{appSettings.SplunkPassword}".encode("utf-8"))
        self._logger = logger

    async def GetApiKeyAsync(self):
        urlString = "{}".format(
            f"{self._appNS}/passwords/bitwarden_event_logs_realm:api_key/")

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(urlString, headers={"Authorization": f"Basic {self._authHeader.decode('utf-8')}"}) as response:
                self._logger.debug(
                    f"Got response from Splunk: {response.status}")
                if response.status == 200:
                    xml = await response.text()
                    xmlDoc = ET.fromstring(xml)
                    clear_password = xmlDoc.findtext(
                        './/{http://dev.splunk.com/ns/rest}key[@name="clear_password"]')
                    if clear_password is None:
                        self._logger.error("Got empty API key from Splunk")
                        return None
                    else:
                        self._logger.debug(
                            "Got Bitwarden API key from Splunk API")
                        return EventsApiKeyModel(clear_password)
                else:
                    self._logger.error("Error getting API key from Splunk")
                    self._logger.error(f"Response: {response.status}")
                    return None

    # -> Optional[EventsApiCollectionModel]:
    async def GetLastLogDateAsync(self):
        urlString = "{}".format(
            f"{self._appNS}/collections/data/eventsapi?output_mode=json"
        )

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(urlString, headers={"Authorization": f"Basic {self._authHeader.decode('utf-8')}"}) as response:
                self._logger.debug(
                    f"Got response from Splunk: {response.status}")
                if response.status == 200:
                    data = await response.json()
                    if data is None:
                        self._logger.debug("No last log date found in Splunk")
                        # return current date minus 1 year
                        lastYear = datetime.datetime.now() - datetime.timedelta(days=365)
                        self._logger.debug(
                            f"Setting lastLogDate to last year: {lastYear}")
                        return lastYear
                    else:
                        self._logger.debug("Got last log date from Splunk API")
                        date = sorted(
                            data,
                            key=lambda k: k['_key'],
                            reverse=True)[0]['last_log_date']
                        self._logger.debug(f"Last log date: {date}")
                        # removing the 7th-digit of the microseconds; this
                        # might be a problem later because the original
                        # datetime is 7-digit microseconds, followed by "Z".
                        # commenting-out for now because it may be fine to just
                        # return a string here.
                        # converted_date = datetime.datetime.strptime(
                        #     (date[:26]).strip(), "%Y-%m-%dT%H:%M:%S.%f")
                        # self._logger.debug(
                            # f"Converted last log date: {converted_date}")
                        return date
                else:
                    self._logger.error(
                        "Error getting last log date from Splunk")
                    self._logger.error(f"Response: {response.status}")
                    return None

    async def UpsertLastLogDateAsync(self, key: str, last_log_date: datetime.datetime) -> None:
        urlString = "{}".format(
            f"{self._appNS}/collections/data/eventsapi/{key}?output_mode=json"
        )

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            data = {"last_log_date": last_log_date}

            curlCommand = f"curl -k '{urlString}' -X POST -H 'Authorization: Basic {self._authHeader.decode('utf-8')}' -H 'Content-Type: application/json' -d '{json.dumps(data)}'"
            self._logger.debug(f"curl command: {curlCommand}")
            async with session.post(
                    urlString, headers={"Authorization": f"Basic {self._authHeader.decode('utf-8')}",
                                        "Content-Type": "application/json"},
                    data=json.dumps(data),
            ) as response:
                content = await response.text()
                self._logger.debug(f"Response content: {content}")
                self._logger.debug(
                    f"Request: {response.request_info}")
                self._logger.debug(
                    f"Got response from Splunk: {response.status}")
                self._logger.debug(f"Response: {response}")
                if response.status == 200:
                    self._logger.debug("Updated last log date in Splunk")
                else:
                    self._logger.error(
                        "Error updating last log date in Splunk")
                    self._logger.error(f"Response: {response.status}")

    def CanCallApi(self) -> bool:
        if self._appSettings.SplunkApiUrl and self._appSettings.SplunkUsername and self._appSettings.SplunkPassword:
            return True
        else:
            return False

    def _AddAuthorization(self, request_message: aiohttp.ClientSession):
        # curl -k "$SPLUNK_API_URL/services/auth/login" --data-urlencode \
        # username=$SPLUNK_USERNAME --data-urlencode password=$SPLUNK_PASSWORD
        authHeader = base64.b64encode(
            f"{self._appSettings.SplunkUsername}:{self._appSettings.SplunkPassword}".encode("utf-8"))
        request_message.headers["Authorization"] = f"Basic {authHeader.decode('utf-8')}"
