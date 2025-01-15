import pyautogui as pg
import time
import keyboard
#text
x = -1392
y = 368

#find button
a = -1021
b = 364

c = '058304000000'
# print(pg.position())
for i in range (2669,650000):
    pg.leftClick(x, y)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(c[:len(c)-len(str(i))]+str(i))
    pg.leftClick(a, b)
    if keyboard.is_pressed('esc'):
        break