"""
conway.py
Author: Noah Pikielny
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
'''
Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[1]).
Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
Any live cell with two or three live neighbours lives, unchanged, to the next generation.
Any dead cell with exactly three live neighbours will come to life.
'''

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
cellNum = 50
#cellSide = int(frameWidth / (cellNum * 2))
cellSide = 5
cells = {}
cellsLongTerm = {}
oldCells = {}
#-----------------------------------------------------
class cell(Sprite):
    Cell = CircleAsset(cellSide / 2, outLive, blue)
    def __init__(self, position):
        super().__init__(cell.Cell, position)
        if cells[(position)] == "alive":
            self.visible = True
        else:
            self.visible = False
class old(Sprite):
    Old = CircleAsset(cellSide / 2, outLive, red)
    def __init__(self, position):
        super().__init__(old.Old, position)
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
                Sprite(RectangleAsset(cellSide, cellSide, outLine, black), (k * cellSide,i * cellSide))
                #cells[(k * cellSide,i * cellSide)] = "dead"
                
                if randint(0,4) == 1:
                    cells[(k * cellSide,i * cellSide)] = "alive"
                else:
                    cells[(k * cellSide,i * cellSide)] = "dead"
                
        
        
        for i in cells:
            cellsLongTerm[i] = cells[i]
        GameOfLife.listenMouseEvent("click",self.mouseClick)
        for l in cells.keys():
            cell(l)
            oldCells[l] = old(l)
            oldCells[l].visible = False

    def spacePressed(self, event):
        self.isActive = not self.isActive
        print("Space pressed", self.isActive)

    def mouseClick(self, event):
        if self.isActive == False:
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
                        oldCells[position].visible = False
                                
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
                        if (i,k) != (0,0):
                            if i * cellSide + sprite.x >= 0 and k * cellSide + sprite.y >= 0:
                                if i + sprite.x / cellSide <= cellNum - 1 and k + sprite.y / cellSide <= cellNum -1:
                                    if cellsLongTerm[(sprite.x + i * cellSide, sprite.y + k * cellSide)] == "alive":
                                        cellsNearby += 1
                                    
                """
                if cellsNearby == 3 or cellsNearby == 2:
                    if cellsLongTerm[(sprite.x, sprite.y)] == "alive":
                        sprite.visible = False
                        oldCells[(sprite.x, sprite.y)].visible = True
                    else:
                        sprite.visible = True
                    cells[(sprite.x, sprite.y)] = "alive"

                else:
                    cells[(sprite.x, sprite.y)] = "dead"
                    sprite.visible = False
                    oldCells[(sprite.x, sprite.y)].visible = False
                """
                if cellsLongTerm[sprite.x, sprite.y] == "alive":
                    if cellsNearby == 3 or cellsNearby == 2:
                        cells[(sprite.x, sprite.y)] = "alive"
                        if cellsLongTerm[(sprite.x, sprite.y)] == "alive":
                            sprite.visible = False
                            oldCells[(sprite.x, sprite.y)].visible = True
                        else:
                            sprite.visible = True
                    else:
                        cells[(sprite.x, sprite.y)] = "dead"
                        sprite.visible = False
                        oldCells[(sprite.x, sprite.y)].visible = False
                else:
                    if cellsNearby == 3:
                        sprite.visible = True
                        cells[(sprite.x, sprite.y)] = "alive"
#-----------------------------------------------------
myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()