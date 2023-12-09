import os
import requests

from PIL import Image
from io import BytesIO
from telegram import Bot
from random import randint
from dotenv import load_dotenv

from urls import (URL_cat, URL_dog, URL_random_image,
                  URL_games_image, URL_nature_image)
from funnybot import pictures_menu, PICTURES, MAIN


load_dotenv()

unsplash_token = os.getenv("unsplash_token")
unsplash_headers = {"Authorization": unsplash_token}


def get_new_image_cat(URL_cat):
    response = requests.get(URL_cat).json()
    random_cat = response[0].get("url")
    return random_cat


def get_new_image_dog(URL_dog):
    response = requests.get(URL_dog).json()
    random_dog = response[0].get("url")
    return random_dog


def get_random_image(URL_random_image):
    response = requests.get(URL_random_image, headers=unsplash_headers)
    if response.status_code == 200:
        image_link = response.json().get("urls")["small_s3"]
        response = requests.get(image_link)
        # image = Image.open(BytesIO(response.content))

        # max_size = 600
        # # Изменение размера с сохранением пропорций
        # # Image.LANCZOS с сохранением деталей и гладкости краев
        # image.thumbnail((max_size, max_size), Image.LANCZOS)

        # with BytesIO() as output:  # открываем байтовый поток
        #     image.save(output, format='JPEG')  # байтовый поток в JPEG формате
        #     output.seek(0)  # Переходим на начало потока данных
        #     resized_image = output.read()  # Сохраняем и возвращаем поток в файл
        #     return resized_image
        return response.content
    else:
        print(f"Ошибка статус код: {response.status_code}")


def get_image(url):
    response = requests.get(url, headers=unsplash_headers)
    count_images = len(response.json().get("results"))
    if response.status_code == 200 and count_images > 0:
        randon_pack_item = randint(0, count_images-1)
        image_link = response.json().get(
            "results")[randon_pack_item]["urls"]["small_s3"]
        response = requests.get(image_link)
        return response.content
    else:
        print(f"Ошибка статус код: {response.status_code}")


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
