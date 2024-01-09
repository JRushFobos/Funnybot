import os

from get_content import (get_new_image_cat,
                         get_new_image_dog,
                         get_random_image,
                         get_image,
                         get_anek,
                         get_poem,
                         get_random_video)
from urls import (URL_cat, URL_dog, URL_random_image,
                  URL_games_image, URL_nature_image, URL_anek, URLs_poems)
from funnybot import (pictures_menu,
                      jokes_menu,
                      poems_menu,
                      video_menu,
                      PICTURES,
                      JOKES,
                      POEMS,
                      VIDEO)


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_cat(URL_cat))
    pictures_menu(update, context)
    return PICTURES


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_dog(URL_dog))
    pictures_menu(update, context)
    return PICTURES


def new_random(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_random_image(URL_random_image))
    pictures_menu(update, context)
    return PICTURES


def new_game(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_image(URL_games_image))
    pictures_menu(update, context)
    return PICTURES


def new_nature(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_image(URL_nature_image))
    pictures_menu(update, context)
    return PICTURES

def new_anek(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=get_anek(URL_anek))
    jokes_menu(update, context)
    return JOKES

def new_poem_pushkin(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Pushkin']))
    poems_menu(update, context)
    return POEMS

def new_poem_lermontov(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Lermontov']))
    poems_menu(update, context)
    return POEMS

def new_poem_krilov(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Krilov']))
    poems_menu(update, context)
    return POEMS

def new_poem_ahmatova(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Ahmatova']))
    poems_menu(update, context)
    return POEMS

def new_poem_zabolockiy(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Zabolockiy']))
    poems_menu(update, context)
    return POEMS

def new_poem_barto(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Barto']))
    poems_menu(update, context)
    return POEMS

def new_poem_chukovskiy(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Chukovskiy']))
    poems_menu(update, context)
    return POEMS

def new_poem_tolstoy(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Tolstoy']))
    poems_menu(update, context)
    return POEMS

def new_poem_zhukovskij(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems['Zhukovskij']))
    poems_menu(update, context)
    return POEMS


def new_youtube_video(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_random_video())
    video_menu(update, context)
    return VIDEO
