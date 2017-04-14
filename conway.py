"""
conway.py
Author: Abby Feyrer
Credit: Mr. Dennison
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound
import time

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 80
space=0
z=0
g=0
allthecells=[]
xs=list(range(11))
ys=list(range(9))
grid=[]
removal=[]
addition=[]
seconddays=[]
for x in xs:
    for y in ys: 
        grid.append((10*x,10*y))
#grid.remove((10000,10000))

blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
white = Color(0xfffafa,1)
green = Color(0x00ff00, 1)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, white)
bg = Sprite(bg_asset, (0,0))

tens=lambda x: round(x,-1)

class cell(Sprite):
    asset=RectangleAsset(11,11,line, blue)
    def __init__(self, position):
        super().__init__(cell.asset, position)
        
class notcell(Sprite):
    asset=RectangleAsset(11,11,line, white)
    def __init__(self, position):
        super().__init__(notcell.asset, position)

class cell1(Sprite):
    asset=RectangleAsset(11,11,line, purple)
    def __init__(self, position):
        super().__init__(cell1.asset, position)

def mousebuttondown(event):
    global z
    z=1
def mousebuttonup(event):
    global z
    z=0
    
def mousemove(event):
    global allthecells, grid
    if z==1:
        cell((tens(event.x-12),tens(event.y-15)))
        coordinates=[(tens(event.x-12),tens(event.y-15))]
        for (x,y) in coordinates:
            if (x,y) not in allthecells:
                allthecells.append((x,y))
                grid.remove((x,y))
                coordinates.remove((x,y))

def spaceKey(event):
    global grid, removal, allthecells, addition, g
    if g==1:
        for (x,y) in grid:
            b=0
            for (h,k) in allthecells:
                if (x-h)<=10 and (x-h)>=-10 and (y-k)<=10 and (y-k)>=-10:
                    b=b+1
            if b==3:
                addition.append((x,y))
        for (h,k) in allthecells:
            a=0
            for (x,y) in allthecells:
                if (x-h)<=10 and (x-h)>=-10 and (y-k)<=10 and (y-k)>=-10:
                    a=a+1
            if a==4 or a==3:
                seconddays.append((h,k))
            if a==2 or a==1 or a>4:
                removal.append((h,k))
        print("ok")
        g=0
    if g==0:
        for (x,y) in addition:
            if (x,y) in grid:
                cell((x,y))
                allthecells.append((x,y))
                grid.remove((x,y))
                addition.remove((x,y))
        for (x,y) in seconddays: 
                cell1((x,y))
        for (x,y) in removal:
            notcell((x,y))
            grid.append((x,y))
            allthecells.remove((x,y))
            removal.remove((x,y))
        print("well")
    g=1
  
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenMouseEvent('mousedown', mousebuttondown)
myapp.listenMouseEvent('mouseup', mousebuttonup)
myapp.listenMouseEvent('mousemove', mousemove)
myapp.listenKeyEvent('keydown', 'space', spaceKey)