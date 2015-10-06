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

grey = Color(0x808080, 0)
dark = Color(0x808080, 1.0)
nostroke = LineStyle(0, grey)

field = []
[field.append(1) for x in range(0, 1000)]

pix = RectangleAsset(10,10,nostroke,grey)

class Pixel(Sprite):
    def __init__(self, width, height):
        super().__init__(width, height)
    
Pixel(560,430)


    
    

myapp = App()
myapp.run()






