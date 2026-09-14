import sqlite3
from db_manager.db_config import DB_PATH
from utils.logger import db_logger

@db_logger
def add_data(args) :
    '''Функция принимает аргументы в виде словаря и записывает их в базу'''
    try :
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            get_values_place = ', '.join(['?'] * len(args))
            get_placeholders = ', '.join(args)
            get_values = tuple(args.values())
            add_query = f"INSERT OR IGNORE INTO personal_safe ({get_placeholders}) VALUES ({get_values_place}) "
            cursor.execute(add_query,get_values)
        return "success"
    except sqlite3.Error as e :
         raise e

@db_logger
def delete_data(id) :
    '''Функция принимает id записи и проводит удаление записи'''
    try :
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            delete_query = "DELETE FROM personal_safe WHERE id = ?"
            delete_value = (id,)
            cursor.execute(delete_query,delete_value)
        return "success"
    except sqlite3.Error as e :
         raise e

@db_logger
def show_data() :
    '''Функция возвращает все записи из базы'''
    try :
        with sqlite3.connect(DB_PATH) as connection :
                cursor = connection.cursor()
                show_query = "SELECT * FROM personal_safe"
                cursor.execute(show_query)
                res = cursor.fetchall()
        return res
    except sqlite3.Error as e :
         raise e

@db_logger
def update_data(id,args) :
    '''Функция принимает id и параметры и устанавливает новое значение'''
    try :
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            get_values_place = ', '.join(['?'] * len(args))
            get_placeholders = ', '.join(args)
            get_values = tuple(args.values())
            sum_values = get_values + (id,)
            update_query = f"UPDATE personal_safe SET ({get_placeholders}) = ({get_values_place}) WHERE id = ?"
            cursor.execute(update_query,sum_values)
        return "success"
    except sqlite3.Error as e :
         raise e

@db_logger
def get_data_by_id(id) :
    '''Функция возвращает запись'''
    try :
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            value = (id,)
            get_query = "SELECT * FROM personal_safe WHERE id = ? "
            cursor.execute(get_query,value)
            res = cursor.fetchone()
        return res
    except sqlite3 as e :
        raise e