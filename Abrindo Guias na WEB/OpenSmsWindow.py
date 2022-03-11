import pyautogui
import pyperclip
import time 
import random
from tkinter import *


texto=["Bom dia Allan" ,"Bom dia Doutor", "Bom dia Chefe", "Bom dia, to com problema em uma nota aqui",
       "Bom dia, to com problema em uma nota aqui" , "Nossa, esse povo de financeiro é muito enjuado em", 
       "Bom dia, a infobarra ta de boa? Vpn ta oscilando aqui","Bom diaaa","Aobaa","Teste internet",
       "Bom dia doutor,tu mexeu no ad da adm","Bom dia, to indo ali na portaria rapidão",
       "Bom diaa","Allan","Diaa"]
valor = random.randrange(14)
frase = (texto[valor])


pyautogui.PAUSE = 1

#abrindo chrome
pyautogui.hotkey('win')

pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(2)

pyautogui.hotkey('tab')

pyautogui.press('enter')

#entrando no site da sms
pyperclip.copy('https://painel.smsdealer.com.br')

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')

time.sleep(2)
pyautogui.click(x=704, y=420, clicks=1)
botao_entrar = pyautogui.position()

#abrindo youutube
time.sleep(2)

pyautogui.hotkey('ctrl','t')

pyperclip.copy('https://www.youtube.com/watch?v=v9mGFXaL5z4&list=RDv9mGFXaL5z4&start_radio=1')

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')

#abrindo a naty
time.sleep(2)

pyautogui.hotkey('ctrl','t')

pyperclip.copy('https://naty.app/login')

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')

time.sleep(2.8)

pyautogui.click(x=674, y=625, clicks=1)

time.sleep(2)

#ligando vpn
pyautogui.hotkey('win')

pyautogui.write('open')

pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=16, y=575, clicks=1, button='right')

time.sleep(2)

pyautogui.click(x=16, y=573, clicks=1, button='right')

time.sleep(2)

pyautogui.click(x=167, y=348, clicks=1, button='left')

time.sleep(2)

pyautogui.click(x=634, y=426, clicks=1, button='left')

#Abrindo micro sip
pyautogui.hotkey('win')

pyautogui.write('micro')

time.sleep(2)

pyautogui.press('enter')

#abrindo skype
pyautogui.hotkey('win')

pyautogui.write('sky')

pyautogui.press('enter')

time.sleep(2)

#Mandando bom dia
pyautogui.click(x=441, y=131, clicks=1, button='left')

pyperclip.copy('Allan R')

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')

pyautogui.click(x=400, y=333, clicks=1, button='left')

pyautogui.click(x=696, y=676, clicks=1, button='left')

pyperclip.copy(frase)

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')

#exibindo janela 
app=Tk()

app.title("Pedro Lucas")
texto = Label(app, text='Parabéns o código foi executado')


texto.grid(column=0,row=2)

app.mainloop()


