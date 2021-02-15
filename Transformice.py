#flood


import pyautogui, time, msvcrt, keyboard
time.sleep(1)

print(pyautogui.position())

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

'''
for word in f:

    pyautogui.keyDown('right')
    time.sleep(0.15)
    pyautogui.keyUp('right')

    pyautogui.keyDown('up')
    time.sleep(0.01)
    pyautogui.keyUp('up')

    pyautogui.keyDown('left')
    time.sleep(0.02)
    pyautogui.keyUp('left')

exit()

'''
