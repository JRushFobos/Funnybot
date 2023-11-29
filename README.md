# Funnybot
### Развлекательный телеграм бот

Funnybot - для получения развлекательного мультимедиа контента

- Картинок
- Изображений - в разработке
- Стихов - в разработке
- Видео - в разработке

### 1. Бот развернут в Docker контейнере на VPS sweb.ru
Сайт https://sweb.ru/

Команды развертывания и запуска:

Local
```bash
docker ps -a
docker images

docker tag funnybot:latest jrush/funnybot:latest
docker push jrush/funnybot:latest
```
Remote
```bash
sudo apt update
sudo apt install docker.io

sudo systemctl status docker
sudo systemctl start docker

sudo docker login

docker pull jrush/funnybot:latest
docker run -d -p 8080:80 --name funnybot jrush/funnybot:latest

docker stop funnybot
```

### 2. Бот используется API:
https://api.thecatapi.com/

### 3. Запуск бота (локально)
2.1. Клонируем проект:

```bash
git clone https://github.com/JRushFobos/Funnybot.git
```

2.2. Устанавливаем виртуальное окружение

```bash
python -m venv venv
```

2.3. Активируем виртуальное окружение

```bash
source venv/Scripts/activate
```

2.4. Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

2.5. В консоле импортируем токены для Телеграмм:

```bash
export TELEGRAM_TOKEN=<TELEGRAM_TOKEN>
```

2.5. Запускаем бота

```bash
python funnybot.py
```

### Об авторе
Мокрушин Евгений [@JRushFobos](https://github.com/JRushFobos)
