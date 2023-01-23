import pyautogui as pg
import time
time.sleep(5)
f = open('code.txt', 'r')
for words in f:
    pg.typewrite(words)
#    pg.press("enter")
