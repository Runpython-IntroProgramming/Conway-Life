"""
conway.py
Author: Dimitri
Credit: Morgan
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

black = Color(0x000000, 1)
white = Color(0xffffff, 1)
noline = LineStyle(0, white)
livecells = {}
addcells = []
surcells = []
deadcells = {}

def neighborlist(x1, y1):
    return([[x1-10, y1-10], [x1-10, y1], [x1-10, y1+10], [x1, y1-10], [x1, y1+10], [x1+10, y1-10], [x1+10, y1], [x1+10, y1+10]])

def surroundcells(x1, y1):
    celllist = neighborlist(x1, y1)
    for deadcell in celllist:
        if livecells.get((deadcell[0], deadcell[1]), False) == False:
            if deadcell in surcells:
                at = 1
            else:
                surcells.append(deadcell)

def getneighbors(x1, y1):
    neighbors = neighborlist(x1, y1)
    counted = 0
    for outsidecells in neighbors:
        if livecells.get((outsidecells[0], outsidecells[1]), False) == True:
            counted += 1
    return(counted)

def createcells():
    for newcells in addcells[:]:
        Cell((newcells[0], newcells[1]))
        addcells.remove(newcells)

def revive():
    for nextcells in surcells[:]:
        if getneighbors(nextcells[0], nextcells[1]) == 3:
            addcells.append(nextcells)
        surcells.remove(nextcells)

class Cell(Sprite):
    asset = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.posx = self.x
        self.posy = self.y
        livecells[(self.posx, self.posy)] = True

    def step(self):
        if livecells.get((self.ogposx, self.ogposy)) == True:
            neighbors = getneighbors(self.posx, self.posy)
            if neighbors < 2 or neighbor > 3:
                deadcells[(self.posx, self.posy)] = True
            surroundcells(self.posx, self.posy)
        else:
            self.visible = False
            
    def kill(self):
        if deadcells.get((self.posx, self.posy), False) == True:
            livecells[(self.posx, self.posy)] = False
            deadcells[(self.posx, self.posy)] = False

class Conways(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Cell((100, 50))
        Cell((110, 60))
        Cell((110, 70))
        Cell((100, 70))
        Cell((90, 70))

    def step(self):
        createcells()
        for cell in self.getSpritesbyClass(Cell):
            cell.kill()
            print("hi")
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        revive()

myapp = Conways(640, 480)
myapp.run()