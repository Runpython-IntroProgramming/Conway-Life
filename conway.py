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
myapp.run()
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

Corners Do Count 
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

white = Color(0xF8F8FF, 1.0)
thinline = LineStyle(1, white)

rectangle = RectangleAsset(1,635, thinline, white)
Sprite(rectangle, (0,0))

rectangle1 = RectangleAsset(1,635, thinline, white)

vline = RectangleAsset(0,0, thinline, white)
#lines
for vl in range(100):
    Sprite(rectangle1, (vl * 150,0))
"""
for hl in range (1000):
    Sprite(rectangle2, (hl * 10,0))
Sprite(rectangle1, (
"""

myapp = App()
myapp.run()



































































