import json
from dataclasses import dataclass
from typing import Any


@dataclass
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

    id: str = ""
    userId: str = ""
    name: str = ""
    email: str = ""
    twoFactorEnabled: bool = False
    status: int = 0
    type: int = 0
    accessAll: bool = False
    externalId: str = ""
    resetPasswordEnrolled: bool = False

    @staticmethod
    def from_dict(obj: Any) -> 'MemberResponseModel':
        assert isinstance(obj, dict)
        id = obj.get("id")
        userId = obj.get("userId")
        name = obj.get("name")
        email = obj.get("email")
        twoFactorEnabled = obj.get("twoFactorEnabled")
        status = obj.get("status")
        type = obj.get("type")
        accessAll = obj.get("accessAll")
        externalId = obj.get("externalId")
        resetPasswordEnrolled = obj.get("resetPasswordEnrolled")
        return MemberResponseModel(id, userId, name, email, twoFactorEnabled, status, type, accessAll, externalId,
                                   resetPasswordEnrolled)

    def to_dict(self) -> dict:
        result: dict = {"id": self.id, "userId": self.userId, "name": self.name, "email": self.email,
                        "twoFactorEnabled": self.twoFactorEnabled, "status": self.status, "type": self.type,
                        "accessAll": self.accessAll, "externalId": self.externalId,
                        "resetPasswordEnrolled": self.resetPasswordEnrolled}
        return result

    @staticmethod
    def from_str(obj: str) -> 'MemberResponseModel':
        assert isinstance(obj, str)
        return MemberResponseModel.from_dict(json.loads(obj))

    def to_str(self) -> str:
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_str()
