class MemberResponseModel:
    """
        public Guid Id { get; set; }
        public Guid? UserId { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }
        public bool TwoFactorEnabled { get; set; }
        public short Status { get; set; }
        public byte? Type { get; set; }
        public bool? AccessAll { get; set; }
        public string ExternalId { get; set; }
        public bool ResetPasswordEnrolled { get; set; }
    """

    def __init__(
            self,
            id=None,
            userId=None,
            name=None,
            email=None,
            twoFactorEnabled=None,
            status=None,
            type=None,
            accessAll=None,
            externalId=None,
            resetPasswordEnrolled=None):
        self._id = id
        self._userId = userId
        self._name = name
        self._email = email
        self._twoFactorEnabled = twoFactorEnabled
        self._status = status
        self._type = type
        self._accessAll = accessAll
        self._externalId = externalId
        self._resetPasswordEnrolled = resetPasswordEnrolled

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value: str):
        self._userId = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def twoFactorEnabled(self):
        return self._twoFactorEnabled

    @twoFactorEnabled.setter
    def twoFactorEnabled(self, value: bool):
        self._twoFactorEnabled = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def accessAll(self):
        return self._accessAll

    @accessAll.setter
    def accessAll(self, value: bool):
        self._accessAll = value

    @property
    def externalId(self):
        return self._externalId

    @externalId.setter
    def externalId(self, value: str):
        self._externalId = value

    @property
    def resetPasswordEnrolled(self):
        return self._resetPasswordEnrolled

    @resetPasswordEnrolled.setter
    def resetPasswordEnrolled(self, value: bool):
        self._resetPasswordEnrolled = value

    def __str__(self):
        return f"id: {self._id},\nuserId: {self._userId},\nname: {self._name},\nemail: {self._email},\ntwoFactorEnabled: {self._twoFactorEnabled},\nstatus: {self._status},\ntype: {self._type},\naccessAll: {self._accessAll},\nexternalId: {self._externalId},\nresetPasswordEnrolled: {self._resetPasswordEnrolled}"
