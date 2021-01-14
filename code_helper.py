from dataclasses import dataclass
from typing import List

from dataclasses_serialization.json import JSONStrSerializerMixin

@dataclass
class ShellyInfo(JSONStrSerializerMixin):
    name: str
    ip: str
    relay: str
    user: str
    password: str


def retrieveDevicesInfo() -> List[ShellyInfo]:
    listShelly: List[ShellyInfo] = []

    with open("./db", "r") as file:
        for element in file.readlines():
            listShelly.append(ShellyInfo.from_json_str(element.replace("\n", "")))

    return listShelly
