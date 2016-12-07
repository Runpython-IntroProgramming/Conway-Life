"""
conway_large.py
Author: Dan Melnikov
Credit: <list sources used, if any>
http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Using_defaultdict
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from collections import Counter
from math import floor
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, MouseEvent, Frame

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
white=Color(0xffffff,1.0)
yellow=Color(0xffff00,1.0)

thinline = LineStyle(1, black)
noline=LineStyle(0,white)


Screen_Radius=300
cell_size=3


def offset(cells, delta):
        "Slide/offset all the cells by delta, a (dx, dy) vector."
        (dx, dy) = (delta[0]*cell_size,delta[1]*cell_size)
        return {(x+dx, y+dy) for (x, y) in cells}
        
def neighborhood(central_cell):
        neighboring_cells = [(-1,-1), (0,-1), (1,-1),   
                             (-1, 0),         (1, 0),
                             (-1, 1), (0, 1), (1, 1)]
        (cx, cy) = (central_cell[0],central_cell[1])
        return {(cx+x*cell_size, cy+y*cell_size) for (x, y) in neighboring_cells}         

def toGrid(mpos):
    return ((mpos[0]-mpos[0]%cell_size),(mpos[1]-mpos[1]%cell_size))

class Cell(Sprite):
    """
    
    """
    cellsprite=CircleAsset(cell_size,thinline,white)
    cellsprite_New=CircleAsset(cell_size,thinline,green)
    cellsprite_Old=CircleAsset(cell_size,thinline,yellow)
    #asset = ImageAsset("greenandyellow.jpg", Frame(50,50,cell_size,cell_size), 1, 'horizontal')
    #asset.append("greenandyellow.jpg", Frame(60,60,cell_size,cell_size), 1, 'horizontal')

    def __init__(self, position):
        super().__init__(Cell.cellsprite, position)
        self.setImage(0)
        
    def ageCell(self):
        self.setImage(1)

    def step(self):
        self.ageCell()
        
        
    def getPosition(self):
        return((self.x, self.y))



class ConwayGame(App):
    """

    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        self.generation=0
        blinker = {(1, 0), (1, 1), (1, 2)}
        toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
        blinker = {(cell_size, 0), (cell_size, cell_size), (cell_size, 2*cell_size)}
        block   = {(5*cell_size, 5*cell_size), (5*cell_size, 6*cell_size), (6*cell_size, 5*cell_size), (6*cell_size, 6*cell_size)}
        toad    = {(0, 0), (0, cell_size), (0, 2*cell_size), (cell_size, cell_size), (cell_size, 2*cell_size), (cell_size, 3*cell_size)}
        glider  = {(10*cell_size, 10*cell_size),(10*cell_size, 11*cell_size), (10*cell_size, 12*cell_size),(11*cell_size, 10*cell_size), (12*cell_size, 11*cell_size)}
      
        self.isOldCell=False
        
        self.listenMouseEvent(MouseEvent.mousedown, self.mousedown)
        self.listenMouseEvent(MouseEvent.mouseup, self.mouseup)
        self.listenMouseEvent(MouseEvent.mousemove, self.mousemove)
        self.dragging = False
        
        startWith = input('Enter B to start wth blank screen, P with predefined setup: ')
        if startWith in ['P','p']:
            self.world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
                               | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))
        else:
           self.world={}
        

    def mousedown(self, event):
        self.newcell(toGrid((event.x,event.y)))
        event.consumed = True
        self.dragging = True

    def mousemove(self, event):
        if self.dragging:
            self.newcell(toGrid((event.x,event.y)))
            event.consumed = True

    def mouseup(self, event):
        if self.dragging:
            self.dragging = False
            event.consumed = True
    
    def life(self):
        counts = Counter(n for c in self.world for n in neighborhood(c))
        self.world = {c for c in counts 
                      if counts[c] == 3 or (counts[c] == 2 and c in self.world)}


    def newcell(self, cell_position):
        if cell_position not in self.world:
            Cell(cell_position)
            self.world.add(cell_position)

                    
    def step(self):
        self.life()
        self.generation+=1
        for c in self.world:
            self.isOldCell=False
            for cell in self.getSpritesbyClass(Cell):
                cell_p=cell.getPosition()
                cell_x=cell_p[0]
                cell_y=cell_p[1]
                if ((cell_x==c[0]) and (cell_y==c[1])):
                    self.isOldCell=True
                    cell.ageCell()
                    break
            if not self.isOldCell:
                Cell(c)

            
        for cell in self.getSpritesbyClass(Cell):
            if cell.getPosition() not in self.world:
                cell.destroy()

myapp = ConwayGame(600,600)
myapp.run()

        
        
        
        
        
