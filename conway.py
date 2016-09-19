"""
conway.py
Author: Peter Bynum
Credit: <list sources used, if any>
Assignment: Conway's Game of life
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1201
SCREEN_HEIGHT = 800
black = Color(0, 1)
green = Color(0x408000, 1.0)
white = Color(0xffffff, 1.0)
border = LineStyle(2, black)
line = LineStyle(1, black)

class Cell(Sprite):
    asset = RectangleAsset(10,10, line, white)
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        

class Conway(App):
    bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, border, white)
    bg = Sprite(bg_asset, (0,0))
    for row in range(0,120):
        Cell((row*10,0))


myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()