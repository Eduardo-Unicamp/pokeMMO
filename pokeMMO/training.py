import pyautogui, pydirectinput
import time

print('\n\n\nprepare-se...\n\n\n')
time.sleep(3)

def function():
    coordenada_base = (486,181) #coordenada da barra de vida a ser comparada pra saber em qual tela está
    pixel_match = False
    #variações da cor
    
    cor_A = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(131, 207, 141),tolerance = 10)  
    cor_B = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(254, 254, 254),tolerance = 10) 
    cor_C = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(57, 133, 66),tolerance = 10) 
    pixel_match = cor_A or cor_B or cor_C

    while True:
        print(pixel_match)#debug 
        print(pyautogui.pixel(coordenada_base[0],coordenada_base[1]))#debug
        if not(pixel_match):
            clicks = 0
            while clicks < 6:
                pydirectinput.press('left')
                clicks+=1

            clicks = 0
            while clicks < 6:
                pydirectinput.press('right')
                clicks+=1
                cor_A = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(131, 207, 141),tolerance = 10)  
                cor_B = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(254, 254, 254),tolerance = 10) 
                cor_C = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(57, 133, 66),tolerance = 10) 
                pixel_match = cor_A or cor_B or cor_C
    
        else: 
            while pixel_match:
                pydirectinput.press('space')#entrar no menu de golpes
                time.sleep(2)
                pydirectinput.press('space')#clicar no primeiro ataque
                time.sleep(3)
                cor_A = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(131, 207, 141),tolerance = 10)  
                cor_B = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(254, 254, 254),tolerance = 10) 
                cor_C = pixel_match = pyautogui.pixelMatchesColor(coordenada_base[0],coordenada_base[1],(57, 133, 66),tolerance = 10) 
                pixel_match = cor_A or cor_B or cor_C
   




function()
