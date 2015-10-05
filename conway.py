"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""

from ggame import App, Color, Sprite, RectangleAsset, LineStyle

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
brown = Color(0xd38d5f, 1.0)
yellow = Color(0xffd42a, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0x808080, 1.0)
dark = Color(0x333333, 1.0)
nostroke = LineStyle(0, black)

pixel = RectangleAsset(5, 5, nostroke, grey)

def createline(y):
    pixelline = [Sprite(pixel, (x, y)) for x in range(0, 960, 6)]

[createline(b) for b in range(0, 480, 6)]

myapp = App()
myapp.run()