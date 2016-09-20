"""
conway.py
Author: Peter Bynum
Credit: <list sources used, if any>
Assignment: Conway's Game of life
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 151
SCREEN_HEIGHT = 101
black = Color(0, 1)
green = Color(0x408000, 1.0)
white = Color(0xffffff, 1.0)
border = LineStyle(2, black)
line = LineStyle(1, black)

class Cell(Sprite):
    asset = RectangleAsset(10,10, line, white)
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.fxcenter = self.fycenter = 0
    
    def step(self):#Step needs to 1. cycle through generations, 2. detect if mouse is over then create life, 3. Change color of new life to black after first cycle
        if createlife = True and 

class Conway(App):
    list = [[0 for col in range(0,15)] for row in range(0,10)]

    

    def mousedown(event):
        createlife = True
    
    def mouseup(event):
        createlife = False
    
    def step(self):
        for Cell in self.getSpritebyClass(Cell):
            Cell.step()

#Step needs to 1. cycle through generations, 2. detect if mouse is over then create life, 3. Change color of new life to black after first cycle


myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
#add mouse sensing here
myapp.run()