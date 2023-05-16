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
        self._lastLogDate = last_log_date
        self._key = _key
        self._user = _user

    @property
    def lastLogDate(self):
        return self._lastLogDate
    
    @lastLogDate.setter
    def lastLogDate(self, value):
        self._lastLogDate = value

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, value):
        self._key = value

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value
    
    def __str__(self):
        return f"LastLogDate: {self._lastLogDate}, Key: {self._key}, User: {self._user}"
