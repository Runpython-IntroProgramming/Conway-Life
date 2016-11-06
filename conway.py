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
    asset = RectangleAsset(1,1,noline,red)

    def __init__(self, position):
        super().__init__(Cell.asset, position)

    def step(self):
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
        bg_asset = RectangleAsset(width, height, thinline, white)
        bg = Sprite(bg_asset, (0,0))
        self.generation=0
        blinker = {(1, 0), (1, 1), (1, 2)}
        block   = {(5, 5), (6, 6), (5, 6), (6, 5)}
        toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
        glider  = {(10, 11), (11, 10), (10, 10), (10, 12), (12, 11)}
        self.world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
                   | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))
        
        self.listenMouseEvent(MouseEvent.mousedown, self.mousedown)
        self.listenMouseEvent(MouseEvent.mouseup, self.mouseup)
        self.listenMouseEvent(MouseEvent.mousemove, self.mousemove)
        self.dragging = False 

    def mousedown(self, event):
        # capture any mouse down within 50 pixels
        Cell((event.x,event.y))
        print('mousedown')
        self.deltax = event.x - (self.x + self.width//2) 
        self.deltay = event.y - (self.y + self.height//2)
        if abs(self.deltax) < 50 and abs(self.deltay) < 50:
            self.dragging = True
            # only drag one bunny at a time - consume the event
            event.consumed = True

    def mousemove(self, event):
        if self.dragging:
            self.x = event.x - self.deltax - self.width//2
            self.y = event.y - self.deltay - self.height//2
            event.consumed = True

    def mouseup(self, event):
        if self.dragging:
            self.dragging = False
            event.consumed = True
    
    def life(self):
        "Play Conway's game of life for N generations from initial world."
        
        #display(world, g)
        counts = Counter(n for c in self.world for n in offset(ConwayGame.neighboring_cells, c))

        self.world = {c for c in counts 
                      if counts[c] == 3 or (counts[c] == 2 and c in self.world)}
                    
    def step(self):
        self.life()
        self.generation+=1
        print('')
        print('*********************************************************')
        print('cells '+str(self.generation))
        for c in self.world:
            Cell(c)
            print(c)
            
            
        for cell in self.getSpritesbyClass(Cell):
            if cell.getPosition() not in self.world:
                cell.destroy()

myapp = ConwayGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
    
 