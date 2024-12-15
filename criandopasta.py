import pyautogui
from time import sleep


#fechar janela atual 

pyautogui.moveTo(1788,12   ,duration=2)
pyautogui.leftClick()

#abrir pasta

pyautogui.moveTo(1397,361  ,duration=2)
pyautogui.rightClick()

pyautogui.moveTo(1475,525 ,duration=2)
pyautogui.leftClick()
pyautogui.moveTo(1329,530  ,duration=2)
pyautogui.leftClick()
pyautogui.write('Criando pasta teste')
sleep(1)
pyautogui.leftClick()


#excluir pasta 

pyautogui.moveTo(1385,355 ,duration=2)
pyautogui.rightClick()
pyautogui.moveTo(1535,388 ,duration=2)
pyautogui.leftClick()



