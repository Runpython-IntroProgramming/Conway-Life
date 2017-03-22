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
    asset=RectangleAsset(11,11,line, blue)
    def __init__(self, position):
        super().__init__(cell.asset, position)
        
def mouseClick(event):
    cell((round(event.x,-1),round(event.y,-1)))


        

myapp = App()
myapp.run()
myapp.listenMouseEvent('click', mouseClick)