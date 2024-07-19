# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Переходим в подкаталог с исходным кодом
WORKDIR /app/weather_app

# Копируем остальной проект
COPY . /app/weather_app/

# Открываем порт
EXPOSE 8000

# Выполняем миграции и запускаем сервер
CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]