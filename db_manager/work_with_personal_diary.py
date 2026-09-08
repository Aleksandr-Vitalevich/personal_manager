import sqlite3
from db_manager.db_config import DB_PATH

def add_data_to_diary(text) :
    '''Функция принимает текст и записывает их в базу'''
    with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            value = (text,)
            add_query = f"INSERT OR IGNORE INTO personal_diary (text_diary) VALUES (?) "
            cursor.execute(add_query,value)
    return "success"

def delete_data_to_diary(id) :
    '''Функция принимает id записи и проводит удаление записи'''
    with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            delete_query = "DELETE FROM personal_diary WHERE id = ?"
            delete_value = (id,)
            cursor.execute(delete_query,delete_value)
            return "success"

def show_data_to_diary() :
    '''Функция возвращает все записи из базы'''
    with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            show_query = "SELECT * FROM personal_diary ORDER BY created_at DESC"
            cursor.execute(show_query)
            res = cursor.fetchall()
    return res
