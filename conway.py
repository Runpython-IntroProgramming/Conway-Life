"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
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

new_cell=CircleAsset(1,thinline,red)
old_cell=CircleAsset(1,thinline,green)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Cell(Sprite):
    """
    Animated space ship
    """
    asset = CircleAsset(1,noline,red)

    def __init__(self, position):
        super().__init__(Cell.asset, position)

    def step(self):
        self.setImage(0)



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
        block   = {(0, 0), (1, 1), (0, 1), (1, 0)}
        toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
        glider  = {(0, 1), (1, 0), (0, 0), (0, 2), (2, 1)}
        self.world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
                   | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))
       

    def offset(cells, delta):
        "Slide/offset all the cells by delta, a (dx, dy) vector."
        (dx, dy) = delta
        return {(x+dx, y+dy) for (x, y) in cells}    
    
    def life(self):
        "Play Conway's game of life for N generations from initial world."
        for g in range(N+1):
            #display(world, g)
            counts = Counter(n for c in world for n in self.offset(Cell.neighboring_cells, c))
            self.world = {c for c in counts 
                    if counts[c] == 3 or (counts[c] == 2 and c in world)}
                    
    def step(self):
        self.generation+=1
        for c in world:
            Cell(c)
            
        #for cell in self.getSpritesbyClass(Cell):
        #    cell.step()

myapp = ConwayGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run() 

 
def display(world, g):
    "Display the world as a grid of characters."
    print ('          GENERATION {}:'.format(g))
    Xs, Ys = zip(*world)
    Xrange = range(min(Xs), max(Xs)+1)
    for y in range(min(Ys), max(Ys)+1):
        print (''.join('#' if (x, y) in world else '.'
                      for x in Xrange))

def display_w(world):                     
    for c in world:
        Sprite(new_cell,c)
    myapp.run()
    
 