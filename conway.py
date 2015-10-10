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

def getcoor(xx, yy):
    return([[yy - 10, xx - 10], [yy - 10, xx], [yy - 10, xx + 10], [yy, xx - 10], [yy, xx + 10], [yy + 10, xx - 10], [yy + 10, xx], [yy + 10, xx + 10]])

def check(posti):
    if livecells.get(str((posti[1], posti[0])), False) == False:
        neig = getcoor(posti[1], posti[0])
        neighborcoun = 0
        for posi in neig:
            if livecells.get(str((posi[1], posi[0])), False) == True:
                neighborcoun += 1
        if neighborcoun == 3:
            Cell((posti[1], posti[0]))
    return(True)
    
def find(xx, yy):
    neighbors = getcoor(xx, yy)
    neighborcount = 0
    for posi in neighbors:
        if livecells.get(str((posi[1], posi[0])), False) == True:
            neighborcount += 1
        else:
            check(posi)
    return(neighborcount)

class Cell(Sprite):
    pix = RectangleAsset(10, 10, nostroke, grey)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        livecells[str(position)] = True
        self.position = position
        
    def step(self):
        n = find(self.x, self.y)
        if n < 2:
            livecells[str(self.position)] = False
            self.destroy()
            print("Im Dead")
        elif n >= 2 and n <= 3:
            print("Im Living")
        elif n > 3:
            livecells[str(self.position)] = False
            self.destroy()
            print("Im Dead")

class Conway(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Cell((10, 0))
        Cell((0, 10))
        Cell((0, 20))
        Cell((10, 30))
        Cell((20, 10))
        Cell((20, 20))
        Cell((30, 10))
        
        
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
    
    

myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()







