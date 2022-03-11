from cProfile import label
import pyautogui
import pyperclip
import time 
import random
from tkinter import * 

app=Tk()

app.title("Pedro Lucas")
texto = Label(app, text='Parabéns o código foi executado')


texto.grid(column=0,row=2)

app.mainloop()
# returns 65
time.sleep(3)
print(pyautogui.position())