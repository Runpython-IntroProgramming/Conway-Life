"""
conway.py
Author: Glen Passow
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

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

height = 10
width = 10

for x in range(0, height):
    for y in range(0, width):
        squares[(x,y)] = cell(rectangle, (a, b))
        a = a+20
    a = 0
    b = b+20
print(squares)

for h in range(0, height):
    for w in range(0, width):
        surroudingCellsAlive = 0
        if squares[(w+1, h+1)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w+1, h)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w+1, h-1)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w, h-1)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w, h+1)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w-1, h-1)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w-1, h)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if squares[(w-1, h+1)].stateCurent == True:
            surroundingCellsAlive = surroundingCellsAlive + 1
        if surroundingCellsAlive < 2:
            squares[(w, h)].nextState = False
        if surroundingCellsAlive  == 2:
            squares[(w, h)].nextState = squares[(w, h)].stateCurrent
        if surroundingCellsAlive == 3:
            squares[(w, h)].nextState = True
        else:
            squares[(w, h)].nextState = False

myapp = App()
myapp.run()