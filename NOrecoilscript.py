# LIBRARIES

import pyautogui
from pynput.mouse import Button, Controller
import win32api
import time
import json

# Main menu
time.sleep(0.3)
print('''
███    ██  ██████  ██████  ███████  ██████  ██████  ██ ██      
████   ██ ██    ██ ██   ██ ██      ██      ██    ██ ██ ██      
██ ██  ██ ██    ██ ██████  █████   ██      ██    ██ ██ ██      
██  ██ ██ ██    ██ ██   ██ ██      ██      ██    ██ ██ ██      
██   ████  ██████  ██   ██ ███████  ██████  ██████  ██ ███████\n''')
time.sleep(0.2)
print('                          by R4las\n')

print('The script is starting...')
#DATAS

# opening json
with open("data.json") as file:
    data = json.load(file)


# convert string data in integers
cadenceForSec = int(data.get("cadenceForSec"))
moveX = int(data.get("X"))
moveY = int(data.get("Y"))

# run mouse
mouse = Controller()

# sleep
sleepMoving = 1000/cadenceForSec

print('The script is started!\n')

def NOrecoil():
    try:
        while True:

            leftState = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
            rightState = win32api.GetKeyState(0x02)

            if leftState < 0 and rightState < 0:
                muoseX, muoseY = pyautogui.position()
                pyautogui.moveTo(muoseX-moveX, muoseY-moveY)
                time.sleep(sleepMoving/1000)

            else:
                pass
    except:
        print('You entered SAFE mode for 5 seconds as you hit the corner\n')
        time.sleep(5)
        NOrecoil()

NOrecoil()