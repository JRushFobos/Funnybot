import os
import random

import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

unsplash_token = os.getenv("unsplash_token")
unsplash_headers = {"Authorization": unsplash_token}
youtube_api_key = os.getenv("youtube_api_key")


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
        randon_pack_item = random.randint(0, count_images - 1)
        image_link = response.json().get("results")[randon_pack_item]["urls"][
            "small_s3"
        ]
        response = requests.get(image_link)
        return response.content
    else:
        print(f"Ошибка статус код: {response.status_code}")


def get_anek(URL_anek):
    response = requests.get(URL_anek)
    soup = bs(response.text, "html.parser")
    # Находим все анегдоты(с тегами)
    anekpots = soup.find_all("div", class_="tecst")
    # Убираем теги пробелы и лишние символы переноса
    clear_anekdots = [anek.text.split("\n+")[0] for anek in anekpots]
    random.shuffle(clear_anekdots)
    return clear_anekdots[0]


def get_poem(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    poems = soup.find_all("li", class_="listing-item")
    links_poems = []
    for poem in poems:
        link = poem.find("a")["href"]  # Извлекаем ссылку из тега <a>
        links_poems.append(link)
    random.shuffle(links_poems)
    poem_response = requests.get(links_poems[0])
    soup = bs(poem_response.text, "html.parser")
    poem_title = soup.find("h1", class_="entry-title").get_text(strip=True)
    text_poems = soup.find("div", class_="entry-content poem-text").get_text()
    only_text_poem = text_poems.split("Анализ")[0].strip()
    return (
        f"{poem_title}\n------------------------------------------------\n"
        f"{only_text_poem}"
    )


def get_random_video():
    youtube = build("youtube", "v3", developerKey=youtube_api_key)
    request = youtube.search().list(
        q="юмор",
        part="snippet",
        type="video",
        maxResults=50,
        videoDuration="short",
    )
    response = request.execute()
    video_links = []
    for item in response["items"]:
        video_links.append("https://www.youtube.com/shorts/" f'{item["id"]["videoId"]}')
    random.shuffle(video_links)
    return video_links[0]
