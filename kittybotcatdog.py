import logging
import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

load_dotenv()

secret_token = os.getenv("TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


URL_cat = "https://api.thecatapi.com/v1/images/search"
URL_dog = "https://api.thedogapi.com/v1/images/search"


def get_new_image_cat():
    response = requests.get(URL_cat).json()
    random_cat = response[0].get("url")
    return random_cat


def get_new_image_dog():
    response = requests.get(URL_dog).json()
    random_dog = response[0].get("url")
    return random_dog


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_cat())


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_dog())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([["/newcat", "/newdog"]], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text="Привет, {}. Посмотри какого котика я тебе нашел".format(name),
        reply_markup=buttons,
    )

    context.bot.send_photo(chat.id, get_new_image_cat())


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler("start", wake_up))
    updater.dispatcher.add_handler(CommandHandler("newcat", new_cat))
    updater.dispatcher.add_handler(CommandHandler("newdog", new_dog))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
