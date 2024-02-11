from random import randint

URL_cat = "https://api.thecatapi.com/v1/images/search"
URL_dog = "https://api.thedogapi.com/v1/images/search"

URL_random_image = "https://api.unsplash.com/photos/random"
URL_games_image = (
    "https://api.unsplash.com/search/photos"
    f"?query=games&page={randint(1,109)}&per_page=30"
)

URL_nature_image = (
    "https://api.unsplash.com/search/photos"
    f"?query=nature&page={randint(1,334)}&per_page=30"
)

URL_anek = "https://anekdotbar.ru/top-100.html"

URLs_poems = {
    "Pushkin": "https://rustih.ru/vse-stixi-pushkina-na-odnoj-stranice/",
    "Lermontov": "https://rustih.ru/vse-stixi-lermontova-na-odnoj-stranice/",
    "Krilov": "https://rustih.ru/vse-basni-krylova-na-odnoj-stranice/",
    "Ahmatova": "https://rustih.ru/vse-stixi-axmatovoj-na-odnoj-stranice/",
    "Zabolockiy": "https://rustih.ru/vse-stixi-zabolockogo-na-odnoj-stranice/",
    "Barto": "https://rustih.ru/vse-stixi-barto-na-odnoj-stranice/",
    "Chukovskiy": "https://rustih.ru/vse-stixi-chukovskogo-na-odnoj-stranice/",
    "Tolstoy": "https://rustih.ru/vse-stixi-alekseya-konstantinovicha-tolstogo-na-odnoj-stranice/",
    "Zhukovskij": "https://rustih.ru/vse-stixi-zhukovskogo-na-odnoj-stranice/",
    "Pasternak":"https://rustih.ru/vse-stixi-pasternaka-na-odnoj-stranice/",
    "Block":"https://rustih.ru/vse-stixi-bloka-na-odnoj-stranice/",
    "Bunin":"https://rustih.ru/vse-stixi-bunina-na-odnoj-stranice/",
}
