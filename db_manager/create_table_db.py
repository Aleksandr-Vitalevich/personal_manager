import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "personal_manager.db"


def create_table() :
    '''Функция создания базы данных'''
    with sqlite3.connect(DB_PATH) as connection :
        cursor = connection.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_login TEXT NOT NULL,
                user_password TEXT NOT NULL)
        ''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS personal_safe (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_service TEXT NOT NULL UNIQUE,
                login_service TEXT,
                password_service TEXT,
                site_service TEXT,
                token_service TEXT,
                other_need_information_service TEXT
                )
        ''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS personal_diary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text_diary TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
        ''')
        

