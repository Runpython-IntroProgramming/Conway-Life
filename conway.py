"""
conway.py
Author: Noah Pikielny
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
#Any live cell with fewer than two live neighbors dies, as if by under population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by overpopulation.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
from random import randint
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
green  = Color(0x696969, 1.0)
white = Color(0xffffff, 1.0)
noLine  = LineStyle(0, black)
outLine = LineStyle(1, white)

frameWidth = 800
frameHeight = 800
cellSide = 5
cells = {}
for i in range(0, 50):
    for k in range(0, 50):
        if randint(0,5) == 4:
            cells[(k * 10,i * 10)] = "alive"
        else:
            cells[(k * 10,i * 10)] = "dead"


class GameOfLife(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        bg = RectangleAsset(frameWidth, frameHeight, noLine, black)
        Sprite(bg, (0,0))
        #cell = CircleAsset(10, noLine, blue)
        for l in cells.keys():
            cell(l,cells[l])
    

class cell(Sprite):
    deadCell = RectangleAsset(10,10, outLine, black)
    liveCell = CircleAsset(5, outLine, green)

    def __init__(self, position, state):
        if state == "alive":
            super().__init__(cell.liveCell, position)
        else:
            super().__init__(cell.deadCell, position)

myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()
