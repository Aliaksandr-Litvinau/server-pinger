# server-pinger

## Сборка и запуск

1. Установите Docker и Docker Compose, если они еще не установлены.

2. Склонируйте репозиторий:

   ```bash
   git clone git@github.com:Aliaksandr-Litvinau/server-pinger.git
   cd server-pinger
   ```

3. Создайте файл `requirements.txt` со следующим содержимым:

   ```
   Django==4.2.2
   djangorestframework==3.14.0
   psycopg2-binary==2.9.1
   ```

4. Создайте файл `.env` со следующим содержимым:

   ```
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=password
   POSTGRES_DB=pingapp
   ```

5. Соберите и запустите контейнеры:

   ```bash
   docker-compose up --build
   ```

6. Приложение будет доступно по адресу http://localhost:8000/.

## Использование
