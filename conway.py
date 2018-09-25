"""
conway.py
Author: Emma Tysinger
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import Color, Sound, SoundAsset

myapp = App()

# Background
#black = Color(0, 1)
#noline = LineStyle(0, black)
#bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
#bg = Sprite(bg_asset, (0,0))

#making list of grid coordinates
width = myapp.width
height = myapp.height
grid = []
cells = []
click = []
x_coordinates = list(range(0, width, 10))
y_coordinates = list(range(0, height, 10))
for x in x_coordinates:
    for y in y_coordinates:
        grid.append((x, y))

#colors for game#
black = Color(0, 1)
pink = Color(0xee1289, 1)
green = Color(0x66cdaa4, 1)
nocolor = Color(0, 0)
line = LineStyle(1, black)
noline = LineStyle(1,nocolor)

    

class NewCell(Sprite):
    asset = RectangleAsset(10, 10, line, green)
    # if self.color==1:
    #     asset=RectangleAsset(7,7,line,green)
    # asset=RectangleAsset(7,7,line,green)
    def __init__(self,  position):
        super().__init__(NewCell.asset, position)
        # myapp.listenMouseEvent('mousedown', self.add)
    # def add(self,event):
    #     self.color=1
    #     self.asset=RectangleAsset(7,7,line,green)

class DeadCell(Sprite):
    asset=RectangleAsset(7, 7, line, nocolor)
    def __init__(self,position):
        super().__init__(DeadCell.asset, position)

# for (x, y) in grid:
#     NewCell((x,y))

def Click(event):
    global cells
    close_x=(event.x//10)*10
    close_y=(event.y//10)*10
    NewCell((close_x,close_y))
    cells.append((close_x,close_y))

myapp.run()
myapp.listenMouseEvent('click',Click)




