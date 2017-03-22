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

x=1

tens=lambda x: round(x,-1)

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)

class cell(Sprite):
    asset=RectangleAsset(11,11,line, blue)
    
    asset=RectangleAsset(11,11,line,purple)
    def __init__(self, position):
        super().__init__(cell.asset, position)
        
def mouseClick(event):
    cell((tens(event.x-12),tens(event.y-15)))


        

myapp = App()
myapp.run()
myapp.listenMouseEvent('click', mouseClick)