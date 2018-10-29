"""
conway.py
Author: Eamon
Credit: 
Assignment:conway life game
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
"""
You may use code supplied in the graphics tutorials as a starting point.
Live cells in your program may be represented as rectangles, circles, or any other shape that you would like to use. The example in the video above uses small circles.
The initial state of live cells may be preset or randomized by you, but it must be possible to start the game with a blank screen.
As the Wikipedia article described, your "playing area" may have fixed boundaries, boundaries that wrap around top and bottom, or may be entirely unbounded (in some ways, the easiest approach!).
The user must be able to "turn on" cells by clicking on them with the mouse, or by click-dragging across the window.
If your playing area is unbounded, then the up/down/right/left cursor keys should allow the user to scroll the playing area within the window.
Your live cells should be two different colors: one for its first day of “life”, the second for all subsequent days.
"""
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

o = 0
myapp = App()
go = False
#colors
invis = Color(0xffffff,1)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

width = myapp.width
height = myapp.height
#list of coords of cells

newcells = []
oldcells = []

black = Color(0, 1)
noline = LineStyle(0, black)
thinline = LineStyle(1,black)

#cells
#cell on day 1
class Cell1(Sprite):
    cll1 = RectangleAsset(20,20,noline,red)
    def __init__(self,  position):
        super().__init__(Cell1.cll1, position)

#cell after day 1 
class Cell2(Sprite):
    cll2 = RectangleAsset(20,20,noline,blue)
    def __init__(self,  position):
        super().__init__(Cell2.cll2, position)

#when there is no cell
class Cell0(Sprite):
    cll0 = RectangleAsset(20,20,noline,invis)
    def __init__(self,  position):
        super().__init__(Cell0.cll0, position)

def mousedown(event):
    global o
    o = 1
def mouseup(event):
    global o
    o = 0

def mousemove(event):
    global Cell1, o, newcells
    clickx = int((event.x//20)*20)
    clicky = int((event.y//20)*20)
    if o==1 and (clickx,clicky) not in newcells:
        Cell1((clickx,clicky))
        newcells.append((clickx, clicky))

def pauseplay(event):
    global go, oldcells
    go = not go
    if go == True:
        print("Game is started")
    else:
        print("Game is stopped")
    
    
nextto = 0

def step():
    global pauseplay, newcells, oldcells, go, nextto, height, width, checkcells, Cell1, Cell2, Cell0, time
    adjacent = []
    topop = []
    if go == True:
        for (m, n) in newcells:
            oldcells.append((m, n))
#move newcells to oldcells
        print("old: " + str(oldcells))
        newcells = []
        checkcells = []
#cells which may be next to others
        for (m, n) in oldcells:
            for x in range(m-20, m+40, 20):
                if x <=width and x >= 0:
                    for y in range(n-20, n+40, 20):
                        if y <= height and y >= 0 and (x, y) not in checkcells:
                            checkcells.append((x, y))
        print("check: " + str(checkcells))



        for (m, n) in checkcells:
            print((m,n))
            nextto = 0
            adjacent = []
            for x in range(m-20, m+40, 20):
                if x <=width and x >= 0:
                    for y in range(n-20, n+40, 20):
                        if y <= height and y >= 0 and (x,y) and(x, y) not in adjacent:
                            adjacent.append((x, y))
            adjacent.remove((m, n))

            for (a, b) in adjacent:
                if (a, b) in oldcells:
                    nextto += 1
            print("adj: " + str(adjacent))
            print("nextto: " + str(nextto))
            
            if nextto == 3 and (m, n) not in oldcells:
                print("should be" + str((m, n)))
                Cell1((m,n))
                newcells.append((m, n))
            elif (m, n) in oldcells:
                print("elif")
                if nextto == 2 or nextto == 3:
                    Cell2((m, n))
                    oldcells.append((m, n))
                else:
                    print("else")
#                    Cell0((m, n))
                    topop.append((m, n))
            else:
                print("c0 at" + str((m, n)))
                Cell0((m, n))
        for (m, n) in topop:
            oldcells.remove((m,n))
#            print("nextto: " + str(nextto))






myapp.run(step)
myapp.listenMouseEvent('mousedown',mousedown)
myapp.listenMouseEvent('mouseup',mouseup)
myapp.listenMouseEvent('mousemove',mousemove)
myapp.listenKeyEvent('keydown','space',pauseplay)


