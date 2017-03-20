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
    asset=RectangleAsset(100,100,line, blue)
    def __init__(self, position):
        super().__init__(cell.asset, position)
        
class Conwaygame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
    cell((100,100))
    
myapp = Conwaygame(700,800)
myapp.listenKeyEvent('keydown', 'space', rightkey)
myapp.listenKeyEvent('keydown', 'r', leftkey)
myapp.listenKeyEvent('keydown', 'space', upkey)
myapp.listenKeyEvent('keydown', 'r', downkey)
myapp.listenMouseEvent('click', mouseClick)