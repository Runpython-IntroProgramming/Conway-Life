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
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
white = Color(0xfffafa,1)
green = Color(0x00ff00, 1)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, white)
bg = Sprite(bg_asset, (0,0))

tens=lambda x: round(x,-1)

class notcell(Sprite):
    asset=RectangleAsset(11,11,line,white)
    def __init__(self, position):
        super().__init__(notcell.asset, position)

class cell(Sprite):
    asset=RectangleAsset(11,11,line, blue)
    
    asset=RectangleAsset(11,11,line,purple)
    def __init__(self, position):
        super().__init__(cell.asset, position)
        
def mousebuttondown(event):
    cell((tens(event.x-12),tens(event.y-15)))


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenMouseEvent('mousedown', mousebuttondown)