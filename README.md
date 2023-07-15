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
   DB_URL=postgres://postgres:postgres@db:5432/pinger_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=pinger_db
   ```

5. Соберите и запустите контейнеры:

   ```bash
   docker compose up --build
   ```
   
6. Coздать суперюзера для возможности добавления доменов из админки:
   ```bash
   docker compose run app sh -c "python manage.py createsuperuser"
   ```

7. Приложение будет доступно по адресу http://0.0.0.0:8000/.


