class EventResponseModel:
    """
        Type = e.Type;
        ItemId = e.ItemId;
        CollectionId = e.CollectionId;
        GroupId = e.GroupId;
        PolicyId = e.PolicyId;
        MemberId = e.MemberId;
        ActingUserId = e.ActingUserId;
        InstallationId = e.InstallationId;
        Date = e.Date;
        Device = e.Device;
        IpAddress = e.IpAddress;
    """

    def __init__(
            self,
            type=None,
            itemId=None,
            collectionId=None,
            groupId=None,
            policyId=None,
            memberId=None,
            actingUserId=None,
            installationId=None,
            date=None,
            device=None,
            ipAddress=None):
        self._type = type
        self._itemId = itemId
        self._collectionId = collectionId
        self._groupId = groupId
        self._policyId = policyId
        self._memberId = memberId
        self._actingUserId = actingUserId
        self._installationId = installationId
        self._date = date
        self._device = device
        self._ipAddress = ipAddress

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def itemId(self):
        return self._itemId

    @itemId.setter
    def itemId(self, value):
        self._itemId = value

    @property
    def collectionId(self):
        return self._collectionId

    @collectionId.setter
    def collectionId(self, value):
        self._collectionId = value

    @property
    def groupId(self):
        return self._groupId

    @groupId.setter
    def groupId(self, value):
        self._groupId = value

    @property
    def policyId(self):
        return self._policyId

    @policyId.setter
    def policyId(self, value):
        self._policyId = value

    @property
    def memberId(self):
        return self._memberId

    @memberId.setter
    def memberId(self, value):
        self._memberId = value

    @property
    def actingUserId(self):
        return self._actingUserId

    @actingUserId.setter
    def actingUserId(self, value):
        self._actingUserId = value

    @property
    def installationId(self):
        return self._installationId

    @installationId.setter
    def installationId(self, value):
        self._installationId = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, value):
        self._device = value

    @property
    def ipAddress(self):
        return self._ipAddress

    @ipAddress.setter
    def ipAddress(self, value):
        self._ipAddress = value

    def __str__(self):
        return f"type: {self.type}\nitemId: {self.itemId}\ncollectionId: {self.collectionId}\ngroupId: {self.groupId}\npolicyId: {self.policyId}\nmemberId: {self.memberId}\nactingUserId: {self.actingUserId}\ninstallationId: {self.installationId}\ndate: {self.date}\ndevice: {self.device}\nipAddress: {self.ipAddress}"
