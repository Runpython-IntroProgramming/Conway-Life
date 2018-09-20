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
from math import floor
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
cellNum = 20
#cellSide = int(frameWidth / (cellNum * 2))
cellSide = 20
cells = {}
cellsLongTerm = {}
#-----------------------------------------------------
class cell(Sprite):
    Cell = CircleAsset(cellSide / 2, outLive, blue)
    oldCell = CircleAsset(cellSide / 2, outLive, red)
    def __init__(self, position):
        if cells[(position)] == "alive":
            super().__init__(cell.Cell, position)
            self.visible = True
        elif cells[position] == "old":
            super().__init__(cell.oldCell, position)
            self.visible = True
        else:
            super().__init__(cell.Cell, position)
            self.visible = False
  

#-----------------------------------------------------
class GameOfLife(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        GameOfLife.listenKeyEvent("keydown", "d",self.spacePressed)
        self.isActive = False
        bg = RectangleAsset(frameWidth, frameHeight, noLine, black)
        Sprite(bg, (0,0))
        frame = 0
        
        for i in range(0, cellNum):
            for k in range(0, cellNum):
                
                if randint(0,2) == 1:
                    cells[(k * cellSide,i * cellSide)] = "alive"
                else:
                    cells[(k * cellSide,i * cellSide)] = "dead"
                
                #cells[(k * cellSide,i * cellSide)] = "dead"
                Sprite(RectangleAsset(cellSide, cellSide, outLine, black), (k * cellSide,i * cellSide))
        for i in cells:
            cellsLongTerm[i] = cells[i]
        GameOfLife.listenMouseEvent("click",self.mouseClick)
        for l in cells.keys():
            cell(l)

    def spacePressed(self, event):
        self.isActive = not self.isActive
        print("Space pressed", self.isActive)

    def mouseClick(self, event):
        if self.isActive == False:
            #position = (int(event.x / cellSide, 0),)
            #position = (int(cellSide * round(event.x / cellSide, 0)), int(cellSide * round(event.y / cellSide, 0)))
            x = floor(event.x / cellSide) * cellSide
            y = floor(event.y / cellSide) * cellSide
            position = (x,y)
            if x >= 0 and y >= 0:
                if x / cellSide <= cellNum - 1 and y / cellSide <= cellNum -1:
                    if cells[position] == "alive":
                        cells[position] = "dead"
                        cellsLongTerm[position] = "dead"
                        for sprite in self.getSpritesbyClass(cell):
                            if sprite.x == x and sprite.y == y:
                                sprite.visible = False
                    else:
                        cells[position] = "alive"
                        cellsLongTerm[position] = "alive"
                        for sprite in self.getSpritesbyClass(cell):
                            if sprite.x == x and sprite.y == y:
                                sprite.visible = True
    def step(self):
        if self.isActive == True: 
            for i in cells:
                cellsLongTerm[i] = cells[i]
            for sprite in self.getSpritesbyClass(cell):
                cellsNearby = 0
                for i in range(-1,2):
                    for k in range(-1,2):
                       # if (i,k) != (0,0):
                        if i * cellSide + sprite.x >= 0 and k * cellSide + sprite.y >= 0:
                            if i + sprite.x / cellSide <= cellNum - 1 and k + sprite.y / cellSide <= cellNum -1:
                                if cellsLongTerm[(sprite.x + i * cellSide, sprite.y + k * cellSide)] == "alive" or cellsLongTerm[(sprite.x + i * cellSide, sprite.y + k * cellSide)] == "old":
                                    cellsNearby += 1
                
                if cellsNearby == 3:
                    if cellsLongTerm[(sprite.x, sprite.y)] == "alive":
                        cells[(sprite.x, sprite.y)] = "old"
                    else:
                        cells[(sprite.x, sprite.y)] = "alive"
                    sprite.visible = True
                else:
                    cells[(sprite.x, sprite.y)] = "dead"
                    sprite.visible = False
            


#-----------------------------------------------------
myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()