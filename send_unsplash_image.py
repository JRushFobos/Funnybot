# send_unsplash_image.py
import os
import requests
from PIL import Image
from io import BytesIO
from telegram import Bot

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
chat_id = os.getenv("my_id")
bot = Bot(token=token)
image_url = "https://unsplash.com/photos/9J9Wdl3Va0o/download?ixid=M3w1MzU4NDJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDE2MjYyMjB8"

response = requests.get(image_url)
if response.status_code == 200:
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
