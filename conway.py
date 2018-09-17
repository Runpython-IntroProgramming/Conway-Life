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
cellsLongTerm = cells

bg = RectangleAsset(frameWidth, frameHeight, noLine, black)
Sprite(bg, (0,0))
for i in range(0, 10):
    for k in range(0, 10):
        if randint(0,5) >= 2:
            cells[(k * 10,i * 10)] = "alive"
        else:
            cells[(k * 10,i * 10)] = "dead"
        Sprite(RectangleAsset(10, 10, outLine, black), (k * 10,i * 10))
cellsLongTerm = cells
#-----------------------------------------------------
class cell(Sprite):
    Cell = CircleAsset(5, outLive, blue)

    def __init__(self, position, state):
        super().__init__(cell.Cell, position)
        if cells[self.x, self.y] == "dead":
            self.visible = False
        else:
            self.visible = True

   
#-----------------------------------------------------
class GameOfLife(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        GameOfLife.listenKeyEvent("keydown", "space",self.spacePressed)
        self.isActive = False
        print(self.isActive)
        ConwayGame.listenMouseEvent("click",self.----)
        for l in cells.keys():
            cell(l,cells[l])
    def spacePressed(self, event):
        self.isActive = not self.isActive
        print("Space pressed", self.isActive)

    def mouseClick(self, event):
        


    def step(self):
        if self.isActive == True:
            
            for sprite in self.getSpritesbyClass(cell):
                print("running")
                cellsNearby = 0
                for i in range(-1,2):
                    for k in range(-1,2):
                        if (i,k) != (0,0):
                            if cells[(sprite.x + i * 10,sprite.y + k * 10)] == "alive":
                                cellsNearby += 1
                print("k")
                if cellsNearby < 2:
                    cells[sprite.x, sprite.y] = "dead"
                elif cellsNearby > 3:
                    cells[sprite.x, sprite,y] = "dead"
                else:
                    cells[sprite.x, sprite,y] = "alive"
                    sprite.visible = True
                    Sprite(sprite, (sprite.x, sprite.y))
                Sprite(CircleAsset(5,outLine, red), (sprite.x, sprite.y))
            print("ran")

#-----------------------------------------------------
myapp = GameOfLife(frameWidth, frameHeight)
myapp.run()