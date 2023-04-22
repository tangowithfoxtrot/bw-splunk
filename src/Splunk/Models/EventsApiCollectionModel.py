class EventsApiCollectionModel:
    """
        [JsonPropertyName("last_log_date")]
        public DateTime? LastLogDate { get; set; }
        [JsonPropertyName("_key")]
        public string Key { get; set; }
        [JsonPropertyName("_user")]
        public string User { get; set; }
    """
    def __init__(self, last_log_date=None, _key=None, _user=None):
        self.lastLogDate = last_log_date
        self.key = _key
        self.user = _user

    def getLastLogDate(self):
        return self.lastLogDate
    
    def setLastLogDate(self, last_log_date): # maybe not needed
        self.lastLogDate = last_log_date

    def getKey(self):
        return self.key
    
    def getUser(self):
        return self.user
    
    def __str__(self):
        return f"LastLogDate: {self.lastLogDate}, Key: {self.key}, User: {self.user}"
