"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

grey = Color(0x808080, 0.6)
dark = Color(0x808080, 1.0)
nostroke = LineStyle(0, grey)
class Cell(Sprite):
    
    pix = RectangleAsset(10, 10, nostroke, grey)
    
    def __init__(self, x, y):
        Sprite(Cell.pix, (x, y))
        click = True
        if click == True:
            self.color = dark
        else:
            self.color = grey
    
Cell(0, 15)


    
    

myapp = App()
myapp.run()






