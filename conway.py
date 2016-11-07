"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Using_defaultdict
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from collections import Counter
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, MouseEvent
myapp = App()
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
white=Color(0xffffff,1.0)
yellow=Color(0xffff00,1.0)

thinline = LineStyle(1, black)
noline=LineStyle(0,white)


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def offset(cells, delta):
        "Slide/offset all the cells by delta, a (dx, dy) vector."
        (dx, dy) = delta
        return {(x+dx, y+dy) for (x, y) in cells} 

class Cell(Sprite):
    """
    Animated space ship
    """
    newasset = RectangleAsset(1,1,noline,green)
    oldasset = RectangleAsset(1,1,noline,yellow)

    def __init__(self, position):
        super().__init__(Cell.newasset, position)
        
    def ageCell(self):
        #self.asset[0]=Cell.oldasset
        self.asset = Cell.oldasset
        print('aging')

    def step(self):
        self.ageCell()
        self.setImage(0)
        
    def getPosition(self):
        return((self.x, self.y))



class ConwayGame(App):
    """

    """
    neighboring_cells = [(-1, -1), (-1, 0), (-1, 1), 
                        ( 0, -1),          ( 0, 1), 
                        ( 1, -1), ( 1, 0), ( 1, 1)]    
    

    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, thinline, black)
        bg = Sprite(bg_asset, (0,0))
        self.generation=0
        blinker = {(1, 0), (1, 1), (1, 2)}
        block   = {(5, 5), (6, 6), (5, 6), (6, 5)}
        toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
        glider  = {(10, 11), (11, 10), (10, 10), (10, 12), (12, 11)}
      
        self.isOldCell=False
        
        self.listenMouseEvent(MouseEvent.mousedown, self.mousedown)
        self.listenMouseEvent(MouseEvent.mouseup, self.mouseup)
        self.listenMouseEvent(MouseEvent.mousemove, self.mousemove)
        self.dragging = False
        
        startWith = input('Enter B to start wth blank screen, P with predefined setup: ')
        if startWith in {'P','p'}:
            self.world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
                               | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))
        else:
           self.world={} 
                               
    def mousedown(self, event):
        self.newcell(event.x,event.y)
        event.consumed = True
        self.dragging = True

    def mousemove(self, event):
        if self.dragging:
            self.newcell(event.x,event.y)
            event.consumed = True

    def mouseup(self, event):
        if self.dragging:
            self.dragging = False
            event.consumed = True
    
    def life(self):
        counts = Counter(n for c in self.world for n in offset(ConwayGame.neighboring_cells, c))

        self.world = {c for c in counts 
                      if counts[c] == 3 or (counts[c] == 2 and c in self.world)}


    def newcell(self, vx, vy):
        if (vx,vy) not in self.world:
            Cell((vx,vy))
            self.world.add((vx,vy))

                    
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

myapp = ConwayGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
    
 