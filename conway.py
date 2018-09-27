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

print ("""
WELCOME TO CONWAY'S GAME OF LIFE!

Rules:
1. Any live cell with < 2 live neighbors dies
2. Any live cell with 2 or 3 live neighbors lives
3. Any live cell with > 3 live neighbors dies
4. Any dead cell with 3 live neighbors becomes a live cell

How to Play:
Add live cells by dragging or clicking the screen using the mouse
Start and stop the game using the spacebar
""")

#creating variables and blank lists
width = myapp.width
height = myapp.height
newcells = []
go = False
z = 0

#colors for game#
black = Color(0, 1)
pink = Color(0xee1289, 1)
green = Color(0x66cdaa4, 1)
nocolor = Color(0xfffafa,1)
line = LineStyle(1, nocolor)
noline = LineStyle(1,nocolor)

# Background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, nocolor)
bg = Sprite(bg_asset, (0,0))

#----------------------------------------------------------------------------------------
class NewCell(Sprite):
    asset = RectangleAsset(15, 15, line, green)
    def __init__(self,  position):
        super().__init__(NewCell.asset, position)

class OldCell(Sprite):
    asset=RectangleAsset(15, 15, line, pink)
    def __init__(self,position):
        super().__init__(OldCell.asset, position)

class NoCell(Sprite):
    asset = RectangleAsset(15, 15, noline, nocolor)
    def __init__(self,  position):
        super().__init__(NoCell.asset, position)

#----------------------------------------------------------------------------------------
def Click(event):
    global newcells
    close_x=int((event.x//15)*15)
    close_y=int((event.y//15)*15)
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
    close_x=int((event.x//15)*15)
    close_y=int((event.y//15)*15)
    if z==1:
        NewCell((close_x,close_y))
        if (close_x,close_y) not in newcells:
            newcells.append((close_x,close_y))

def Go(event):
    global go
    go = not go
    if go == True:
        print("Game is started")
    else:
        print("Game is stopped")
#----------------------------------------------------------------------------------------    
def step():
    global go
    if go == True:
        global  newcells
        cells = []
        for (m, n) in newcells:
            cells.append((m, n))
        newcells = []
        
        #create list of cells to check
        check_cells = []
        for (m, n) in cells:
            for x in range(m-15, m+30, 15):
                for y in range(n-15, n+30, 15):
                    if (x,y) not in check_cells:
                        check_cells.append((x, y))
        
        #check cells if they have 3 alive cells around them            
        for (m, n) in check_cells:
            surrounding = []
            g = 0
            for x in range(m-15, m+30, 15):
                for y in range(n-15, n+30, 15):
                    surrounding.append((x, y))
            
            surrounding.remove((m, n))
            for (p, r) in surrounding:
                if (p, r) in cells:
                    g += 1
    
            if g == 3 and (m,n) not in cells:
                NewCell((m, n))
                newcells.append((m, n))
            elif (m, n) in cells:
                if g == 3 or g == 2:
                    OldCell((m, n))
                    newcells.append((m, n))
                else:
                    NoCell((m, n))



myapp.run(step)
myapp.listenMouseEvent('click',Click)
myapp.listenMouseEvent('mousedown',Down)
myapp.listenMouseEvent('mouseup',Up)
myapp.listenMouseEvent('mousemove',MouseMove)
myapp.listenKeyEvent('keydown','space',Go)