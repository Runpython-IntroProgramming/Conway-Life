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
    cell = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        self.x = x-position
        self.y = y-position



class Conways(App):
    def _init__(self, width, height):
        super().__init__(width, height)
        green = Color(0x00ff00, 1)
        blackline = LineStyle(1, green)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, blackline, green)
        Sprite(bg_asset, (0,0))
        celloutline = RectangleAsset(CELLWIDTH, CELLHEIGHT, blackline, white)
        #for x in range(0, SCREEN_WIDTH, CELLWIDTH):
            #Sprite(celloutline)
        Cell((10, 10))

myapp = Conways(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()