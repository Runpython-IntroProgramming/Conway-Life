"""
conway.py
Author: johannes testorf
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life


myapp = App()
myapp.run()
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)


width=list(range(0,64))
height = list(range(0,48))

thinline = LineStyle(1, black)

for x in width
    for y in height
        rectangle = RectangleAsset(x, y, thinline, white)