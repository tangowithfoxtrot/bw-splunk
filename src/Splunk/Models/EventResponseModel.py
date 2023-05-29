import json
from dataclasses import dataclass
from typing import Any


def to_str(x: Any) -> str:
    x = str(x)
    assert isinstance(x, str)
    return x


class EventEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (EventResponseModel, EventLogModel)):
            return obj.to_dict()
        return super().default(obj)


@dataclass
class EventResponseModel:
    hash: str = ""
    type: str = ""
    itemId: str = ""
    collectionId: str = ""
    groupId: str = ""
    policyId: str = ""
    memberId: str = ""
    actingUserId: str = ""
    installationId: str = ""
    date: str = ""
    device: str = ""
    ipAddress: str = ""

    @staticmethod
    def from_dict(obj: Any) -> 'EventResponseModel':
        assert isinstance(obj, dict)
        type = obj.get("type")
        itemId = obj.get("itemId")
        collectionId = obj.get("collectionId")
        groupId = obj.get("groupId")
        policyId = obj.get("policyId")
        memberId = obj.get("memberId")
        actingUserId = obj.get("actingUserId")
        installationId = obj.get("installationId")
        date = obj.get("date")
        device = obj.get("device")
        ipAddress = obj.get("ipAddress")
        return EventResponseModel(type, itemId, collectionId, groupId, policyId, memberId, actingUserId, installationId,
                                  date, device, ipAddress)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = self.type
        result["itemId"] = self.itemId
        result["collectionId"] = self.collectionId
        result["groupId"] = self.groupId
        result["policyId"] = self.policyId
        result["memberId"] = self.memberId
        result["actingUserId"] = self.actingUserId
        result["installationId"] = self.installationId
        result["date"] = self.date
        result["device"] = self.device
        result["ipAddress"] = self.ipAddress
        return result

    def to_str(self) -> str:
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_str()


@dataclass
class EventLogModel(EventResponseModel):
    hash: str = ""
    groupName: str = ""
    actingUserName: str = ""
    actingUserEmail: str = ""
    memberName: str = ""
    memberEmail: str = ""

    @staticmethod
    def from_dict(obj: Any) -> 'EventLogModel':
        assert isinstance(obj, dict)
        hash = obj.get("hash")
        type = obj.get("type")
        itemId = obj.get("itemId")
        collectionId = obj.get("collectionId")
        groupId = obj.get("groupId")
        policyId = obj.get("policyId")
        memberId = obj.get("memberId")
        actingUserId = obj.get("actingUserId")
        installationId = obj.get("installationId")
        date = obj.get("date")
        device = obj.get("device")
        ipAddress = obj.get("ipAddress")
        groupName = obj.get("groupName")
        actingUserName = obj.get("actingUserName")
        actingUserEmail = obj.get("actingUserEmail")
        memberName = obj.get("memberName")
        memberEmail = obj.get("memberEmail")
        return EventLogModel(hash, type, itemId, collectionId, groupId, policyId, memberId, actingUserId,
                             installationId,
                             date, device, ipAddress, groupName, actingUserName, actingUserEmail, memberName,
                             memberEmail)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hash"] = self.hash
        result["type"] = self.type
        result["itemId"] = self.itemId
        result["collectionId"] = self.collectionId
        result["groupId"] = self.groupId
        result["policyId"] = self.policyId
        result["memberId"] = self.memberId
        result["actingUserId"] = self.actingUserId
        result["installationId"] = self.installationId
        result["date"] = self.date
        result["device"] = self.device
        result["ipAddress"] = self.ipAddress
        result["groupName"] = self.groupName
        result["actingUserName"] = self.actingUserName
        result["actingUserEmail"] = self.actingUserEmail
        result["memberName"] = self.memberName
        result["memberEmail"] = self.memberEmail
        return result

    def to_str(self) -> str:
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_str()
