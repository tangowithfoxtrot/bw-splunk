import json
from dataclasses import dataclass
from typing import Any


@dataclass
class GroupResponseModel:
    """
        public Guid Id { get; set; }
        public string Name { get; set; }
        public bool? AccessAll { get; set; }
        public string ExternalId { get; set; }
    """

    id: str = ""
    name: str = ""
    accessAll: bool = False
    externalId: str = ""

    @staticmethod
    def from_dict(obj: Any) -> 'GroupResponseModel':
        assert isinstance(obj, dict)
        id = obj.get("id")
        name = obj.get("name")
        accessAll = obj.get("accessAll")
        externalId = obj.get("externalId")
        return GroupResponseModel(id, name, accessAll, externalId)

    def to_dict(self) -> dict:
        result: dict = {"id": self.id, "name": self.name, "accessAll": self.accessAll, "externalId": self.externalId}
        return result

    @staticmethod
    def from_str(obj: str) -> 'GroupResponseModel':
        assert isinstance(obj, str)
        return GroupResponseModel.from_dict(json.loads(obj))

    def to_str(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def __str__(self):
        return self.to_str()