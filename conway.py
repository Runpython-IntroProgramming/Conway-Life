"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>http://doc.pyschools.com/html/dictionary.html, https://gamedev.stackexchange.com/questions/11838/sprite-group-doesnt-support-indexing
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

class PosCell(Sprite):
    """
    Cell outline
    """
    asset = RectangleAsset(11, 11, gridgrey, trial)
    createdict = {}


    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        if len(list(self.collidingWithSprites(Cell))) >= 0:
            createdict[cell.position] = PosCell
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
        self.shredlist = []
        self.bornlist = []
        ConwayLife.listenMouseEvent("click", self.mouseClick)
        ConwayLife.listenKeyEvent('keydown', 'enter', self.start)
        ConwayLife.listenKeyEvent('keydown', 's', self.ps)

    def step(self):
        print(self.celldict)
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        for sell in self.getSpritesbyClass(PosCell):
            sell.step

    def mouseClick(self, event):
        if ((((round(event.x/10))*10),((round(event.y/10))*10))) not in self.a:
            c = Cell((((round(event.x/10))*10),((round(event.y/10))*10)))
            c
            self.celldict[c.position] = Cell
        else:
            pass

    def start(self, event):
        for cell in self.celldict:
            if len(list(self.celldict[cell].collidingWithSprites(Cell))) < 2:
                self.shredlist.append(self.celldict[cell])
            if len(list(self.celldict[cell].collidingWithSprites(Cell))) > 3:
                self.shredlist.append(self.celldict[cell])
            if len(list(self.celldict[cell].collidingWithSprites(Cell))) == 3:
                PosCell((cell.x-10, cell.y))
                PosCell((cell.x-10, cell.y-10))
                PosCell((cell.x, cell.y-10))
                PosCell((cell.x+10, cell.y))
                PosCell((cell.x+10, cell.y+10))
                PosCell((cell.x, cell.y+10))
                PosCell((cell.x-10, cell.y+10))
                PosCell((cell.x+10, cell.y-10))
                #for poscell in len(list(PosCell.collidingWithSprites(Cell))):
                for nposcell in keys(self.celldict):
                    if nposcell in PosCell.createdict:
                        PosCell
                        
                
                
                #now program for alive!
                #so what i want to do is look at all of the possible sprite places 

    def ps(self, event):
        print(self.shredlist)

ConwayLife().run()