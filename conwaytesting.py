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

    
spritelist = [[(0, 0, 0), (1, 1, 0), (0, 2, 0)], [(2, 0, 1), (0, 1, 1), (0, 2, 1)], [(0, 0, 2), (0, 1, 2), (0, 2, 2)]]
print(spritelist)
col = 1
row = 1
def countneighbors(col, row):
        s = 0
        if col+1 <= 2 and row+1 <= 2 and col-1 >= 0 and row-1 >= 0:
            if spritelist[col-1][row-1][0] == 1 or spritelist[col-1][row-1][0] == 2:
                s += 1
            if spritelist[col-1][row][0] == 1 or spritelist[col-1][row][0] == 2:
                s += 1
            if spritelist[col][row-1][0] == 1 or spritelist[col][row-1][0] == 2:
                s += 1
            if spritelist[col-1][row+1][0] == 1 or spritelist[col-1][row+1][0] == 2:
                s += 1
            if spritelist[col][row+1][0] == 1 or spritelist[col][row+1][0] == 2:
                s += 1
            if spritelist[col+1][row-1][0] == 1 or spritelist[col+1][row-1][0] == 2:
                s += 1
            if spritelist[col+1][row][0] == 1 or spritelist[col+1][row][0] == 2:
                s += 1
            if spritelist[col+1][row+1][0] == 1 or spritelist[col+1][row+1][0] == 2:
                s += 1
        if col+1
        if col+1 <= 2 and row+1 > 2:
        print(s)
        return s
if countneighbors(2,1) == 2:
    print("yes")

