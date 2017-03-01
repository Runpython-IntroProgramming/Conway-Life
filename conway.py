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
        if generation == True:
            for x in celllist:
                x.checked = 0
            for x in alivelist:
                x.step()
            for x in celllist:
                x.update()
myapp=Conway(SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
black = Color(0, 1)
thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
cf = RectangleAsset(20, 30, thinline, gray)

#Cell Class
class Cell(Sprite):
    #self, url, frame=None, qty=1, direction='horizontal', margin=0)
    asset = ImageAsset("Animationonway1.png", Frame(50, 10, 20, 30), 3, 'vertical')
    def __init__(self, position, listposition, state, step):
        super().__init__(Cell.asset, position)
        self.p = position
        self.s = state
        self.l = int(listposition)
        self.checked = step
        self.gen = 0
    def step(self):
        surround = [celllist[self.l-33], celllist[self.l-32], celllist[self.l-34], celllist[self.l+32], celllist[self.l+33], celllist[self.l+34], celllist[self.l-1], celllist[self.l+1]]
        if self.checked == 0:
            alive = 0
            self.checked = 1
            if celllist[self.l-32].s in [1,2]:
                alive += 1
            if celllist[self.l-33].s in [1,2]:
                alive += 1
            if celllist[self.l-34].s in [1,2]:
                alive += 1
            if celllist[self.l-1].s in [1,2]:
                alive += 1
            if celllist[self.l+1].s in [1,2]:
                alive += 1
            if celllist[self.l+32].s in [1,2]:
                alive += 1
            if celllist[self.l+33].s in [1,2]:
                alive += 1
            if celllist[self.l+34].s in [1,2]:
                alive += 1
            if self.s !=0:
                for x in surround:
                    x.step()
            if alive == 2:
                if self.s == 0:
                    self.gen = 0
                else:
                    self.gen = 2
            elif alive == 3:
                if self.s == 0:
                    self.gen = 1
                    alivelist.append(celllist[self.l])
                else:
                    self.gen = 2
            else:
                if celllist[self.l] in alivelist:
                    alivelist.remove(celllist[self.l])
                self.gen = 0       
    def update(self):
        if self.gen == 1:
            self.s = 1
            self.setImage(1)
        elif self.gen == 0:
            self.s = 0
            self.setImage(0)
        else:
            self.s = 2
            self.setImage(2)
    
celllist =list(range(1, 563))
i = 0
x = 0
y = 0
c = 0
while i != 1:
    celllist[c] = Cell((x, y), c, 0, 0)
    if y > (SCREEN_HEIGHT - 30):
        i=1
    elif x > (SCREEN_WIDTH - 20):
        x=0
        y=y+30
    else:
        x=x+20
        c= c+1
alivelist=[]
#User Input
generation = False
def gen():
    global generation
    generation = not generation
def spaceKey(event):
    gen()
    print("0th step")
def mouseClick(event):
    for x in celllist:
        if (x.x + 20)> event.x > (x.x) and (x.y)<event.y<(x.y+30):
            alivelist.append(x)
            x.s = 1
            x.setImage(1)
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenMouseEvent('click', mouseClick)
# generations


        

myapp.run()