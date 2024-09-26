import pyautogui
from time import sleep
sleep(2)
value = int(input())
sleep(5)
for i in range(1, value + 1):
    for j in range(i):
        pyautogui.write("#")
    pyautogui.press('enter')