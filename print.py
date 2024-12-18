import pyautogui as pa 


#print da tela inteira

pa.screenshot('tela_inteira.jpg')


#print parte a tela

pa.screenshot('calculadora.jpg', region = (1391,434 , 421, 262 ))