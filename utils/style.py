import tkinter as tk
from functools import wraps

def orange_style(button_func) :
    '''Декоратор приводит стиль лаунчера к одному формату'''
    @wraps(button_func)
    def wrapper(*args,**kwargs) :
        '''Функция обертка'''
        btn = button_func(*args,**kwargs) 
        btn.configure(
            font=("Helvetica",11,"bold"),
            bg= "#1E1E1E",
            fg= "#FFFFFF",

            highlightbackground="#FF6B00",
            highlightthickness=2,

            padx=20,
            pady=10,
            cursor="hand2"
        )
        return btn
    return wrapper