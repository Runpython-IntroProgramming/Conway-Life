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
mousex = 0
mousey = 0
createlife = 0
spritelist = 0

class Cell(Sprite):
    asset = ImageAsset("conwaysprites.png",
        Frame(0,0,10,10), 3, 'horizontal')
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.fxcenter = self.fycenter = 0
        self.col = position[0]/10
        self.row = position[1]/10
        self.setImage(2)

    def step(self): #Step needs to 1. cycle through generations, 2. detect if mouse is over then create life, 3. Change color of new life to black after first cycle
        global spritelist
        global mousex
        global mousey
        if spritelist[self.row][self.col] == 1: #if alive do the below
            if self.countneighbors() < 2 or self.countneighbors() > 3:
                spritelist[self.row][self.col] = 0

        if spritelist[self.row][self.col] == 2: #if just birthed do the below
            if self.countneighbors() < 2 or self.countneighbors() > 3:
                spritelist[self.row][self.col] = 0
            else:
                spritelist[self.row][self.col] = 1
        
        if spritelist[self.row][self.col] == 0: #if dead do the below
            if self.countneighbors() == 3:
                spritelist[self.row][self.col] = 2
        
        if createlife == True and self.mouseoverlife() == True:
            spritelist[self.row][self.col] = 2
            

    def changecolor(self):
        if spritelist[self.row][self.col] == 0:
            self.setImage(2)
        if spritelist[self.row][self.col] == 1:
            self.setImage(1)
        if spritelist[self.row][self.col] == 2:
            self.setImage(0)

    
    def mouseoverlife(self):
        global mousex
        global mousey
        if (mousex >= self.x and mousex <= self.x+10) and (mousey >= self.y and mousey <= self.y+10):
            return True
        else:
            return False
            
    def countneighbors(self):
        s = 0
        if self.col+1 <= 29 and self.row+1 <= 29 and self.col-1 >= 0 and self.row-1 >= 0: # center
            if spritelist[self.row-1][self.col-1] == 1 or spritelist[self.row-1][self.col-1] == 2: #7
                s += 1
            if spritelist[self.row-1][self.col] == 1 or spritelist[self.row-1][self.col] == 2: #8
                s += 1
            if spritelist[self.row][self.col-1] == 1 or spritelist[self.row][self.col-1] == 2: #4
                s += 1
            if spritelist[self.row-1][self.col+1] == 1 or spritelist[self.row-1][self.col+1] == 2: #9
                s += 1
            if spritelist[self.row][self.col+1] == 1 or spritelist[self.row][self.col+1] == 2: #6
                s += 1
            if spritelist[self.row+1][self.col-1] == 1 or spritelist[self.row+1][self.col-1] == 2: #1
                s += 1
            if spritelist[self.row+1][self.col] == 1 or spritelist[self.row+1][self.col] == 2: #2
                s += 1
            if spritelist[self.row+1][self.col+1] == 1 or spritelist[self.row+1][self.col+1] == 2: #3
                s += 1
        elif self.col+1 <= 29 and self.row+1 <= 29 and self.col-1 >=0 and self.row-1 < 0: #top middle
            if spritelist[self.row+1][self.col-1] == 1 or spritelist[self.row+1][self.col-1] == 2: #1
                s += 1
            if spritelist[self.row+1][self.col] == 1 or spritelist[self.row+1][self.col] == 2: #2
                s += 1
            if spritelist[self.row+1][self.col+1] == 1 or spritelist[self.row+1][self.col+1] == 2: #3
                s += 1
            if spritelist[self.row][self.col-1] == 1 or spritelist[self.row][self.col-1] == 2: #4
                s += 1
            if spritelist[self.row][self.col+1] == 1 or spritelist[self.row][self.col+1] == 2: #6
                s += 1
        elif self.col+1 <= 29 and self.row+1 <= 29 and self.col-1 < 0 and self.row-1 >= 0: #left middle
            if spritelist[self.row+1][self.col] == 1 or spritelist[self.row+1][self.col] == 2: #2
                s += 1
            if spritelist[self.row+1][self.col+1] == 1 or spritelist[self.row+1][self.col+1] == 2: #3
                s += 1
            if spritelist[self.row][self.col+1] == 1 or spritelist[self.row][self.col+1] == 2: #6
                s += 1
            if spritelist[self.row-1][self.col] == 1 or spritelist[self.row-1][self.col] == 2: #8
                s += 1
            if spritelist[self.row-1][self.col+1] == 1 or spritelist[self.row-1][self.col+1] == 2: #9
                s += 1
        elif self.col+1 <= 29 and self.row+1 > 29 and self.col-1 >= 0 and self.row-1 >= 0: #bottom middle
            if spritelist[self.row][self.col-1] == 1 or spritelist[self.row][self.col-1] == 2: #4
                s += 1
            if spritelist[self.row][self.col+1] == 1 or spritelist[self.row][self.col+1] == 2: #6
                s += 1
            if spritelist[self.row-1][self.col-1] == 1 or spritelist[self.row-1][self.col-1] == 2: #7
                s += 1
            if spritelist[self.row-1][self.col] == 1 or spritelist[self.row-1][self.col] == 2: #8
                s += 1
            if spritelist[self.row-1][self.col+1] == 1 or spritelist[self.row-1][self.col+1] == 2: #9
                s += 1
        elif self.col+1 > 29 and self.row+1 <= 29 and self.col-1 >= 0 and self.row-1 >= 0: #right middle
            if spritelist[self.row+1][self.col-1] == 1 or spritelist[self.row+1][self.col-1] == 2: #1
                s += 1
            if spritelist[self.row+1][self.col] == 1 or spritelist[self.row+1][self.col] == 2: #2
                s += 1
            if spritelist[self.row-1][self.col-1] == 1 or spritelist[self.row-1][self.col-1] == 2: #7
                s += 1
            if spritelist[self.row][self.col-1] == 1 or spritelist[self.row][self.col-1] == 2: #4
                s += 1
            if spritelist[self.row-1][self.col] == 1 or spritelist[self.row-1][self.col] == 2: #8
                s += 1
        elif self.col+1 <= 29 and self.row+1 <= 29 and self.col-1 < 0 and self.row-1 < 0: #left upper corner
            if spritelist[self.row+1][self.col] == 1 or spritelist[self.row+1][self.col] == 2: #2
                s += 1
            if spritelist[self.row+1][self.col+1] == 1 or spritelist[self.row+1][self.col+1] == 2: #3
                s += 1
            if spritelist[self.row][self.col+1] == 1 or spritelist[self.row][self.col+1] == 2: #6
                s += 1
        elif self.col+1 > 29 and self.row+1 <= 29 and self.col-1 >= 0 and self.row-1 < 0: #right upper corner
            if spritelist[self.row+1][self.col-1] == 1 or spritelist[self.row+1][self.col-1] == 2: #1
                s += 1
            if spritelist[self.row+1][self.col] == 1 or spritelist[self.row+1][self.col] == 2: #2
                s += 1
            if spritelist[self.row][self.col-1] == 1 or spritelist[self.row][self.col-1] == 2: #4
                s += 1
        elif self.col+1 > 29 and self.row+1 > 29 and self.col-1 >= 0 and self.row-1 >= 0: #right lower corner
            if spritelist[self.row-1][self.col-1] == 1 or spritelist[self.row-1][self.col-1] == 2: #7
                s += 1
            if spritelist[self.row-1][self.col] == 1 or spritelist[self.row-1][self.col] == 2: #8
                s += 1
            if spritelist[self.row][self.col-1] == 1 or spritelist[self.row][self.col-1] == 2: #4
                s += 1
        elif self.col+1 <= 29 and self.row+1 > 29 and self.col-1 < 0 and self.row-1 >= 0: #left lower corner
            if spritelist[self.row-1][self.col+1] == 1 or spritelist[self.row-1][self.col+1] == 2: #9
                s += 1
            if spritelist[self.row][self.col+1] == 1 or spritelist[self.row][self.col+1] == 2: #6
                s += 1
            if spritelist[self.row-1][self.col] == 1 or spritelist[self.row-1][self.col] == 2: #8
                s += 1
        return s



class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for y in range(0,30):
            for x in range(0,30):
                Cell((10*x,10*y))
        global spritelist
        spritelist = [[(0) for x in range(0,30)] for y in range(0,30)]

    def mousedown(self, event):
        global createlife
        createlife = True

    def mousemove(self, event):
        global mousex
        global mousey
        mousex = event.x-10
        mousey = event.y-10


    def mouseup(self, event):
        global createlife
        createlife = False
    
    def step(self):
        for g in self.getSpritesbyClass(Cell):
            g.step()
        for g in self.getSpritesbyClass(Cell):
            g.changecolor()

        
myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mousedown', myapp.mousedown)
myapp.listenMouseEvent('mouseup', myapp.mouseup)
myapp.listenMouseEvent('mousemove', myapp.mousemove)
myapp.run()