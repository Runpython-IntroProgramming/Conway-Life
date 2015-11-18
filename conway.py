"""
conway.py
Author: Dimitri
Credit: Wikipedia
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELLWIDTH = 10
CELLHEIGHT = 10

black = Color(0, 1)
white = Color(0xffffff, 1)
noline = LineStyle(0, white)
blackline = LineStyle(.1, black)




class Cell(Sprite):
    asset = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        
    def step():
        
    


class Conways(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, white)
        bg = Sprite(bg_asset, (0,0))
        Cell((100, 100))
        Cell((90, 100))
        Cell((110, 100))
    
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        


myapp = Conways(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
