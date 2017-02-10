"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
#Set Up
SCREEN_WIDTH = 660
SCREEN_HEIGHT = 510
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenMouseEvent('click', mouseClick)

# Colors
black = Color(0, 1)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
# Background

noline = LineStyle(0, black)
thinline = LineStyle(1, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
bg = Sprite(bg_asset, (0,0))


cf = RectangleAsset(20, 30, thinline, gray)

#Cell Class
class Cell(Sprite):
    def _init_(self, position, state)
    super()._init_(
celllist = list(range(1, 563))
i = 0
x = 0
y = 0
c = 0
while i != 1:
    celllist[c] = Sprite(cf, (x, y))
    if y > (SCREEN_HEIGHT - 30):
        i=1
    elif x > (SCREEN_WIDTH - 20):
        x=0
        y=y+30
    else:
        x=x+20
        c= c+1
#User Inpu
def spaceKey(event):
    


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()