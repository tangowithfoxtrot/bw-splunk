#!/usr/bin/env python3
"""
Splunk API client
"""

import asyncio
import datetime
import logging
from typing import Optional
import aiohttp
import json
import base64
import xml.etree.ElementTree as ET
from AppSettings import AppSettings
from Models import (EventsApiKeyModel, EventsApiCollectionModel)

class SplunkApi:
    def __init__(self, appSettings: AppSettings, logger: logging.Logger):
        self._appSettings = appSettings
        self._httpClient = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False))
        self._logger = AppSettings.logger

    async def GetApiKeyAsync(self) -> Optional[EventsApiKeyModel]:
        # not implemented
        return None
    
    async def GetLastLogDateAsync(self) -> Optional[EventsApiCollectionModel]:
        # not implemented
        return None
    
    async def UpsertLastLogDateAsync(self, key: str, last_log_date: datetime.datetime) -> None:
        # not implemented
        pass

    def CanCallApi(self) -> bool:
        # not implemented
        return False
    
    def AddAuthorization(self, request_message: requests.Request) -> None:
        # not implemented
        pass