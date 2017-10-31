from telegram import *
from telegram.ext import *
import logging
import requests

class bot:
    def __init__(self, token, api_key):
        self.token = token
        self.apikey = api_key
        self.updater = Updater(token=self.token)

        self.dispatcher = self.updater.dispatcher

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        start_handler = CommandHandler(command="start", callback=self.give_exchange)
        self.dispatcher.add_handler(start_handler)

        give_handler = CommandHandler(command="give", callback=self.give_exchange)
        self.dispatcher.add_handler(give_handler)

        self.updater.start_polling()

    def give_exchange(self, bot, update):
        try:
            exchange = requests.get(self.api_key)

            exchange_rate = exchange.json()["quotes"]["USDCRC"]

            update.message.reply_text(text=f"Compra dólar:  {round(exchange_rate, 2)} colones")

        except:
            update.message.reply_text(text="Algo salio mal, intente de nuevo.")
