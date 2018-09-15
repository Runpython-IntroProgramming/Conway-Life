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
#-----------------------------------------------------
from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
from random import randint
#-----------------------------------------------------
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
green  = Color(0x0fff6f, 1.0)
white = Color(0xffffff, 1.0)
noLine  = LineStyle(0, black)
outLine = LineStyle(1, white)
outLive = LineStyle(1, green)
#-----------------------------------------------------
frameWidth = 800
frameHeight = 800
cellSide = 5
cells = {}
for i in range(0, 10):
    for k in range(0, 10):
        """
        if randint(0,5) == 4:
            cells[(k * 10,i * 10)] = "alive"
        else:
            cells[(k * 10,i * 10)] = "dead"
        """
        cells[(k * 10, i * 10)] = "dead"
#-----------------------------------------------------
class cell(Sprite):
    deadCell = RectangleAsset(10,10, outLine, black)
    liveCell = CircleAsset(5, outLive, blue)

    def __init__(self, position, state):
        if state == "alive":
            super().__init__(cell.liveCell, position)
        else:
            super().__init__(cell.deadCell, position)

   
#-----------------------------------------------------
class GameOfLife(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        bg = RectangleAsset(frameWidth, frameHeight, noLine, black)
        Sprite(bg, (0,0))
        GameOfLife.listenKeyEvent("keydown", "space",self.spacePressed)
        #ConwayGame.listenMouseEvent("click",self.----)
        for l in cells.keys():
            cell(l,cells[l])
    def step(self):
        for sprite in self.getSpritesbyClass(cell):
            cellsNearby = 0
            for i in range(-1,2):
                for k in range(-1,2):
                    if (i,k) != (sprite.x, sprite.y):
                        if cells[(i,k)] == "alive":
                            cellsNearby += 1
            if cellsNearby < 2:
                cells[sprite.x, sprite.y] = "dead"
            elif cellsNearby > 3:
                cells[sprite.x, sprite,y] = "dead"
    
    def spacePressed(self, event):
        cells[(20, 20)] = "alive"
        
        
#-----------------------------------------------------
myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()
