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
   requests==2.31.0
   dj-database-url==2.0.0
   ```

4. Создайте файл `.env` со следующим содержимым (тестовый не для продакшн):

   ```
   DEBUG=True
   SECRET_KEY=django-insecure-53u_bf0uwa)@^o$64(79#frk2=r0d7eya4d+5@wgbmi(tlcgi3
   DB_URL=postgres://postgres:postgres@0.0.0.0:5432/pinger_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=pinger_db
   DB_HOST=0.0.0.0
   DB_PORT=5432
   ```

5. Соберите и запустите контейнеры:

   ```bash
   docker compose up --build
   ```

6. Приложение будет доступно по адресу http://localhost:8000/.

## Использование
   ```bash
   docker compose run app python manage.py makemigrations
   ```

   ```bash
   docker compose run app python manage.py migrate
   ```

   ```bash
  docker compose logs db
   ```