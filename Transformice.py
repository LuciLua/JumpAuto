#flood


import pyautogui, time, msvcrt, keyboard
time.sleep(1)

while True:
    if keyboard.is_pressed("<"):

        pyautogui.keyDown('left')
        time.sleep(0.3)
        pyautogui.keyUp('left')

        pyautogui.keyDown('right')
        time.sleep(0.008)
        pyautogui.keyUp('right')

        pyautogui.keyDown('up')
        time.sleep(0.01)
        pyautogui.keyUp('up')

    if keyboard.is_pressed(">"):

        pyautogui.keyDown('right')
        time.sleep(0.3)
        pyautogui.keyUp('right')

        pyautogui.keyDown('left')
        time.sleep(0.008)
        pyautogui.keyUp('left')

        pyautogui.keyDown('up')
        time.sleep(0.01)
        pyautogui.keyUp('up')


    elif keyboard.is_pressed("e"):
        break
        

else:
    print('interrompe')
    exit()
