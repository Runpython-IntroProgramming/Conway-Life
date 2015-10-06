"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle

grey = Color(0x808080, 1.0)
dark = Color(0x333333, 1.0)
nostroke = LineStyle(0, black)

pixel = RectangleAsset(10, 10, nostroke, grey)

field = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def createfield(y):
    pixelline = [Sprite(pixel, (x, y)) for x in range(0, 640, 8)]
g = 0
for b in field:
    if b == 1:
        x = (10 % field[g]) * 11
        y = (field[g] / 10) * 11
        Sprite(pixel, (x, y))
    g += 1

myapp = App()
myapp.run()
