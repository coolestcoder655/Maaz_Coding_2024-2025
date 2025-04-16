import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

pyautogui.moveTo(320, 320)

while True:
    pyautogui.press("left")
    pyautogui.press("right")