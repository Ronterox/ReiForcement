import pyautogui as pygui
import pydirectinput as pydir
import random
import time
import os

# pygui.moveTo(100, 100, duration = 1)
scr = pygui.size()
WIDTH, HEIGHT = scr.width, scr.height

w,h=300,400

rx,ry = WIDTH*0.5 - w, HEIGHT*0.5 - h

img = pygui.screenshot('img.png', region=(rx, ry, w + w * 0.5, h))
# os.system('start img.png')
pygui.click(WIDTH * 0.5, HEIGHT * 0.5)

def click_around():
    xlen = range(0, round(w + w * 0.5), 20)
    for y in range(0, h, 40):
        for x in xlen:
            r,g,b = img.getpixel((x, y))
            if random.choice([0,1]) and  r < 100 and g < 100 and b < 100:
                pygui.click(x * 2 + rx, y + ry, 1)
                break

for _ in range(10):
    click_around()
