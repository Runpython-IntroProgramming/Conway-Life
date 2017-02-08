"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 660
SCREEN_HEIGHT = 510

# Colors
black = Color(0, 1)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
# Background

noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
bg = Sprite(bg_asset, (0,0))


cellframe = RectangleAsset(20, 30, noline, gray)
cf1 = Sprite(cellframe)

celllist = list(range(1, 496))
i = 0
x = 0
y = 0
while i < 1:
    


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()