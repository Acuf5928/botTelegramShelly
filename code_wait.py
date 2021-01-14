from telegram import Update
from telegram.ext import CallbackContext
import re

from telegram.ext import ConversationHandler

from code_change_shelly_status import putOff
from code_change_shelly_status import putOn
from code_manage_device import addDevice
from code_manage_device import removeDevice
from const import REGEX_KEY_ADD
from const import REGEX_KEY_DELETE
from const import REGEX_KEY_EXIT
from const import REGEX_KEY_PUT_OFF
from const import REGEX_KEY_PUT_ON
from const import WAIT


def wait(update: Update, context: CallbackContext) -> int:
    chat_id = update.message.chat_id
    message = update.message.text

    message = message.lower()
    message = message.split(" ")

    if re.search(REGEX_KEY_PUT_ON, message[0], re.IGNORECASE):
        putOn(update, context)
    elif re.search(REGEX_KEY_PUT_OFF, message[0], re.IGNORECASE):
        putOff(update, context)
    elif re.search(REGEX_KEY_ADD, message[0], re.IGNORECASE):
        addDevice(update, context)
    elif re.search(REGEX_KEY_DELETE, message[0], re.IGNORECASE):
        removeDevice(update, context)
    elif re.search(REGEX_KEY_EXIT, message[0], re.IGNORECASE):
        context.bot.send_message(chat_id=chat_id, text="Connessione chiusa")
        return ConversationHandler.END

    return WAIT
