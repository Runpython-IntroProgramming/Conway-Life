"""
conway.py
Author: Peter Bynum
Credit: <list sources used, if any>
Assignment: Conway's Game of life
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 151
SCREEN_HEIGHT = 101
black = Color(0, 1)
green = Color(0x408000, 1.0)
white = Color(0xffffff, 1.0)
border = LineStyle(2, black)
line = LineStyle(1, black)
"""
spritelist = [[(1, 0, 0), (0, 1, 0), (0, 2, 0)], [(1, 0, 1), (2, 1, 1), (0, 2, 1)], [(1, 0, 2), (2, 1, 2), (0, 2, 2)]]
print(spritelist)
def countneighbors(row, col):
        s = 0
        print(col, row)
        if col+1 <= 2 and row+1 <= 2 and col-1 >= 0 and row-1 >= 0: # center
            if spritelist[col-1][row-1][0] == 1 or spritelist[col-1][row-1][0] == 2: #7
                s += 1
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2: #4
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2: #8
                s += 1
            if spritelist[col-1][row+1][0] == 1 or spritelist[col-1][row+1][0] == 2: #1
                s += 1
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2: #2
                s += 1
            if spritelist[col+1][row-1][0] == 1 or spritelist[col+1][row-1][0] == 2: #9
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2: #6
                s += 1
            if spritelist[col+1][row+1][0] == 1 or spritelist[col+1][row+1][0] == 2: #3
                s += 1
        elif col+1 <= 2 and row+1 <= 2 and col-1 >=0 and row-1 < 0: #top middle
            if spritelist[col-1][row+1][0] == 1 or spritelist[col-1][row+1][0] == 2: #1
                s += 1
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2: #2
                s += 1
            if spritelist[col+1][row+1][0] == 1 or spritelist[col+1][row+1][0] == 2: #3
                s += 1
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2: #4
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2: #6
                s += 1
        elif col+1 <= 2 and row+1 <= 2 and col-1 < 0 and row-1 >= 0: #left middle
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2: #2
                s += 1
            if spritelist[col+1][row+1][0] == 1 or spritelist[col+1][row+1][0] == 2: #3
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2: #6
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2: #8
                s += 1
            if spritelist[col+1][row-1][0] == 1 or spritelist[col+1][row-1][0] == 2: #9
                s += 1
        elif col+1 <= 2 and row+1 > 2 and col-1 >= 0 and row-1 >= 0: #bottom middle
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2: #4
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2: #6
                s += 1
            if spritelist[col-1][row-1][0] == 1 or spritelist[col-1][row-1][0] == 2: #7
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2: #8
                s += 1
            if spritelist[col+1][row-1][0] == 1 or spritelist[col+1][row-1][0] == 2: #9
                s += 1
        elif col+1 > 2 and row+1 <= 2 and col-1 >= 0 and row-1 >= 0: #right middle
            if spritelist[col-1][row+1][0] == 1 or spritelist[col-1][row+1][0] == 2: #1
                s += 1
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2: #2
                s += 1
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2: #4
                s += 1
            if spritelist[col-1][row-1][0] == 1 or spritelist[col-1][row-1][0] == 2: #7
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2: #8
                s += 1
        elif col+1 <= 2 and row+1 <= 2 and col-1 < 0 and row-1 < 0: #left upper corner
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2: #2
                s += 1
            if spritelist[col+1][row+1][0] == 1 or spritelist[col+1][row+1][0] == 2: #3
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2: #6
                s += 1
        elif col+1 > 2 and row+1 <= 2 and col-1 >= 0 and row-1 < 0: #right upper corner
            if spritelist[col-1][row+1][0] == 1 or spritelist[col-1][row+1][0] == 2: #1
                s += 1
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2: #2
                s += 1
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2: #4
                s += 1
        elif col+1 > 2 and row+1 > 2 and col-1 >= 0 and row-1 >= 0: #right lower corner
            if spritelist[col-1][row-1][0] == 1 or spritelist[col-1][row-1][0] == 2: #7
                s += 1
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2: #4
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2: #8
                s += 1
        elif col+1 <= 2 and row+1 > 2 and col-1 < 0 and row-1 >= 0: #left lower corner
            if spritelist[col+1][row-1][0] == 1 or spritelist[col+1][row-1][0] == 2: #9
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2: #6
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2: #8
                s += 1
        print(s)
        return s
if countneighbors(2,1) == 2:
    print("yes")
"""

asset = ImageAsset("conwaysprites.png",
    Frame(0,0,10,10), 3, 'horizontal')
cell = Sprite(asset, (0,0))
cell.phase = 0
cell.setImage(2)

def step():
    if cell.phase == 0:
        cell.setImage(2)
    if cell.phase == 1:
        cell.setImage(1)
    if cell.phase == 2:
        cell.setImage(0)

def changecolor(event):
    print(cell.x)
    print(cell.y)
    cell.phase += 1
    if cell.phase == 3:
        cell.phase = 0


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', changecolor)
myapp.run(step)