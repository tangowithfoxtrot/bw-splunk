from typing import Optional

class EventsApiKeyModel:
    def __init__(self, api_key: Optional[str] = None):
        self._clientId: Optional[str] = None
        self._clientSecret: Optional[str] = None

        if api_key:
            parts = api_key.split('_')
            if len(parts) > 1:
                self._clientId = parts[0]
                self._clientSecret = parts[1]

    def __str__(self):
        return f"{self._clientId}_{self._clientSecret}"

    def getClientId(self) -> Optional[str]:
        return self._clientId

    def getClientSecret(self) -> Optional[str]:
        return self._clientSecret
