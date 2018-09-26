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
z = 0
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
    def __init__(self,  position):
        super().__init__(NewCell.asset, position)

class OldCell(Sprite):
    asset=RectangleAsset(10, 10, line, pink)
    def __init__(self,position):
        super().__init__(Old.asset, position)

def Click(event):
    global cells, grid
    close_x=(event.x//10)*10
    close_y=(event.y//10)*10
    NewCell((close_x,close_y))
    cells.append((close_x,close_y))
    grid.remove((close_x,close_y))
    print(close_x)

def Down(event):
    global z
    z = 1
    
def Up(event):
    global z
    z = 0
    
def MouseMove(event):
    global cells, grid, z
    close_x=round(event.x//10,0)*10
    close_y=round(event.y//10,0)*10
    print(close_x)
    if z==1:
        NewCell((close_x,close_y))
        cells.append((close_x,close_y))
        grid.remove((close_x,close_y))
    
#def step():
    global cells, grid, newcells
    for (m, n) in cells:
        surrounding = []
        g = 0
        print(m-10)
        for x in range(m-10, m+10, 10):
            for y in range(n-10, n+10, 10):
                surrounding.append((x, y))
        
        surrounding.remove((m, n))
        for (p, r) in surroundings:
            if (p, r) in cells:
                g += 1
        
        if g >= 3:
            OldCell((m, n))
        else:
            cells.remove((m ,n))
    
    for (m, n) in grid:
        surrounding = []
        g = 0
        for x in range(m-10, m+10, 10):
            for y in range(n-10, n+10, 10):
                surrounding.append((x, y))
        
        surrounding.remove((m, n))
        for (p, r) in surroundings:
            if (p, r) in cells:
                g += 1
        
        if g >= 3:
            NewCell((m, n))
            grid.remove((m, n))
            cells.append((m, n))
            

myapp.run()
myapp.listenMouseEvent('click',Click)
myapp.listenMouseEvent('mousedown',Down)
myapp.listenMouseEvent('mouseup',Up)
myapp.listenMouseEvent('mousemove',MouseMove)
# make a list newcells that puts the x,y coordinates of the mouse click
# Need to make it draggable
# Step function that transfers newcells list to old cells
# checks all the surrounding cells and add 1 to a variable
# if variable >3 make new cell


