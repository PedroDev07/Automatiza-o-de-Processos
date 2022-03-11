import pyautogui
import pyperclip
import time 

pyautogui.PAUSE = 1
pyautogui.hotkey('win')

pyautogui.write('chrome')

pyautogui.press('enter')

pyautogui.hotkey('tab')

pyautogui.press('enter')

pyperclip.copy('https://painel.smsdealer.com.br/?returnUrl=%2FAdmSms%2FIndex%2F')

pyautogui.hotkey('ctrl','v')

pyautogui.press('enter')


time.sleep(3)
pyautogui.click(x=704, y=420, clicks=1)
botao_entrar = pyautogui.position()