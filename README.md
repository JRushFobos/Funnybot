# Funnybot
### Развлекательный телеграм бот

Funnybot - для получения развлекательного мультимедиа контента

- Картинки
- Анекдоты
- Стихи
- Видео - в разработке

### 1. Настроен CI/CD на VPS sweb.ru с помощью Git Actions
Телеграм бот автоматически обновляется при обновлении main ветки

### 2. Бот развернут в Docker контейнере на VPS sweb.ru (ручной деплой)
Сайт https://sweb.ru/

Команды ручного развертывания и запуска:

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


### 3. Бот использует:
API https://api.thecatapi.com
API https://api.unsplash.com
Сайт анегдотов https://anekdotbar.ru
Сайт стихов https://rustih.ru


### 4. Запуск бота (локально)
4.1. Клонируем проект:

```bash
git clone https://github.com/JRushFobos/Funnybot.git
```

4.2. Устанавливаем виртуальное окружение

```bash
python -m venv venv
```

4.3. Активируем виртуальное окружение

```bash
source venv/Scripts/activate
```

4.4. Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

4.5. Запускаем бота

```bash
python funnybot.py
```

### Об авторе
Мокрушин Евгений [@JRushFobos](https://github.com/JRushFobos)
