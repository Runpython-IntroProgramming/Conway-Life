"""
conway.py
Author: Dimitri
Credit: Morgan
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

black = Color(0, 1)
white = Color(0xffffff, 1)
noline = LineStyle(0, white)
livecells = []

def neighborlist(x1, y1):
    return([[x1-10, y1-10], [x1-10, y1], [x1-10, y1+10], [x1, y1-10], [x1, y1+10], [x1+10, y1-10], [x1+10, y1], [x1+10, y1+10]])

def getneighbors(x1, y1):
    neighbors = neighborlist(x1, y1)
    counted = 0
    for cells in neighbors:
        if livecells.get((cells[0], cells[1]) = False) == True:
            counted += 1
        else:
            counted += 0
    return(counted)


class Cell(Sprite):
    asset = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.locx = x
        self.locy = y
        livecells = [(self.locx, self.locy)] = True




class Conways(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #self.stopped = true
        Cell((100, 100))
        Cell((90, 100))
        Cell((110, 100))

    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.kill()
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
        check()



myapp = Conways(640, 480)
myapp.run()
