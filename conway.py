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
        livecells[self.position] = True
        
    def step(self):
        n = find(self.x, self.y)
        if n < 2 or n > 3:
            killcells[self.position] = True
        checking(self.x, self.y)
        if livecells.get(self.position) == False:
            self.visible = False
            restingcells[self.position] = True
        if restingcells.get(self.position) == False:
            self.visible = True
    
    def kill(self):
        if killcells.get(self.position, False) == True:
            livecells[self.position] = False
            killcells[self.position] = False
    
    def mover(self):
        self.x += 10

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        """Cell((100, 50))
        Cell((110, 60))
        Cell((110, 70))
        Cell((100, 70))
        Cell((90, 70))"""
        Cell((100, 50))
        Cell((110, 60))
        Cell((100, 70))
        Cell((100, 60))
        self.listenKeyEvent("keydown", "right arrow", self.moveright)
    
    def moveright(self, event):
        xdiff += 10
        for cell in self.getSpritesbyClass(Cell):
            cell.mover()
    
    def step(self):
        create()
        for cell in self.getSpritesbyClass(Cell):
            cell.kill()
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        check()
        
        
myapp = Conway(640, 480)
myapp.run()




