#!/usr/bin/env python3
import asyncio
import logging
import os
import sys
from typing import List
from AppSettings import AppSettings
from Models.EventsApiKeyModel import EventsApiKeyModel
import configparser

from SplunkApi import SplunkApi

# if not running in Splunk, load environment variables from .env
if sys.argv[1] == "cli":
    config = configparser.ConfigParser()
    config.read("src/Splunk/.env")
    # temporary; we need to pull this from SplunkApi later
    api_key = config["DEFAULT"]["API_KEY"]
else:
    # do splunk stuff to get the api key properly
    api_key = os.environ.get("API_KEY")

API_KEY = api_key

class Program:
    def __init__(self):
        self._eventsApiKey = None
        self._logger = None

    async def main_async(self, args: List[str]):
        appSettings = AppSettings()

        if appSettings.SplunkEnvironment:
            # _eventsApiKey = EventsApiKeyModel(API_KEY)
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s [%(levelname)s] %(message)s',
                handlers=[
                    logging.FileHandler(f"{appSettings.SplunkHome}/var/log/splunk/bitwarden_event_logs.log"),
                    logging.StreamHandler()])
        else:
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s [%(levelname)s] %(message)s',
                handlers=[
                    logging.FileHandler("bitwarden_event_logs.log"),
                    logging.StreamHandler()])

        self._logger = logging.getLogger(__name__)

        splunkApi = SplunkApi(appSettings, self._logger)
        if splunkApi.CanCallApi():
            _eventsApiKey = await splunkApi.GetApiKeyAsync()
            if _eventsApiKey is None:
                self._logger.error("Cannot resolve events API key")
                _eventsApiKey = EventsApiKeyModel(API_KEY)
                return # ?
            _key = "64421adf537747506913b9e1" # magic number; pull this from Splunk
            lastLogDate = await splunkApi.GetLastLogDateAsync() # just testing for now
            await splunkApi.UpsertLastLogDateAsync(_key, lastLogDate) # just testing for now
        else:
            _eventsApiKey = EventsApiKeyModel(API_KEY)
            self._logger.debug("Cannot call Splunk API; using environment variables")

    def main(self, args: List[str]):
        asyncio.run(self.main_async(args))

if __name__ == "__main__":
    program = Program()
    program.main(sys.argv)
