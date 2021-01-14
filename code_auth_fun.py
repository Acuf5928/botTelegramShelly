from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler
import pyotp

from const import AUTH_USERS
from const import WAIT
from const_private import TOTP_KEY


def auth(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user.username
    chat_id = update.message.chat_id

    message = update.message.text
    message = message.lower()
    message = message.replace("password", "")
    message = message.replace(" ", "")

    if checkTotp(message) and user in AUTH_USERS:
        context.bot.send_message(chat_id=chat_id, text="Autenticato per cinque minuti")
        return WAIT
    else:
        context.bot.send_message(chat_id=chat_id, text="Non sei autorizzato")
        return ConversationHandler.END


def checkTotp(value: str) -> bool:
    totp = pyotp.TOTP(TOTP_KEY)
    return totp.verify(value)
