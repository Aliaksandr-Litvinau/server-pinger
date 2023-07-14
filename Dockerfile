FROM python:3.10

# Установите переменную среды PYTHONUNBUFFERED в значение 1
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию в /app
WORKDIR /app

# Копируйте файл requirements.txt в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install -r requirements.txt

# Копируйте все файлы проекта в контейнер
COPY . .

# Запустите сервер Django при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
