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
    image.thumbnail((max_size, max_size), Image.LANCZOS)

    temp_image_path = "temp_image.jpg"
    image.save(temp_image_path)

    with open(temp_image_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)
    os.remove(temp_image_path)
else:
    print("Не удалось загрузить изображение")
