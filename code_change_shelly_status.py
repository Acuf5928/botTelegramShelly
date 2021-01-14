from dataclasses import dataclass
from typing import List

import requests
from dataclasses_serialization.json import JSONStrSerializerMixin
from telegram import Update
from telegram.ext import CallbackContext

@dataclass
class ShellyInfo(JSONStrSerializerMixin):
    name: str
    ip: str
    relay: str
    user: str
    password: str


def putOn(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    message = update.message.text
    message = message.lower()
    message = message.replace("accendi", "")
    message = message.replace(" ", "")

    try:
        listDevice = retrieveDevicesInfo()
    except Exception:
        context.bot.send_message(chat_id=chat_id, text="Errore nel db")
        return

    targetDevice = None

    for element in listDevice:
        if element.name == message:
            targetDevice = element

    if targetDevice is None:
        context.bot.send_message(chat_id=chat_id, text="Device non trovato")
        return

    link = createLink(targetDevice, "on")
    requests.get(link, timeout=2)


def putOff(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    message = update.message.text
    message = message.lower()
    message = message.replace("spegni", "")
    message = message.replace(" ", "")

    try:
        listDevice = retrieveDevicesInfo()
    except Exception:
        context.bot.send_message(chat_id=chat_id, text="Errore nel db")
        return

    targetDevice = None

    for element in listDevice:
        if element.name == message:
            targetDevice = element

    if targetDevice is None:
        context.bot.send_message(chat_id=chat_id, text="Device non trovato")
        return

    link = createLink(targetDevice, "off")
    requests.get(link, timeout=2)


def retrieveDevicesInfo() -> List[ShellyInfo]:
    listShelly: List[ShellyInfo] = []

    with open("./db", "r") as file:
        for element in file.readlines():
            listShelly.append(ShellyInfo.from_json_str(element.replace("\n", "")))

    return listShelly


def createLink(info: ShellyInfo, command: str) -> str:
    link = "http://" + info.user + ":" + info.password + "@" + info.ip + "/relay/" + info.relay

    if command != "update":
        link = link + "?turn=" + command

    return link
