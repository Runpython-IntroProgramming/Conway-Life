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
        self.row = position[1]/10
        self.col = position[0]/10

    """
    def step(self)
    
    """
    #def step(self):Step needs to 1. cycle through generations, 2. detect if mouse is over then create life, 3. Change color of new life to black after first cycle

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(0,15):
            for y in range(0,10):
                Cell((10*x,10*y))
    

    

    def mousedown(self, event):
        createlife = True

    def mousemove(self, event):
        mousex = event.x
        mousey = event.y

    def mouseup(self, event):
        createlife = False
    
    def step(self):
        for Cell in self.getSpritebyClass(Cell):
            Cell.step()

#Step needs to 1. cycle through generations, 2. detect if mouse is over then create life, 3. Change color of new life to black after first cycle


myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mousedown', myapp.mousedown)
myapp.listenMouseEvent('mouseup', myapp.mouseup)
myapp.listenMouseEvent('mousemove', myapp.mousemove)
myapp.run()