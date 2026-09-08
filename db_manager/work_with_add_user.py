import sqlite3
from pathlib import Path
from utils import check_password,hash_password
from db_manager.db_config import DB_PATH

def add_user(login,password) :
        '''Функция принимает два параметра логин и пароль и создает запись в бд'''
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM user")
            if cursor.fetchone()[0] >= 1:
                return "forbidden"
            hash_password_user = hash_password(password)
            values = (login,hash_password_user)
            add_query = f"INSERT OR IGNORE INTO user (user_login,user_password) VALUES (?, ?) "
            cursor.execute(add_query,values)
        return "success"

def check_user_in_db() :
        '''Функция проверяет наличие пользователя в базе данных'''
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            check_query = 'SELECT COUNT(*) FROM user'
            cursor.execute(check_query)
            res = cursor.fetchone()[0]
        return True if res > 0 else False

def check_user_authorization(login,password) :
        '''Функция принимает логин и пароль'''
        with sqlite3.connect(DB_PATH) as connection :
                cursor = connection.cursor()
                get_user_password = "SELECT user_password FROM user WHERE user_login = ?"
                values_login = (login,)
                cursor.execute(get_user_password,values_login)
                res = cursor.fetchone()
                if not res :
                       return False
                elif res :
                        check_password_user = check_password(password,res[0])
                        if check_password_user :
                               return True
                        else : 
                               return False
                