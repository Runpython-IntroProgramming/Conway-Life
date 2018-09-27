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


#making list of grid coordinates
width = myapp.width
height = myapp.height
grid = []
cells = []
newcells = []
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
nocolor = Color(0xfffafa,1)
line = LineStyle(1, white)
noline = LineStyle(1,nocolor)

# Background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, white)
bg = Sprite(bg_asset, (0,0))

#----------------------------------------------------------------------------------------
class NewCell(Sprite):
    asset = RectangleAsset(10, 10, line, green)
    def __init__(self,  position):
        super().__init__(NewCell.asset, position)

class OldCell(Sprite):
    asset=RectangleAsset(10, 10, line, pink)
    def __init__(self,position):
        super().__init__(OldCell.asset, position)

class NoCell(Sprite):
    asset = RectangleAsset(10, 10, noline, nocolor)
    def __init__(self,  position):
        super().__init__(NoCell.asset, position)

#----------------------------------------------------------------------------------------
def Click(event):
    global newcells
    close_x=int(round(event.x,-1))
    close_y=int(round(event.y,-1))
    NewCell((close_x,close_y))
    newcells.append((close_x,close_y))

def Down(event):
    global z
    z = 1
    
def Up(event):
    global z
    z = 0
    
def MouseMove(event):
    global newcells, z
    close_x=int(round(event.x,-1))
    close_y=int(round(event.y,-1))
    if z==1:
        NewCell((close_x,close_y))
        if (close_x,close_y) not in newcells:
            newcells.append((close_x,close_y))

#----------------------------------------------------------------------------------------    
def step():
    global  newcells
    cells = []
    for (m, n) in newcells:
        cells.append((m, n))
    newcells = []

    #check all alive cells if they have 3 alive cells around them
    for (m, n) in cells:
        surrounding = []
        g = 0
        for x in range(m-10, m+20, 10):
            for y in range(n-10, n+20, 10):
                surrounding.append((x, y))
        
        surrounding.remove((m, n))
        for (p, r) in surrounding:
            if (p, r) in cells:
                g += 1
    
        if g == 3 or g == 2:
            OldCell((m, n))
            newcells.append((m, n))
        else:
            NoCell((m, n))
    
    #create list of all surroundings cells of current alive cells
    scells = []
    for (m, n) in cells:
        for x in range(m-10, m+20, 10):
            for y in range(n-10, n+20, 10):
                if (x,y) not in scells:
                    scells.append((x, y))
    
    for (m, n) in cells:
        if (m, n) in scells:
            scells.remove((m, n))
    
    #check all surrounding cells if they have 3 alive cells around them            
    for (m, n) in scells:
        surrounding = []
        g = 0
        for x in range(m-10, m+20, 10):
            for y in range(n-10, n+20, 10):
                surrounding.append((x, y))
        
        surrounding.remove((m, n))
        for (p, r) in surrounding:
            if (p, r) in cells:
                g += 1

        if g == 3:
            NewCell((m, n))
            newcells.append((m, n))
        

myapp.run(step)
myapp.listenMouseEvent('click',Click)
myapp.listenMouseEvent('mousedown',Down)
myapp.listenMouseEvent('mouseup',Up)
myapp.listenMouseEvent('mousemove',MouseMove)
myapp.listenKeyEvent('keydown','space',Go)



