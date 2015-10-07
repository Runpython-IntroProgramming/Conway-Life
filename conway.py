"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset, http://stackoverflow.com/questions/26454649/python-round-up-to-the-nearest-ten
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle


grey = Color(0x808080, 1.0)
dark = Color(0x808080, 1.0)
nostroke = LineStyle(0, grey)
class pixel(Sprite):
    pix = RectangleAsset(10,10,nostroke,grey)
    def __init__(self, x, y):
        Sprite(pix, (x, y))
    
pixel(40,49)


    
    

myapp = App()
myapp.run()






