from dataclasses_serialization.json import JSONSerializer
from telegram import Update
from telegram.ext import CallbackContext

from code_helper import retrieveDevicesInfo


def addDevice(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Funzione non implementata")


def removeDevice(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    message = update.message.text
    message = message.lower()
    message = message.replace("rimuovi", "")
    message = message.replace(" ", "")

    try:
        listDevice = retrieveDevicesInfo()
    except Exception:
        context.bot.send_message(chat_id=chat_id, text="Errore nel db")
        return

    for index in range(0, len(listDevice)):
        if listDevice[index].name == message:
            del listDevice[index]
            with open("./db", "w") as file:
                for element in listDevice:
                    file.write(str(JSONSerializer.serialize(element)).replace("\'", "\"") + "\n")
            context.bot.send_message(chat_id=chat_id, text="Device eliminato")
            return

    context.bot.send_message(chat_id=chat_id, text="Device non trovato")
