import pyautogui, pydirectinput
import time

print('\n\n\nPREPARE-SE\n\n\n')
time.sleep(3)


#pega  a posição do cursor
coordenadas = pyautogui.position()
print(f'Coordenadas do cursor:{coordenadas}, {type(coordenadas)}')
print(coordenadas[0],coordenadas[1])

#tira e pega a cor da posição coletada
printsc = pyautogui.screenshot()
cores = printsc.getpixel(coordenadas)
print(cores)
#verifica se tal cor é igual a ela mesma
pixelmatch = pyautogui.pixelMatchesColor(coordenadas[0],coordenadas[1], (cores))

print(pixelmatch)

print('\n\n\nFIM\n\n\n')
