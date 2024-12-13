import pyautogui

from time import sleep


'''
from  mouseinfo import mouseInfo
mouseInfo()

'''

#Posição de algo

pyautogui.moveTo(576,571,duration=1)
for i in range(0,100):
    sleep(0.1)
    pyautogui.click()

#pyautogui.move(1900,0,duration=2)
