#!/bin/bash

# Запрашиваем ввод пользователя
echo "Введите имя миграции:"

# Читаем ввод и сохраняем в переменную

# Создаем миграцию с использованием Alembic
alembic revision --autogenerate -m "Init migration first"
alembic upgrade head