# send_unsplash_image.py
import os
import requests
from PIL import Image
from io import BytesIO
from telegram import Bot
from random import randint

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
chat_id = os.getenv("my_id")
bot = Bot(token=token)
image_url = f"https://api.unsplash.com/search/photos?query=games&page={randint(1,109)}&per_page=30"
headers = {"Authorization": "Client-ID 0j8aNMxNUwSnZbmPHpob9OJiSBvIxQkTB9DTr71MsjU"}

print(image_url)
response = requests.get(image_url, headers=headers)
print(response.status_code)
print(response.json().get("results")[0]["links"]["download"])
links_list = []
if response.status_code == 200:
    image_link = response.json().get("results")[0]["links"]["download"]
    response = requests.get(image_link)
    image = Image.open(BytesIO(response.content))

    max_size = 800
    # Изменение размера с сохранением пропорций
    # Image.LANCZOS с сохранением деталей и гладкости краев
    image.thumbnail((max_size, max_size), Image.LANCZOS)

    with BytesIO() as output:  # открываем байтовый поток
        image.save(output, format='JPEG')  # байтовый поток в JPEG формате
        output.seek(0)  # Переходим на начало потока данных
        resized_image = output.read()  # Читаем поток в файл

    bot.send_photo(chat_id=chat_id, photo=resized_image)
else:
    print("Не удалось загрузить изображение")
