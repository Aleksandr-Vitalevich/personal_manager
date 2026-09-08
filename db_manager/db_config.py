import os
import streamlit as st
# Получаем абсолютный путь к этому файлу (db_manager/db_config.py)
file_path = os.path.abspath(__file__)

# Поднимаемся на один уровень вверх — в саму папку db_manager
db_manager_dir = os.path.dirname(file_path)

# Поднимаемся еще на один уровень вверх — в КОРЕНЬ текущего проекта
BASE_DIR = os.path.dirname(db_manager_dir)

# Формируем путь к базе данных строго в корне текущего запущенного проекта
DB_PATH = os.path.join(BASE_DIR, "personal_manager.db")