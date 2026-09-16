import tkinter as tk
import subprocess
import os
from utils.style import orange_style

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_safe_and_diary() :
    '''Функция запуска приложения сейф и дневник'''
    streamlit_path = os.path.join(BASE_DIR,'.venv','bin','streamlit')
    script_path = os.path.join(BASE_DIR,'main_operation.py')
    subprocess.Popen(['streamlit','run','main_operation.py'])

def run_calendar_notes() :
    pass

def run_chat() :
    pass

root = tk.Tk()
root.title("Персональный менеджер")
root.geometry("450x550")
root.configure(bg="#212121")

label = tk.Label(root,
                text="Персональный менеджер v2.0",
                font=("Helvetica",16,"bold"),
                bg="#212121",
                fg="#FFFFFF")
label.pack(pady=30)

@orange_style
def create_safe_btn() :
    '''Функция отрисовки кнопки запуска сейфа и дневника'''
    return tk.Label(root,text="Запустить сейф и дневник")

@orange_style
def create_calendar_btn() :
    '''Функция отрисовки кнопки запуска календарь и заметки'''
    return tk.Label(root,text="Запустить календарь и заметки")

@orange_style
def create_chat_btn() :
    '''Функция отрисовки кнопки запуска чата'''
    return tk.Label(root,text="Запустить личный чат")

safe_btn = create_safe_btn()
calendar_btn = create_calendar_btn()
chat_btn = create_chat_btn()

safe_btn.bind("<Button-1>",lambda event : run_safe_and_diary())
calendar_btn.bind("<Button-1>",lambda event : run_calendar_notes())
chat_btn.bind("<Button-1>",lambda event : run_chat())

safe_btn.pack(pady=20)
calendar_btn.pack(pady=20)
chat_btn.pack(pady=20)

root.mainloop()