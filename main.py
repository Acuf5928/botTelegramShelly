import logging
import re

from telegram.ext import ConversationHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from code_auth_fun import auth
from code_generate_totp_key import setupBot
from code_wait import wait
from const import REGEX_KEY_AUTH
from const import WAIT

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

logger = logging.getLogger(__name__)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(re.compile(REGEX_KEY_AUTH, re.IGNORECASE)), auth)],
        states={
            WAIT: [MessageHandler(Filters.regex(re.compile(r'.*', re.IGNORECASE)), wait)],
        },
        fallbacks=[],
        allow_reentry=True,
        conversation_timeout=300
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    try:
        from const_private import TELEGRAM_TOKEN
        main()
    except Exception:
        if setupBot():
            print("Configuration file created successfully, restart the program")
        else:
            print("Impossible create config file")
