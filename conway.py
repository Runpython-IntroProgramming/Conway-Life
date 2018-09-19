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
cellNum = 10
cellSide = int(frameWidth / (cellNum * 2))
print(cellSide)
cells = {}

bg = RectangleAsset(frameWidth, frameHeight, noLine, black)
Sprite(bg, (0,0))
for i in range(0, cellNum):
    for k in range(0, cellNum):
        if randint(0, 5) >= 2:
            cells[(k * 10,i * 10)] = "alive"
        else:
            cells[(k * 10,i * 10)] = "dead"
        Sprite(RectangleAsset(cellSide, cellSide, outLine, black), (k * cellSide,i * cellSide))
cellsLongTerm = cells
#-----------------------------------------------------
class cell(Sprite):
    Cell = CircleAsset(cellSide, outLive, blue)

    def __init__(self, position):
        super().__init__(cell.Cell, position)
        self.visible = False

    def nearbyCells(self):
        cellsNearby = 0
        for i in range(-1,2):
            for k in range(-1,2):
                if (i,k) != (0,0):
                    if cellsLongTerm[(self.x + 10 * i,self.y + 10 * k)] == "alive":
                        cellsNearby += 1
        if cellsNearby < 2 or cellsNearby > 3:
            cells[(self.x, self.y)] = "dead"
            return False
        else:
            cells[(self.x, self.y)] = "alive"
            return True
        
        
        
class tempCell(Sprite):
    Cell = CircleAsset(5, outLive, blue)

    def __init__(self, position):
        super().__init__(tempCell.Cell, position)
        
   
#-----------------------------------------------------
class GameOfLife(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        GameOfLife.listenKeyEvent("keydown", "space",self.spacePressed)
        self.isActive = False
        print(self.isActive)
        GameOfLife.listenMouseEvent("click",self.mouseClick)
        for l in cells.keys():
            cell(l)
    def spacePressed(self, event):
        self.isActive = not self.isActive
        print("Space pressed", self.isActive)

    def mouseClick(self, event):
        if self.isActive == False:
            position = (int(10 * round(event.x / 10, 0)), int(10 * round(event.y / 10, 0)))
            cells[position] = "alive"
        '''
        for sprite in self.getSpritesbyClass(cell):
                sprite.visible = sprite.nearbyCells()
                print(sprite.nearbyCells())
'''

    def step(self):

        if self.isActive == True:   
            for sprite in self.getSpritesbyClass(cell):
                cellsNearby = 0
                for i in range(-1,2):
                    for k in range(-1,2):
                        if (i,k) != (0,0):
                            if sprite.x + i * 10 >= 0 and sprite.y + k * 10 >= 0 and sprite.x/10 + i <= cellNumb and sprite.y/10 + k <= cellNumb:
                                if cellsLongTerm[(sprite.x + 10 * i,sprite.y + 10 * k)] == "alive":
                                    cellsNearby = 1
                                    print('yoy')
                print("ayo")
                if randint(1,2) == 1:
                    cells[(sprite.x, sprite.y)] = "dead"
                    sprite.visible = False
                else:
                    cells[(sprite.x, sprite.y)] = "alive"
                    sprite.visible = True
            

#-----------------------------------------------------
myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()