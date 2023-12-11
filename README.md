# Funnybot
### Развлекательный телеграм бот

Funnybot - для получения развлекательного мультимедиа контента

- Картиноки
- Анегдоты - в разработке
- Стихи - в разработке
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



### 4. Бот используется API:
https://api.thecatapi.com/

### 5. Запуск бота (локально)
5.1. Клонируем проект:

```bash
git clone https://github.com/JRushFobos/Funnybot.git
```

5.5. Устанавливаем виртуальное окружение

```bash
python -m venv venv
```

5.3. Активируем виртуальное окружение

```bash
source venv/Scripts/activate
```

5.4. Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

5.5. В консоле импортируем токены для Телеграмм:

```bash
export TELEGRAM_TOKEN=<TELEGRAM_TOKEN>
```

5.5. Запускаем бота

```bash
python funnybot.py
```

### Об авторе
Мокрушин Евгений [@JRushFobos](https://github.com/JRushFobos)
