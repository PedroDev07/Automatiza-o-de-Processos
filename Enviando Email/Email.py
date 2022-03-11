import pyautogui
import pyperclip



#acessando a base de dados
pyautogui.PAUSE = 1
pyautogui.hotkey('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.hotkey('tab')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

#baixando a base de dados
time.sleep(4)
pyautogui.click(x=393, y=264, clicks=3)
time.sleep(4)
pyautogui.click(x=393, y=268, clicks=1)
time.sleep(1.5)
pyautogui.click(x=1158, y=161, clicks=1)
time.sleep(1.5)
pyautogui.click(x=984, y=556, clicks=1)

#extraindo dados 
import pandas as pd

df = pd.read_excel(r'C:\Code\Python\Python\PersonalProjects\Mobilidade_global_covid\arquivo.xlsx')
print(df)

quantidade = df['quantidade']
valor_final = df ['Valor Final']
