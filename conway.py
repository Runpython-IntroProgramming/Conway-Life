"""
conway.py
Author: Morgan Meliment
Credit: http://brythonserver.github.io/ggame/#ggame.EllipseAsset
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life

"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

grey = Color(0x808080, 1)
nostroke = LineStyle(0, grey)
livecells = {}
makecells = []
surcells = []
killcells = {}

def create():
    for celle in makecells[:]:
        Cell((celle[0], celle[1]))
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
    pix = RectangleAsset(10, 10, nostroke, grey)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        livecells[self.position] = True
        
    def step(self):
        n = find(self.x, self.y)
        print(n)
        if n < 2 or n > 3:
            killcells[self.position] = True
        checking(self.x, self.y)
    
    def kill(self):
        if killcells.get(self.position, False) == True:
            livecells[self.position] = False
            killcells[self.position] = False
            self.destroy()

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Cell((10, 0))
        Cell((10, 10))
        Cell((10, 20))

        
    def step(self):
        create()
        for cell in self.getSpritesbyClass(Cell):
            cell.kill()
        print(livecells)
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        
        check()
        
    

myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()




