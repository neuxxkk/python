import pyautogui

n=input('')
if n=='up':
    pyautogui.press('playpause',presses=1)
else:
    print(pyautogui.KEYBOARD_KEYS)

pyautogui.KEYBOARD_KEYS