import pyautogui, pydirectinput
import time

print('\n\n\nprepare-se...\n\n\n')
time.sleep(3)

def function():
    clicks = 0
    while clicks < 6:
        pydirectinput.press('left')
        clicks+=1

    clicks = 0
    while clicks < 6:
        pydirectinput.press('right')
        clicks+=1

    print('\n\n\nfim...\n\n\n')

#jjjjjjjjjk''/ljjjjjjjj'

function()
