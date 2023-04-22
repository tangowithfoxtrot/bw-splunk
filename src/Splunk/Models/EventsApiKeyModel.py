class EventsApiKeyModel:
    def __init__(self, api_key=None):
        self.ClientId = None
        self.ClientSecret = None

        if api_key:
            parts = api_key.split('_')
            if len(parts) > 1:
                self.ClientId = parts[0]
                self.ClientSecret = parts[1]
    
    def __str__(self):
        return f"{self.ClientId}_{self.ClientSecret}"

    def getClientId(self):
        return self.ClientId
    
    def getClientSecret(self):
        return self.ClientSecret
