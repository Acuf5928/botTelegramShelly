import datetime
from dataclasses import dataclass
from typing import List

import pyotp
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


def checkTotp(value: str, key: str) -> bool:
    totp = pyotp.TOTP(key)
    delta = datetime.timedelta(seconds=30)
    return totp.verify(otp=value) or totp.verify(for_time=datetime.datetime.now() - delta, otp=value) or totp.verify(for_time=datetime.datetime.now() + delta, otp=value)
