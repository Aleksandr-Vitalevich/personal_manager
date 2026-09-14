from datetime import datetime
import os
from functools import wraps
MODULE_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_logs_file = os.path.join(MODULE_BASE_DIR,"system_logs.log")

def db_logger(func) :
    '''Наш декоратор'''
    @wraps(func)
    def wrapper(*args,**kwargs) :
        '''Наша функция обертка'''
        start_time_func = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try :
            result = func(*args,**kwargs)
            log_entry = f"[{start_time_func}] : FUNCTION : {func.__name__} | STATUS: SUCCESS | MSG: {result}\n"    
            with open(path_logs_file,'a',encoding='utf-8') as file :
                file.write(log_entry)
            return result
        except Exception as e :
            error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{error_time}] : FUNCTION : {func.__name__} | STATUS: ERROR | MSG: {str(e)}\n"
            with open(path_logs_file,'a',encoding='utf-8') as file :
                file.write(log_entry)    
            raise e

    return wrapper