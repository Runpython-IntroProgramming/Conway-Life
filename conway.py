"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset, http://stackoverflow.com/questions/26454649/python-round-up-to-the-nearest-ten
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle
import math

grey = Color(0x808080, 1.0)
dark = Color(0x333333, 1.0)
nostroke = LineStyle(0, black)

pixel = RectangleAsset(10, 10, nostroke, grey)

field = []
[field.append(1) for x in range(0, 30)]

g = 0
for b in field:
    g += 1
    if b == 1:
        x = (g % 10) * 11
        y = int(math.floor(g / 10.0)) * 11
        Sprite(pixel, (x, y))
        print(x , y)
    

myapp = App()
myapp.run()
