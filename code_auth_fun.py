from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler

from code_helper import checkTotp
from const import AUTH_USERS
from const import WAIT

try:
    from const_private import TOTP_KEY
except Exception:
    pass


def auth(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user.username
    chat_id = update.message.chat_id

    message = update.message.text
    message = message.lower()
    message = message.replace("password", "")
    message = message.replace(" ", "")

    if checkTotp(message, TOTP_KEY) and user in AUTH_USERS:
        context.bot.send_message(chat_id=chat_id, text="Autenticato per cinque minuti")
        return WAIT
    else:
        context.bot.send_message(chat_id=chat_id, text="Non sei autorizzato")
        return ConversationHandler.END
