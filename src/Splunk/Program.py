#!/usr/bin/env python3
import asyncio
import logging
import sys
from typing import List
from AppSettings import AppSettings
from BitwardenApi import BitwardenApi
from SplunkApi import SplunkApi


class Program:
    def __init__(self):
        self._eventsApiKey = None
        self._logger = None

    async def main_async(self, args: List[str]):
        appSettings = AppSettings()

        if appSettings.SplunkEnvironment:
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
                    logging.StreamHandler()
                ]
            )

        self._logger = logging.getLogger(__name__)

        splunkApi = SplunkApi(appSettings, self._logger)
        if splunkApi.CanCallApi():
            try:
                _eventsApiKey = await splunkApi.GetApiKeyAsync()
            except Exception as e:
                self._logger.error("Error getting API key from Splunk")
                self._logger.error(e)
                exit(1)
            lastLogDate, key = await splunkApi.GetLastLogDateAsync()
            await splunkApi.UpsertLastLogDateAsync(lastLogDate, str(key))

        accessToken = await splunkApi.GetApiKeyAsync()
        accessTokenString = accessToken.__str__()
        if accessToken is None:
            self._logger.error("Cannot resolve Bitwarden API key")
            return

        bitwardenApi = BitwardenApi(
            accessToken=accessTokenString,
            appSettings=appSettings,
            eventsApiKey=_eventsApiKey,  # type: ignore
            logger=self._logger,
            splunkApi=splunkApi)

        self._logger.debug("Getting logs from Bitwarden")
        eventLogs = await bitwardenApi.PrintEventLogsAsync()
        # TODO: finish this

    def main(self, args: List[str]):
        asyncio.run(self.main_async(args))


if __name__ == "__main__":
    program = Program()
    program.main(sys.argv)
