#!/bin/bash

# Запрашиваем ввод пользователя
echo "Введите имя миграции:"
alembic revision --autogenerate -m "Init migration first"
alembic upgrade head