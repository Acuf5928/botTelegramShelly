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


def retrieveDevicesInfo(path: str = "./db") -> List[ShellyInfo]:
    listShelly: List[ShellyInfo] = []

    with open(path, "r") as file:
        for element in file.readlines():
            listShelly.append(ShellyInfo.from_json_str(element.replace("\n", "")))

    return listShelly


# timeNow and delta are set in this way for testing purpose
def checkTotp(value: str, key: str, timeNow: datetime = datetime.datetime.now(), delta: datetime = datetime.timedelta(seconds=30)) -> bool:
    totp = pyotp.TOTP(key)
    return totp.verify(for_time=timeNow, otp=value) or totp.verify(for_time=timeNow - delta, otp=value) or totp.verify(for_time=timeNow + delta, otp=value)
