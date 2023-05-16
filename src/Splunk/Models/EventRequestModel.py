class EventRequestModel:
    """
        public DateTime? Start { get; set; }
        public DateTime? End { get; set; }
        public Guid? ActingUserId { get; set; }
        public Guid? ItemId { get; set; }
        public string ContinuationToken { get; set; }
    """

    def __init__(
            self,
            start=None,
            end=None,
            actingUserId=None,
            itemId=None,
            continuationToken=None):
        self._start = start
        self._end = end
        self._actingUserId = actingUserId
        self._itemId = itemId
        self._continuationToken = continuationToken

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def actingUserId(self):
        return self._actingUserId

    @actingUserId.setter
    def actingUserId(self, value):
        self._actingUserId = value

    @property
    def itemId(self):
        return self._itemId

    @itemId.setter
    def itemId(self, value):
        self._itemId = value

    @property
    def continuationToken(self):
        return self._continuationToken

    @continuationToken.setter
    def continuationToken(self, value):
        self._continuationToken = value

    def __str__(self):
        return f"start: {self._start},\nend: {self._end},\nactingUserId: {self._actingUserId},\nitemId: {self._itemId},\ncontinuationToken: {self._continuationToken}"
