from Models.EventResponseModel import EventResponseModel

class EventLogModel(EventResponseModel):
    """
        public string GroupName { get; set; }
        public string ActingUserName { get; set; }
        public string ActingUserEmail { get; set; }
        public string MemberName { get; set; }
        public string MemberEmail { get; set; }
    """

    def __init__(self, event: EventResponseModel):
        if event is not None:
            super().__init__(type=event.type,
                             itemId=event.itemId,
                             collectionId=event.collectionId,
                             groupId=event.groupId,
                             policyId=event.policyId,
                             memberId=event.memberId,
                             actingUserId=event.actingUserId,
                             installationId=event.installationId,
                             date=event.date,
                             device=event.device,
                             ipAddress=event.ipAddress)
        else:
            super().__init__()
        self.groupName = None
        self.actingUserName = None
        self.actingUserEmail = None
        self.memberName = None
        self.memberEmail = None

    @property
    def groupName(self):
        return self._groupName
    
    @groupName.setter
    def groupName(self, value):
        self._groupName = value

    @property
    def actingUserName(self):
        return self._actingUserName
    
    @actingUserName.setter
    def actingUserName(self, value):
        self._actingUserName = value

    @property
    def actingUserEmail(self):
        return self._actingUserEmail
    
    @actingUserEmail.setter
    def actingUserEmail(self, value):
        self._actingUserEmail = value

    @property
    def memberName(self):
        return self._memberName
    
    @memberName.setter
    def memberName(self, value):
        self._memberName = value

    @property
    def memberEmail(self):
        return self._memberEmail
    
    @memberEmail.setter
    def memberEmail(self, value):
        self._memberEmail = value

    def __str__(self):
        return f"groupName: {self.groupName}\nactingUserName: {self.actingUserName}\nactingUserEmail: {self.actingUserEmail}\nmemberName: {self.memberName}\nmemberEmail: {self.memberEmail}\n{super().__str__()}"
