"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset, http://stackoverflow.com/questions/10665591/how-to-remove-list-elements-in-a-for-loop-in-python
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life

"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

purple = Color(0x512DA8, 1)
nostroke = LineStyle(0, purple)
livecells = {}
makecells = []
surcells = []
restingcells = {}
killcells = {}
xdiff = 0
ydiff = 0

def create():
    for celle in makecells[:]:
        if restingcells.get((celle[0], celle[1]), False) == False:
            Cell((celle[0], celle[1]))
        else:
            restingcells[(celle[0], celle[1])] = False
            livecells[(celle[0], celle[1])] = True
        makecells.remove(celle)

def getcoor(xx, yy):
    return([[xx - 10, yy - 10], [xx - 10, yy], [xx - 10, yy + 10], [xx, yy - 10], [xx, yy + 10], [xx + 10, yy - 10], [xx + 10, yy], [xx + 10, yy + 10]])

def check():
    for celle in surcells[:]:
        if find(celle[0], celle[1]) == 3:
            makecells.append(celle)
        surcells.remove(celle)
            
def checking(xx, yy):
    dei = getcoor(xx, yy)
    for deadcell in dei:
        if livecells.get((deadcell[0], deadcell[1]), False) == False:
            if deadcell in surcells:
                at = 1
            else:
                surcells.append(deadcell)
            
def find(xx, yy):
    neighbors = getcoor(xx, yy)
    neighborcount = 0
    for posi in neighbors:
        if livecells.get((posi[0], posi[1]), False) == True:
            neighborcount += 1
    return(neighborcount)

class Cell(Sprite):
    pix = RectangleAsset(10, 10, nostroke, purple)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        self.ogposx = self.x - xdiff
        self.ogposy = self.y - ydiff
        livecells[(self.ogposx, self.ogposy)] = True
        
    def step(self):
        n = find(self.ogposx, self.ogposy)
        if n < 2 or n > 3:
            killcells[(self.ogposx, self.ogposy)] = True
        checking(self.ogposx, self.ogposy)
        if livecells.get((self.ogposx, self.ogposy)) == False:
            self.visible = False
            restingcells[(self.ogposx, self.ogposy)] = True
        if restingcells.get((self.ogposx, self.ogposy)) == False:
            self.visible = True
    
    def kill(self):
        if killcells.get((self.ogposx, self.ogposy), False) == True:
            livecells[(self.ogposx, self.ogposy)] = False
            killcells[(self.ogposx, self.ogposy)] = False
    
    def mover(self, direction):
        if direction == "r":
            self.x += 20
        elif direction == "l":
            self.x -= 20
        elif direction == "u":
            self.y -= 20
        elif direction == "d":
            self.y += 20

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        
        Cell((100, 50))
        Cell((110, 60))
        Cell((110, 70))
        Cell((100, 70))
        Cell((90, 70))
        """
        Cell((100, 50))
        Cell((110, 60))
        Cell((100, 70))
        Cell((100, 60))
        """
        self.listenKeyEvent("keydown", "right arrow", self.moveright)
        self.listenKeyEvent("keydown", "left arrow", self.moveleft)
        self.listenKeyEvent("keydown", "up arrow", self.moveup)
        self.listenKeyEvent("keydown", "down arrow", self.movedown)
        self.listenMouseEvent('click', self.create)
        
    def moveright(self, event):
        xdiff += 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("r")
    def moveleft(self, event):
        xdiff -= 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("l")
    def moveup(self, event):
        ydiff -= 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("u")
    def movedown(self, event):
        ydiff += 20
        for cell in self.getSpritesbyClass(Cell):
            cell.mover("d")
            
    def create(self, event):
        diffx = event.x % 10
        diffy = event.y % 10
        finx = event.x - diffx
        finy = event.y - diffy
        if restingcells.get((finx, finy), False) == False:
            Cell((finx, finy))
        else:
            restingcells[(finx, finy)] = False
            livecells[(finx, finy)] = True
    
    def step(self):
        create()
        for cell in self.getSpritesbyClass(Cell):
            cell.kill()
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        check()
        
        
myapp = Conway(640, 480)
myapp.run()




