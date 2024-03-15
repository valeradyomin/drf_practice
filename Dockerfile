# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем requirements.txt в рабочую директорию контейнера
COPY ./requirements.txt /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем код приложения в рабочую директорию контейнера
COPY . /app
