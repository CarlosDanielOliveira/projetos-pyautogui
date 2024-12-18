import pyautogui as pa
import os
import subprocess
from time import sleep
import pyperclip


'''
senha
pa.alert(text='Testando', title= 'RPA', button='ok')

senha
senha = pa.prompt(text='Digite sua senha: ', title = 'Obrigatório')
print(senha)

confirmação 

resposta = pa.confirm(text='Deseja sair da navegaçaõ?', title='Informação', buttons=['Sim', 'Não'] )
'''

#solicitar matricula

id = pa.prompt(text='Digite seu id: ', title = 'Acesso Ultra English')


#solicitar senha

senha = pa.password(text='Digite sua senha: ', title = 'Acesso Ultra English', mask='*')


#abrir bloco de notas

sleep(1)
caminho_do_arquivo = r"C:\Users\carlo\Desktop\USERS"
subprocess.Popen(['notepad.exe', caminho_do_arquivo])


#colar informações

pyperclip.copy(id)
pa.moveTo(1565,562, duration=1)
pa.hotkey('ctrl' , 'v')
sleep(0.5)
pa.press('enter')
pyperclip.copy(senha)
pa.moveTo(1565,562, duration=1)
pa.hotkey('ctrl' , 'v')
