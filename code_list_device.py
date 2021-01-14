from telegram import Update
from telegram.ext import CallbackContext

from code_helper import retrieveDevicesInfo


def listDevice(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    try:
        listDevice = retrieveDevicesInfo()
    except Exception:
        context.bot.send_message(chat_id=chat_id, text="Errore nel db")
        return

    message = "Lista device:\n"

    for element in listDevice:
        message = message + element.name + "\n"

    context.bot.send_message(chat_id=chat_id, text=message)
