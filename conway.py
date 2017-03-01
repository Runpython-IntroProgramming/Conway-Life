"""
conway.py
Author: Brendan
Credit: Mr. Dennison
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

#Set Up
SCREEN_WIDTH = 660
SCREEN_HEIGHT = 510
generation = False
class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        white = Color(0xffffff, 1)
# Background

        noline = LineStyle(0, black)
        
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, white)
        bg = Sprite(bg_asset, (0,0))
#Step Function
    def step(self):
        for Cell in 
myapp=Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
# Colors
black = Color(0, 1)
thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
cf = RectangleAsset(20, 30, thinline, gray)



    
celllist =list(range(1, 563))
i = 0
x = 0
y = 0
c = 0
while i != 1:
    celllist[c] = Cell((x, y), c, 0)
    if y > (SCREEN_HEIGHT - 30):
        i=1
    elif x > (SCREEN_WIDTH - 20):
        x=0
        y=y+30
    else:
        x=x+20
        c= c+1
#Cell Class
class Cell(Sprite):
    def __init__(self, position, listposition, state):
        super().__init__(cf, position)
        self.s = state
        self.l = int(listposition)
    def step(self):
        alive = 0
        if celllist[self.l-32].s in [1, 2]:
            alive += 1
        elif celllist[self.l-33].s in [1, 2]:
            alive += 1
        elif celllist[self.l-34].s in [1, 2]:
            alive += 1
        elif celllist[self.l-1].s in [1, 2]:
            alive += 1
        elif celllist[self.l+1].s in [1, 2]:
            alive += 1
        elif celllist[self.l+32].s in [1, 2]:
            alive += 1
        elif celllist[self.l+33].s in [1, 2]:
            alive += 1
        elif celllist[self.l+34].s in [1, 2]:
            alive += 1
        else:
            alive = alive
        if alive>3 or alive<2:
            self.s = 0
        else:
            self.s = self.s
celllist[30].s=1
celllist[31].s=1
celllist[].s=1
#User Input
def gen():
    generation = not generation
def spaceKey(event):
    gen()
def mouseClick(event):
    dd
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenMouseEvent('click', mouseClick)


# generations

 

        

myapp.run()