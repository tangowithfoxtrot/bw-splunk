class ListResponseModel:
    """
        public string Object { get; set; }
        public IEnumerable<T> Data { get; set; }
        public string ContinuationToken { get; set; }
    """

    def __init__(self, object=None, data=None, continuationToken=None):
        self._object = object
        self._data = data
        self._continuationToken = continuationToken

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, value):
        self._object = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def continuationToken(self):
        return self._continuationToken

    @continuationToken.setter
    def continuationToken(self, value):
        self._continuationToken = value

    def __str__(self):
        return f"object: {self._object},\ndata: {self._data},\ncontinuationToken: {self._continuationToken}"
