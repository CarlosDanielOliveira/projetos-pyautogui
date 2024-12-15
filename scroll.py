import pyautogui
import requests
import webbrowser
from time import sleep

'''for i in range (0,30):
    pyautogui.moveTo(718,393, duration=1)
    pyautogui.scroll(-270, sleep(2))'''





#Abrir pagina do google
import webbrowser

url = "https://www.google.com"
webbrowser.open(url)

#pesquisar por linkedin 

pyautogui.moveTo(1094,102,duration=2)
sleep(0.2)
pyautogui.click()
sleep(0.2)
pyautogui.moveTo(1038,450,duration=3)

for i in range (0,10):
    pyautogui.scroll(-700)
    sleep(3)



    