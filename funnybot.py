import logging
import time
import os

from dotenv import load_dotenv

from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackQueryHandler,
                          ConversationHandler)
import telegram

import bot_send
from menu import (main_menu_buttons,
                  pictures_buttons,
                  jokes_buttons,
                  poems_buttons)

load_dotenv()

secret_token = os.getenv("TOKEN")
MAIN = 1
PICTURES = 2
JOKES = 3
POEMS = 4

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    # Создание кнопок выбора категории
    buttons = main_menu_buttons
    keyboard = telegram.InlineKeyboardMarkup(buttons)

    # Отправка сообщения с кнопками выбора категории
    context.bot.send_message(
        chat_id=chat.id,
        text=f"Привет, {name}\nВыбери категорию.",
        reply_markup=keyboard,
    )
    return MAIN


def main_menu(update, context):
    chat = update.effective_chat

    # Создание кнопок выбора категории
    buttons = main_menu_buttons
    keyboard = telegram.InlineKeyboardMarkup(buttons)

    # Отправка сообщения с кнопками выбора категории
    context.bot.send_message(
        chat_id=chat.id,
        text=f"Выбери категорию.",
        reply_markup=keyboard,
    )
    return MAIN


def pictures_menu(update, context):
    keyboard = telegram.InlineKeyboardMarkup(pictures_buttons)

    query = update.callback_query
    try:
        query.answer()
        query.message.reply_text(
            "Выберите категорию картинок:", reply_markup=keyboard)
    except telegram.error.BadRequest as error:
        time.sleep(2)
        query.answer()
        query.message.reply_text(
            "Выберите категорию картинок:", reply_markup=keyboard)


def jokes_menu(update, context):
    keyboard = telegram.InlineKeyboardMarkup(jokes_buttons)
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        "Выберите категорию:", reply_markup=keyboard)

def poems_menu(update, context):
    keyboard = telegram.InlineKeyboardMarkup(poems_buttons)
    query = update.callback_query
    query.answer()
    query.message.reply_text(
        "Выберите категорию:", reply_markup=keyboard)


def video_menu(update, context):
    pass


def reset_conversation(update, context):
    context.user_data.clear()  # Очищаем данные пользователя
    return wake_up(update, context)


def main():
    updater = Updater(token=secret_token)
    dp = updater.dispatcher

    # ConversationHandler для управления состояниями
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', wake_up)],
        states={
            PICTURES: [CallbackQueryHandler(main_menu, pattern='return')],
            JOKES: [CallbackQueryHandler(main_menu, pattern='return')],
            POEMS: [CallbackQueryHandler(main_menu, pattern='return')],
            MAIN: [CallbackQueryHandler(
                pictures_menu, pattern='pictures'),
                CallbackQueryHandler(
                jokes_menu, pattern='jokes'),
                CallbackQueryHandler(
                poems_menu, pattern='poems')],

        },
        fallbacks=[],
    )
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_cat, pattern='new_cat'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_dog, pattern='new_dog'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_game, pattern='new_game'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_nature, pattern='new_nature'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_anek, pattern='new_anek'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_random, pattern='random'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_pushkin, pattern='Pushkin'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_lermontov, pattern='Lermontov'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_krilov, pattern='Krilov'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_ahmatova, pattern='Ahmatova'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_zabolockiy, pattern='Zabolockiy'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_barto, pattern='Barto'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_chukovskiy, pattern='Chukovskiy'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_tolstoy, pattern='Tolstoy'))
    dp.add_handler(CallbackQueryHandler(
        bot_send.new_poem_zhukovskij, pattern='Zhukovskiy'))

    dp.add_handler(CallbackQueryHandler(
        main_menu, pattern='return'))

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler('start', reset_conversation))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
