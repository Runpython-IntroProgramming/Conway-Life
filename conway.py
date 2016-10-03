"""
conway.py
Author: Peter Bynum
Credit: <list sources used, if any>
Assignment: Conway's Game of life
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1201
SCREEN_HEIGHT = 801
black = Color(0, 1)
green = Color(0x408000, 1.0)
white = Color(0xffffff, 1.0)
border = LineStyle(2, black)
line = LineStyle(1, black)

class Cell(Sprite):
    asset = ImageAsset("conwaysprites.png",
        Frame(0,0,10,10), 3, 'horizontal')
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.fxcenter = self.fycenter = 0
        self.row = position[1]/10
        self.col = position[0]/10
        self.setImage(3)

    def step(self): #Step needs to 1. cycle through generations, 2. detect if mouse is over then create life, 3. Change color of new life to black after first cycle
        if spritelist[self.col][self.row][0] == 1: #if alive do the below
            if Cell.countneighbors < 2 or Cell.countneighbors > 3:
                spritelist[self.col][self.row][0] = 0
            
        if spritelist[self.col][self.row][0] == 0: #if dead do the below
            if Cell.countneighbors == 3:
                spritelist[self.col][self.row][0] = 2
            
        if spritelist[self.col][self.row][0] == 2: #if just birthed do the below
            if Cell.countneighbors < 2 or Cell.countneighbors > 3:
                spritelist[self.col][self.row][0] = 0
            else:
                spritelist[self.col][self.row][0] = 1
        
        if Conway.createlife == True:
            spritelist[self.col][self.row][0] = 2
    
    def changecolor(self):
        if spritelist[self.col][self.row][0] == 0:
            self.setImage(2)
        if spritelist[self.col][self.row][0] == 1:
            self.setImage(1)
        if spritelist[self.col][self.row][0] == 2:
            self.setImage(0)
    
    def createlife(self):
        if (mousex >= self.x and mousex <= self.x+10) and (mousey >= self.y and mousey <= self.y):
            return True
            
    def countneighbors(self):
        s = 0
        if self.col+1 <= 79 and self.row+1 <= 59 and self.col-1 >= 0 and self.row-1 >= 0: # center
            if spritelist[self.col-1][self.row-1][0] == 1 or spritelist[self.col-1][self.row-1][0] == 2: #7
                s += 1
            if spritelist[self.col-1][self.row][0] == 1 or spritelist[self.col-1][self.row][0] == 2: #4
                s += 1
            if spritelist[self.col][self.row-1][0] == 1 or spritelist[self.col][self.row-1][0] == 2: #8
                s += 1
            if spritelist[self.col-1][self.row+1][0] == 1 or spritelist[self.col-1][self.row+1][0] == 2: #1
                s += 1
            if spritelist[self.col][self.row+1][0] == 1 or spritelist[self.col][self.row+1][0] == 2: #2
                s += 1
            if spritelist[self.col+1][self.row-1][0] == 1 or spritelist[self.col+1][self.row-1][0] == 2: #9
                s += 1
            if spritelist[self.col+1][self.row][0] == 1 or spritelist[self.col+1][self.row][0] == 2: #6
                s += 1
            if spritelist[self.col+1][self.row+1][0] == 1 or spritelist[self.col+1][self.row+1][0] == 2: #3
                s += 1
        elif self.col+1 <= 79 and self.row+1 <= 59 and self.col-1 >=0 and self.row-1 < 0: #top middle
            if spritelist[self.col-1][self.row+1][0] == 1 or spritelist[self.col-1][self.row+1][0] == 2: #1
                s += 1
            if spritelist[self.col][self.row+1][0] == 1 or spritelist[self.col][self.row+1][0] == 2: #2
                s += 1
            if spritelist[self.col+1][self.row+1][0] == 1 or spritelist[self.col+1][self.row+1][0] == 2: #3
                s += 1
            if spritelist[self.col-1][self.row][0] == 1 or spritelist[self.col-1][self.row][0] == 2: #4
                s += 1
            if spritelist[self.col+1][self.row][0] == 1 or spritelist[self.col+1][self.row][0] == 2: #6
                s += 1
        elif self.col+1 <= 79 and self.row+1 <= 59 and self.col-1 < 0 and self.row-1 >= 0: #left middle
            if spritelist[self.col][self.row+1][0] == 1 or spritelist[self.col][self.row+1][0] == 2: #2
                s += 1
            if spritelist[self.col+1][self.row+1][0] == 1 or spritelist[self.col+1][self.row+1][0] == 2: #3
                s += 1
            if spritelist[self.col+1][self.row][0] == 1 or spritelist[self.col+1][self.row][0] == 2: #6
                s += 1
            if spritelist[self.col][self.row-1][0] == 1 or spritelist[self.col][self.row-1][0] == 2: #8
                s += 1
            if spritelist[self.col+1][self.row-1][0] == 1 or spritelist[self.col+1][self.row-1][0] == 2: #9
                s += 1
        elif self.col+1 <= 79 and self.row+1 > 59 and self.col-1 >= 0 and self.row-1 >= 0: #bottom middle
            if spritelist[self.col-1][self.row][0] == 1 or spritelist[self.col-1][self.row][0] == 2: #4
                s += 1
            if spritelist[self.col+1][self.row][0] == 1 or spritelist[self.col+1][self.row][0] == 2: #6
                s += 1
            if spritelist[self.col-1][self.row-1][0] == 1 or spritelist[self.col-1][self.row-1][0] == 2: #7
                s += 1
            if spritelist[self.col][self.row-1][0] == 1 or spritelist[self.col][self.row-1][0] == 2: #8
                s += 1
            if spritelist[self.col+1][self.row-1][0] == 1 or spritelist[self.col+1][self.row-1][0] == 2: #9
                s += 1
        elif self.col+1 > 79 and self.row+1 <= 59 and self.col-1 >= 0 and self.row-1 >= 0: #right middle
            if spritelist[self.col-1][self.row+1][0] == 1 or spritelist[self.col-1][self.row+1][0] == 2: #1
                s += 1
            if spritelist[self.col][self.row+1][0] == 1 or spritelist[self.col][self.row+1][0] == 2: #2
                s += 1
            if spritelist[self.col-1][self.row][0] == 1 or spritelist[self.col-1][self.row][0] == 2: #4
                s += 1
            if spritelist[self.col-1][self.row-1][0] == 1 or spritelist[self.col-1][self.row-1][0] == 2: #7
                s += 1
            if spritelist[self.col][self.row-1][0] == 1 or spritelist[self.col][self.row-1][0] == 2: #8
                s += 1
        elif self.col+1 <= 79 and self.row+1 <= 59 and self.col-1 < 0 and self.row-1 < 0: #left upper corner
            if spritelist[self.col][self.row+1][0] == 1 or spritelist[self.col][self.row+1][0] == 2: #2
                s += 1
            if spritelist[self.col+1][self.row+1][0] == 1 or spritelist[self.col+1][self.row+1][0] == 2: #3
                s += 1
            if spritelist[self.col+1][self.row][0] == 1 or spritelist[self.col+1][self.row][0] == 2: #6
                s += 1
        elif self.col+1 > 79 and self.row+1 <= 59 and self.col-1 >= 0 and self.row-1 < 0: #right upper corner
            if spritelist[self.col-1][self.row+1][0] == 1 or spritelist[self.col-1][self.row+1][0] == 2: #1
                s += 1
            if spritelist[self.col][self.row+1][0] == 1 or spritelist[self.col][self.row+1][0] == 2: #2
                s += 1
            if spritelist[self.col-1][self.row][0] == 1 or spritelist[self.col-1][self.row][0] == 2: #4
                s += 1
        elif self.col+1 > 79 and self.row+1 > 59 and self.col-1 >= 0 and self.row-1 >= 0: #right lower corner
            if spritelist[self.col-1][self.row-1][0] == 1 or spritelist[self.col-1][self.row-1][0] == 2: #7
                s += 1
            if spritelist[self.col-1][self.row][0] == 1 or spritelist[self.col-1][self.row][0] == 2: #4
                s += 1
            if spritelist[self.col][self.row-1][0] == 1 or spritelist[self.col][self.row-1][0] == 2: #8
                s += 1
        elif self.col+1 <= 79 and self.row+1 > 59 and self.col-1 < 0 and self.row-1 >= 0: #left lower corner
            if spritelist[self.col+1][self.row-1][0] == 1 or spritelist[self.col+1][self.row-1][0] == 2: #9
                s += 1
            if spritelist[self.col+1][self.row][0] == 1 or spritelist[self.col+1][self.row][0] == 2: #6
                s += 1
            if spritelist[self.col][self.row-1][0] == 1 or spritelist[self.col][self.row-1][0] == 2: #8
                s += 1
        return s



class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(0,80):
            for y in range(0,60):
                Cell((10*x,10*y))
        spritelist = [[(0,x,y) for x in range(0,80)] for y in range(0,60)]

    def mousedown(self, event):
        createlife = True

    def mousemove(self, event):
        mousex = event.x
        mousey = event.y

    def mouseup(self, event):
        createlife = False
    
    def step(self):
        for Cell in self.getSpritebyClass(Cell):
            Cell.step()
        for Cell in self.getSpritebyClass(Cell):
            Cell.changecolor


myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mousedown', myapp.mousedown)
myapp.listenMouseEvent('mouseup', myapp.mouseup)
myapp.listenMouseEvent('mousemove', myapp.mousemove)
myapp.run()