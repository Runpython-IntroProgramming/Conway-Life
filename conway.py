"""
conway.py
Author: Glen Passow
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame



    def step(self):
        for Sprite in self.getSpritesbyClass(Sprite):
            Sprite.step()






class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.stateCurent = False
        self.livingNeighbors = 0
        self.nextState = False

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

thinline = LineStyle(1, black)
rectangle = RectangleAsset(20, 20, thinline, white)

a = 0
b = 0

squares = {}

height = 20
width = 20

simulationState = 1

for x in range(0, height):
    for y in range(0, width):
        squares[(x,y)] = cell(rectangle, (a, b))
        a = a+20
    a = 0
    b = b+20
while simulationState == 0:
    pass

while simulationState == 1:
    for h in range(0, height):
        for w in range(0, width):
            surroundingCellsAlive = 0
            if (w+1, h+1) in squares and squares[(w+1, h+1)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if ((w+1, h)) in squares and squares[(w+1, h)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if (w+1, h-1) in squares and squares[(w+1, h-1)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if (w, h-1) in squares and squares[(w, h-1)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if (w, h+1) in squares and squares[(w, h+1)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if (w-1, h-1) in squares and squares[(w-1, h-1)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if (w-1, h) in squares and squares[(w-1, h)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
            if (w-1, h+1) in squares and squares[(w-1, h+1)].stateCurent == True:
                surroundingCellsAlive = surroundingCellsAlive + 1
                
            if surroundingCellsAlive < 2:
                squares[(w, h)].nextState = False
            elif surroundingCellsAlive  == 2:
                squares[(w, h)].nextState = squares[(w, h)].stateCurrent
            elif surroundingCellsAlive == 3:
                squares[(w, h)].nextState = True
            else:
                squares[(w, h)].nextState = False
                
    for h in range(0, height):
        for w in range(0, width):
            squares[(w, h)].stateCurent = squares[(w, h)].nextState
    App.listenKeyEvent("keydown", "space", simulationState = 3)

myapp = App()
myapp.run()