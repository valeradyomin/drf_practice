# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем requirements.txt в рабочую директорию контейнера
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в рабочую директорию контейнера
COPY . .

## Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
