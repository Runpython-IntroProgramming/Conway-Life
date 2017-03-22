"""
conway.py
Author: Abby Feyrer
Credit: None
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""

from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

x=1

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(1,blue)

class cell(Sprite):
    asset=RectangleAsset(10,10,line, blue)
    def __init__(self, position):
        super().__init__(cell.asset, position)
        


class Conwaygame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        cell((100,10))

myapp = Conwaygame(700,800)
myapp.run()
