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

def find(post):
    neighborcount = 0
    for posi in neighbors:
        if livecells.get(posi, False) == True:
            neighborcount += 1
    return(neighborcount)

class Cell(Sprite):
    pix = RectangleAsset(20, 20, nostroke, grey)
    
    def __init__(self, position):
        super().__init__(Cell.pix, position)
        livecells[position] = True
        self.position = position
        
    def step(self):
        print(self.position)
        self.destroy()
        """
        neighbors = [str((self.y - 20, self.x - 20)), str((self.y - 20, self.x)), str((self.y - 20, self.x + 20)), str((self.y, self.x - 20)), str((self.y, self.x + 20)), str((self.y + 20, self.x - 20)), str((self.y + 20, self.x)), str((self.y + 20, self.x + 20))]
        ne = find(neighbors)
        print(ne)
        self.destroy()
        
        if neighborcount < 2:
            self.destroy()
            print("Im Dead")
        elif neighborcount >= 2 and neighborcount <= 3:
            print("Im Living")
        elif neighborcount > 3:
            self.destroy()
        """
class Conway(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        Cell((0, 0))
        Cell((20, 20))
        
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
    
    

myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()






