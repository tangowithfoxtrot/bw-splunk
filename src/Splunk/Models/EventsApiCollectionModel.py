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

    @property
    def lastLogDate(self):
        return self.lastLogDate
    
    @lastLogDate.setter
    def lastLogDate(self, value):
        self.lastLogDate = value

    @property
    def key(self):
        return self.key
    
    @key.setter
    def key(self, value):
        self.key = value

    @property
    def user(self):
        return self.user
    
    @user.setter
    def user(self, value):
        self.user = value
    
    def __str__(self):
        return f"LastLogDate: {self.lastLogDate}, Key: {self.key}, User: {self.user}"
