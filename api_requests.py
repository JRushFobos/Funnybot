import os
import requests

from PIL import Image
from io import BytesIO
from telegram import Bot
from random import randint
from dotenv import load_dotenv

from urls import URL_cat, URL_dog, URL_random_image

load_dotenv()

unsplash_token = os.getenv("unsplash_token")

URL_cat = "https://api.thecatapi.com/v1/images/search"
URL_dog = "https://api.thedogapi.com/v1/images/search"
URL_random = ("https://api.unsplash.com/search/photos"
              f"?query=games&page={randint(1,109)}&per_page=30")

unsplash_headers = {"Authorization": unsplash_token}


def get_new_image_cat():
    response = requests.get(URL_cat).json()
    random_cat = response[0].get("url")
    return random_cat


def get_new_image_dog():
    response = requests.get(URL_dog).json()
    random_dog = response[0].get("url")
    return random_dog


def get_random_image():
    response = requests.get(URL_random_image, headers=unsplash_headers)
    if response.status_code == 200:
        image_link = response.json()["links"]["download"]
        response = requests.get(image_link, headers=unsplash_headers)

        image = Image.open(BytesIO(response.content))

        max_size = 800
        # Изменение размера с сохранением пропорций
        # Image.LANCZOS с сохранением деталей и гладкости краев
        image.thumbnail((max_size, max_size), Image.LANCZOS)

        with BytesIO() as output:  # открываем байтовый поток
            image.save(output, format='JPEG')  # байтовый поток в JPEG формате
            output.seek(0)  # Переходим на начало потока данных
            resized_image = output.read()  # Сохраняем и возвращаем поток в файл
            return resized_image

# def get_random_image():
#     response = requests.get(URL_random, headers=unsplash_headers)
#     if response.status_code == 200:
#         image_link = response.json().get("results")[0]["links"]["download"]
#         response = requests.get(image_link)
#         image = Image.open(BytesIO(response.content))

#         max_size = 800
#         # Изменение размера с сохранением пропорций
#         # Image.LANCZOS с сохранением деталей и гладкости краев
#         image.thumbnail((max_size, max_size), Image.LANCZOS)

#         with BytesIO() as output:  # открываем байтовый поток
#             image.save(output, format='JPEG')  # байтовый поток в JPEG формате
#             output.seek(0)  # Переходим на начало потока данных
#             resized_image = output.read()  # Сохраняем и возвращаем поток в файл
#             return resized_image


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_cat())


def new_dog(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_dog())


def new_random(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_random_image())
