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
cellNum = 4
#cellSide = int(frameWidth / (cellNum * 2))
cellSide = 30
cells = {}

#-----------------------------------------------------
class cell(Sprite):
    Cell = CircleAsset(cellSide / 2, outLive, blue)

    def __init__(self, position):
        super().__init__(cell.Cell, position)
        self.visible = False
        if cells[(position)] == "alive":
            self.visible = True
        else:
            self.visible = False
'''
    def nearbyCells(self):
        cellsNearby = 0
        for i in range(-1,2):
            for k in range(-1,2):
                if (i,k) != (0,0):
                    if cellsLongTerm[(self.x + cellSide * i,self.y + cellSide * k)] == "alive":
                        cellsNearby += 1
        if cellsNearby < 2 or cellsNearby > 3:
            cells[(self.x, self.y)] = "dead"
            return False
        else:
            cells[(self.x, self.y)] = "alive"
            return True
        
'''      
   
#-----------------------------------------------------
class GameOfLife(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        GameOfLife.listenKeyEvent("keydown", "space",self.spacePressed)
        self.isActive = False
        print(self.isActive)
        bg = RectangleAsset(frameWidth, frameHeight, noLine, black)
        Sprite(bg, (0,0))
        for i in range(0, cellNum):
            for k in range(0, cellNum):
                cells[(k * cellSide,i * cellSide)] = "alive"
                Sprite(RectangleAsset(cellSide, cellSide, outLine, black), (k * cellSide,i * cellSide))
        cellsLongTerm = cells
        GameOfLife.listenMouseEvent("click",self.mouseClick)
        for l in cells.keys():
            cell(l)

    def spacePressed(self, event):
        self.isActive = not self.isActive
        print("Space pressed", self.isActive)

    def mouseClick(self, event):
        if self.isActive == False:
            position = (int(10 * round(event.x / cellSide, 0)), int(10 * round(event.y / cellSide, 0)))
            cells[position] = "alive"
        


    def step(self):

        if self.isActive == True:   
            for sprite in self.getSpritesbyClass(cell):
                cellsNearby = 0
                for i in range(-1,2):
                    for k in range(-1,2):
                        if (i,k) != (0,0):
                            if i * cellSide + sprite.x >= 0 and k * cellSide + sprite.y >= 0:
                                if i <= cellNum - 1 and k <= cellNum -1:
                                    if cells[(i,k)] == "alive":
                                        cellsNearby += 1
                print(cellsNearby)

            

#-----------------------------------------------------
myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()