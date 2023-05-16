class GroupResponseModel:
    """
        public Guid Id { get; set; }
        public string Name { get; set; }
        public bool? AccessAll { get; set; }
        public string ExternalId { get; set; }
    """

    def __init__(self):
        self._id = None
        self._name = None
        self._accessAll = None
        self._externalId = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def accessAll(self):
        return self._accessAll
    
    @accessAll.setter
    def accessAll(self, value):
        self._accessAll = value

    @property
    def externalId(self):
        return self._externalId
    
    @externalId.setter
    def externalId(self, value):
        self._externalId = value

    def __str__(self):
        return f"id: {self._id},\nname: {self._name},\naccessAll: {self._accessAll},\nexternalId: {self._externalId}"
