"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

swidth = 640
sheight = 480

grey = Color(0x808080, 1)
nostroke = LineStyle(0, grey)
livecells = {}

class Cell(Sprite):
    pix = RectangleAsset(20, 20, nostroke, grey)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        livecells[position] = True
    
    def step(self):
        self.GFX.destroy()
        
class Conway(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        Cell(0, 0)
        Cell(0, 20)
        
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
    
    

myapp = Conway(swidth, sheight)
myapp.run()






