"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""



from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))

myapp = SpaceGame()
"""
Rules:
Player makes initial layout
Ways for game to end: all cells die,
no cells change from one generation to the next, 
or the pattern flips back and forth between two or more positions.

How cells work:
Births: Each dead cell adjacent to exactly three live neighbors will become live in the next generation.
Death by isolation: Each live cell with one or fewer live neighbors will die in the next generation.
Death by overcrowding: Each live cell with four or more live neighbors will die in the next generation.
Survival: Each live cell with either two or three live neighbors will remain alive for the next generation.

Corners Do Count)
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import floor
#colors
red = Color(0xFF4040, 1.0)
green = Color(0x00FF00, 1.0)
blue = Color(0x1C86EE, 1.0)
white = Color(0xF8F8FF, 1.0)
orange = Color(0xFF7D40, 1.0)

thinline = LineStyle(1, white)

#Making the grid
#once each click fills the closed box, make grid black to fill in with back ground
line1 = RectangleAsset(1,400, thinline, white)
line2 = RectangleAsset(400,1, thinline, white)
for x in range(11):
    Sprite(line1, (x*40, 0))
    Sprite(line2, (0, x*40))

#Making user be able to click 

cell_asset = RectangleAsset(40,40,thinline, green)
#cell = Sprite(cell_asset, (0,0))
def mouseClick(event):
    #cell.x = event.x
    #cell.y = event.y 
#making a rectangle in closest box
    x = floor(event.x/40)*40 
    y = floor(event.y/40)*40
    if x < 400 and y < 400:
        Sprite(cell_asset,(x, y))

    
myapp.listenMouseEvent('click', mouseClick)
myapp.run()
