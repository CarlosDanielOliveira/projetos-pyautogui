

import pyautogui as pa
import pyperclip 
from time import sleep
import os
import subprocess

'''
* ABRIR ÁREA DE TRABALHO*

import os



desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
subprocess.Popen(['explorer', desktop_path])

'''

# Abre a área de trabalho no Windows

os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
sleep(1)

pa.moveTo(1325,346, duration= 1)
sleep(1)
pa.hotkey('alt' , 'space') #maximizar pasta
pa.moveTo(543,126, duration=1)
pa.leftClick()

#abrir um bloco de notas e nomear

pa.moveTo(1126,388 ,duration= 1)
pa.rightClick(duration=1)
pa.moveTo(1244,551, duration= 1)
sleep(1)
pa.leftClick()
pa.moveTo(1548,826, duration=1)
pa.leftClick()
sleep(1)
pyperclip.copy('Automação - RPA')
pa.hotkey('ctrl', 'v')
sleep(0.3)
pa.press('Enter')

#entrar no bloco e escrever

sleep(1)
caminho_do_arquivo = r"C:\Users\carlo\Desktop\Automação - RPA.txt"
subprocess.Popen(['notepad.exe', caminho_do_arquivo])
pa.moveTo(597,227, duration=1.5)
pa.leftClick()
pyperclip.copy('AUTOMATIZANDO PROCESSOS - RPA PY')
pa.hotkey('ctrl', 'v')  #PODERIA CRIAR UMA FUNÇÃO, POIS GEROU-SE UMA ROTINA DE UTILIZAÇÃO. 

#salvar e sair 

sleep(1.5)
pa.hotkey('ctrl' , 's')
sleep(0.5)
pa.hotkey('alt' , 'f4')

#excluir bloco

sleep(2)
os.remove(caminho_do_arquivo)
pa.click(1291,368, duration=1)
sleep(2)

pa.hotkey('alt' , 'space') #maximizar pasta
pa.moveTo(127,41, duration=1)
pa.leftClick()
sleep(1)
pa.hotkey('alt' , 'f4')
















