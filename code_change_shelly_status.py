from telegram import Update
from telegram.ext import CallbackContext


def putOn(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Funzione non implementata")


def putOff(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Funzione non implementata")