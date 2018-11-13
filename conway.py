"""
conway.py
Author: Jackson Tolliday
Credit: http://doc.pyschools.com/html/dictionary.html, https://gamedev.stackexchange.com/questions/11838/sprite-group-doesnt-support-indexing
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
        RULES:
    Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by overpopulation.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset

day1 = Color(0xffff00, 1.0)
day2 = Color(0xffffff, 1.0)
grey = Color(0xffffff, 1.0) 
trial = Color(0xC0C0C0, 1.0)
gridgrey = LineStyle(1, grey)
noline = LineStyle(0, grey)

class Poscell(Sprite):
    """
    Cell outline
    """
    asset = RectangleAsset(11, 11, gridgrey, trial)
    createdict = {}
    posposcells = []


    def __init__(self, position):
        super().__init__(Poscell.asset, position)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        if len(list(self.collidingWithSprites(Cell))) >= 0:
            createdict[cell.position] = Poscell
            print(createdict)


class Cell(Sprite):
    """
    Cell outline
    """
    asset = RectangleAsset(11, 11, gridgrey, day1)

    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        print(len(list(self.collidingWithSprites(Cell))))

class ConwayLife(App):
    """
    Game setup
    """
    def __init__(self):
        super().__init__()
        # Background
        bg_asset = RectangleAsset(self.width, self.height, noline, grey)
        bg = Sprite(bg_asset, (0,0))
        self.a = []
        self.celldict = {}
        self.postuplelist = []
        self.shredlist = []
        self.bornlist = []
        ConwayLife.listenMouseEvent("click", self.mouseClick)
        ConwayLife.listenKeyEvent('keydown', 'enter', self.start)
        ConwayLife.listenKeyEvent('keydown', 's', self.ps)
        adddict = {}
        deldict = {}

    def step(self):
        print(self.celldict)
        print(Poscell.createdict)
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        for sell in self.getSpritesbyClass(Poscell):
            sell.step

    def mouseClick(self, event):
        if ((((round(event.x/10))*10),((round(event.y/10))*10))) not in self.a:
            c = Cell((((round(event.x/10))*10),((round(event.y/10))*10)))
            c
            self.celldict[c.position] = c
        else:
            pass

    def start(self, event):
        for cell in self.celldict:
            if len(self.celldict[cell].collidingWithSprites(Cell)) < 2:
                self.shredlist.append(self.celldict[cell])
            if len(list(self.celldict[cell].collidingWithSprites(Cell))) > 3:
                self.shredlist.append(self.celldict[cell])
            if len(list(self.celldict[cell].collidingWithSprites(Cell))) == 3:
                Poscell.posposcells.append((cell[0]-10, cell[1]))
                Poscell.posposcells.append((cell[0]-10, cell[1]-10))
                Poscell.posposcells.append((cell[0], cell[1]-10))
                Poscell.posposcells.append((cell[0]+10, cell[1]))
                Poscell.posposcells.append((cell[0]+10, cell[1]+10))
                Poscell.posposcells.append((cell[0], cell[1]+10))
                Poscell.posposcells.append((cell[0]-10, cell[1]+10))
                Poscell.posposcells.append((cell[0]+10, cell[1]-10))
                Poscell.posposcells = sorted(Poscell.posposcells)
        print(Poscell.posposcells)
        for countcopies in Poscell.posposcells:
            if countcopies not in self.postuplelist: 
                self.postuplelist.append(countcopies) 
        print(self.postuplelist)
        for nposcellk, nposcelld in self.celldict.items():
            if nposcellk in Poscell.posposcells:
                pass
                

    def ps(self, event):
        print(self.shredlist)

ConwayLife().run()