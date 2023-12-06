from random import randint

URL_cat = "https://api.thecatapi.com/v1/images/search"
URL_dog = "https://api.thedogapi.com/v1/images/search"

URL_random_image = "https://api.unsplash.com/photos/random"
URL_games_image = ("https://api.unsplash.com/search/photos"
                   f"?query=games&page={randint(1,109)}&per_page=30")

URL_nature_image = ("https://api.unsplash.com/search/photos"
                    f"?query=nature&page={randint(1,334)}&per_page=30")
