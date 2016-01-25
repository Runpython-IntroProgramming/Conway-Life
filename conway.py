"""

Author: Dimitri
Credit: Morgan
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
""""""
conway.py
Author: Dimitri
Credit: Morgan
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

black = Color(0, 1)
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
                print("found")
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
        self.posx = x
        self.posy = y
        livecells[(self.ogposx, self.ogposy)] = True

    def step(self):
        if livecells.get((self.ogposx, self.ogposy)) == True:
            neighbors = getneighbors(self.posx, self.posy)
            if neighbor < 2 or neighbor > 3:
                self.visible = False
                mortalcells.append([self.x, self.y])
                print("dead")
            elif [self.x, self.y] in mortalcells:
                mortalcells.remove([self.x, self.y])
        else:
            self.visible = False

class Conways(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #self.stopped = True
        Cell((100, 100))
        Cell((100, 90))
        Cell((100, 80))


    def step(self):
        print(livecells, "b", deadcells, "b", addcells, "b", surcells, "b", mortalcells)
        kill()
        countir = 0
        for cell in self.getSpritesbyClass(Cell):
            countir += 1
            cell.step()
            print("hi")
        getneighborssur()
        createcells()
        print(countir)


myapp = Conways(640, 480)
myapp.run()
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent
black = Color(0x000000, 1)
nostroke = LineStyle(0, black)
alivecells = {}
makecells = []
surcells = []
killcells = {}
xdiff = 0
ydiff = 0
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
        if alivecells.get((deadcell[0], deadcell[1]), False) == False:
            if deadcell in surcells:
                at = 1
            else:
                surcells.append(deadcell)
            
def find(xx, yy):
    neighbors = getcoor(xx, yy)
    neighborcount = 0
    for posi in neighbors:
        if alivecells.get((posi[0], posi[1]), False) == True:
            neighborcount += 1
    return(neighborcount)
class Cell(Sprite):
    pix = RectangleAsset(10, 10, nostroke, black)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        self.ogposx = self.x
        self.ogposy = self.y
        alivecells[(self.ogposx, self.ogposy)] = True
        self.x += xdiff
        self.y += ydiff
        self.day = 0
        self.changed = False
        
    def step(self):
        if alivecells.get((self.ogposx, self.ogposy)) == True:
            self.day += 1
            if self.day > 1 and self.changed == False:
                self.color = colortwo
                self.changed = True
            n = find(self.ogposx, self.ogposy)
            if n < 2 or n > 3:
                killcells[(self.ogposx, self.ogposy)] = True
            checking(self.ogposx, self.ogposy)
        else:
            self.visible = False
    
    def kill(self):
        if killcells.get((self.ogposx, self.ogposy), False) == True:
            alivecells[(self.ogposx, self.ogposy)] = False
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
            
    def checktokill(self, px, py):
        if px == self.ogposx and py == self.ogposy:
            self.visible = False
            killcells[(self.ogposx, self.ogposy)] = True
            self.kill()
class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.stopped = True
        Cell((100, 50))
        Cell((110, 60))
        Cell((110, 70))
        Cell((100, 70))
        Cell((90, 70))
        self.listenKeyEvent("keydown", "right arrow", self.moveright)
        self.listenKeyEvent("keydown", "left arrow", self.moveleft)
        self.listenKeyEvent("keydown", "up arrow", self.moveup)
        self.listenKeyEvent("keydown", "down arrow", self.movedown)
        self.listenKeyEvent("keydown", "space", self.toggle)
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
    def toggle(self, event):
        if self.stopped == True:
            self.stopped = False
        else:
            self.stopped = True
            
    def create(self, event):
        diffx = event.x % 10
        diffy = event.y % 10
        finx = event.x - diffx - 10 - xdiff
        finy = event.y - diffy - 10 - ydiff
        if alivecells.get((finx, finy), False) == True:
            for cell in self.getSpritesbyClass(Cell):
                cell.checktokill(finx, finy)
        else:
            Cell((finx, finy))
    
    def step(self):
        if self.stopped == False:
            create()
            for cell in self.getSpritesbyClass(Cell):
                cell.kill()
            for cell in self.getSpritesbyClass(Cell):
                cell.step()
            check()
        
        
myapp = Conway(640, 480)
myapp.run()
"""
from ggame import App, Color, Sprite, RectangleAsset, LineStyle, MouseEvent

black = Color(0, 1)
white = Color(0xffffff, 1)
noline = LineStyle(0, white)
livecells = []
deadcells = []
addcells = []
surcells = []
mortalcells = []

def neighborlist(x1, y1):
    return([[x1-10, y1-10], [x1-10, y1], [x1-10, y1+10], [x1, y1-10], [x1, y1+10], [x1+10, y1-10], [x1+10, y1], [x1+10, y1+10]])

def getneighborssur():
    for pos in surcells:
        if newneighbors(pos[0], pos[1]) == 3:
            print("new")
            addcells.append(pos)
            surcells.remove(pos)

def newneighbors(x1, y1):
    neighbors = neighborlist(x1, y1)
    counted = 0
    for outsidecells in neighbors:
        if [outsidecells[0], outsidecells[1]] in livecells:
            counted += 1
    return(counted)

def getneighbors(x1, y1):
    neighbors = neighborlist(x1, y1)
    counted = 0
    for outsidecells in neighbors:
        if [outsidecells[0], outsidecells[1]] in livecells:
            counted += 1
        else:
            surcells.append(outsidecells)
    return(counted)

def createcells():
    for newcells in addcells:
        #print(newcells[0], newcells[1])
        Cell((newcells[0], newcells[1]))
        addcells.remove(newcells)

def revive():
    for nextcells in surcells:
        #print(getneighborssur(nextcells[0], nextcells[1]))
        if getneighborssur(nextcells[0], nextcells[1]) == 3:
            addcells.append(nextcells)
        surcells.remove(nextcells)

def kill():
    for thecell in mortalcells:
        deadcells.append(thecell)
        livecells.remove(thecell)
        mortalcells.remove(thecell)
    

class Cell(Sprite):
    asset = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        livecells.append([self.x, self.y])
        generation = 0

    def step(self):
        if [self.x, self.y] in livecells:
            neighbor = getneighbors(self.x, self.y)
            print(neighbor)
            if neighbor < 2 or neighbor > 3:
                self.visible = False
                mortalcells.append([self.x, self.y])
                print("dead")
            elif [self.x, self.y] in mortalcells:
                mortalcells.remove([self.x, self.y])
        else:
            if neighbors == 3 and [self.x, self.y] in deadcells:
                self.visible = True
                deadcells.pop(deadcells.index([self.x, self.y]))
                livecells.append([self.x, self.y])

class Conways(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #self.stopped = True
        Cell((100, 100))
        Cell((100, 90))
        Cell((100, 80))


    def step(self):
        print(livecells, "b", deadcells, "b", addcells, "b", surcells, "b", mortalcells)
        kill()
        countir = 0
        for cell in self.getSpritesbyClass(Cell):
            countir += 1
            cell.step()
            print("hi")
        getneighborssur()
        createcells()
        print(countir)


myapp = Conways(640, 480)
myapp.run()