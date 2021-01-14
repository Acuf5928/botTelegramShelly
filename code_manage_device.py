from telegram import Update
from telegram.ext import CallbackContext


def addDevice(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Funzione non implementata")


def removeDevice(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Funzione non implementata")