import os

from funnybot import (JOKES, MAIN, PICTURES, POEMS, VIDEO, jokes_menu,
                      pictures_menu, poems_menu, video_menu)
from get_content import (get_anek, get_image, get_new_image_cat,
                         get_new_image_dog, get_poem, get_random_image,
                         get_random_video)
from urls import (URL_anek, URL_cat, URL_dog, URL_games_image,
                  URL_nature_image, URL_random_image, URLs_poems)


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
    context.bot.send_message(chat.id, get_poem(URLs_poems["Pushkin"]))
    poems_menu(update, context)
    return POEMS


def new_poem_lermontov(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Lermontov"]))
    poems_menu(update, context)
    return POEMS


def new_poem_krilov(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Krilov"]))
    poems_menu(update, context)
    return POEMS


def new_poem_ahmatova(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Ahmatova"]))
    poems_menu(update, context)
    return POEMS


def new_poem_zabolockiy(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Zabolockiy"]))
    poems_menu(update, context)
    return POEMS


def new_poem_barto(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Barto"]))
    poems_menu(update, context)
    return POEMS


def new_poem_chukovskiy(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Chukovskiy"]))
    poems_menu(update, context)
    return POEMS


def new_poem_tolstoy(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Tolstoy"]))
    poems_menu(update, context)
    return POEMS


def new_poem_zhukovskij(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Zhukovskij"]))
    poems_menu(update, context)
    return POEMS


def new_poem_pasternak(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Pasternak"]))
    poems_menu(update, context)
    return POEMS


def new_poem_block(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Block"]))
    poems_menu(update, context)
    return POEMS


def new_poem_bunin(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_poem(URLs_poems["Bunin"]))
    poems_menu(update, context)
    return POEMS


def new_youtube_video(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, get_random_video())
    video_menu(update, context)
    return VIDEO


def about_bot(update, context):
    text = (
        "👉 Funnybot - для получения развлекательного "
        "мультимедиа контента\n"
        "1️⃣ Картинки\n"
        "2️⃣ Анекдоты\n"
        "3️⃣ Стихи\n"
        "4️⃣ Видео - ссылки на YouTube видео\n"
        "5️⃣ Видео - в формате файлов (в разработке)"
    )
    chat = update.effective_chat
    context.bot.send_message(chat.id, text=text)
    return MAIN
