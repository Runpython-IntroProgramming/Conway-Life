"""
conway.py
Author: Ella Edmonds
Credit: None
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

#print("Press the space bar to pause or play simulation.")
#print("When the simulation is paused, click to remove or add cells.")
print("Green Cells are babies and yellow cells are older")
print("A cell will survive if it has 2-3 neighbors, and a dead cell will create life if it has 3 neighbors.")

w = int(input("How wide would you like youre grid? "))
l = int(input("How long would you like youre grid? "))

cells = {}
sprites = {}


class DeadCell(Sprite):
    grey = Color(0x000000,.3)
    grey1 = Color(0x000000,.1)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey1)
    def __init__(self,position):
        super().__init__(DeadCell.square,position)
        if cells[position] == "dead":
            self.visible = True
        else:
            self.visible = False
        #print(cells)
        #print(position)

class BabyCell(Sprite):
    green = Color(0x00ff00,.8)
    side = LineStyle(1,green)
    square1 = RectangleAsset(8,8,side,green)
    
    def __init__(self,position):
        super().__init__(BabyCell.square1,position)
        if cells[(position)] == "baby":
            self.visible = True
        else:
            self.visible = False

class LiveCell(Sprite):
    yellow = Color(0xffff00,.8)
    side = LineStyle(1,yellow)
    square2 = RectangleAsset(8,8,side,yellow)
    
    def __init__(self,position):
        super().__init__(LiveCell.square2,position)
        if cells[(position)] == "old":
            self.visible = True
        else:
            self.visible = False


class Game(App):
  
    def __init__(self, width, height):
        super().__init__(width, height)
        Game.listenMouseEvent("click",self.baby)
        Game.listenKeyEvent("keydown","n",self.clear)
        madecells = []

    a = []
    x = []
    y = []
    
    b=[]
    
    for m in range(w):
        x.append(10+(8*m))
        y.append(10)
        b.append(10+(8*m))

    for m in b:
        for n in range(l):
            x.append(m)
            y.append(18+(n*8))
    
    d = zip(x,y)
    Cells = []
    Sprites = []
    madecells = []
    madecellslist = []
    
    for m in d:
        cells[(m[0],m[1])] = "dead"
        sprites[(m[0],m[1])] = DeadCell
        madecellslist.append((sprites.get((m[0],m[1])),((m[0],m[1]))))
        madecells.append(sprites.get((m[0],m[1]))((m[0],m[1])))
        Cells.append((m[0],m[1]))
    
    def baby(self,event):
        click = []
        print(int(event.x),int(event.y))
        click.append((event.x,event.y))
        Babys = []
        for m in self.Cells:
            if m[0] <= event.x <= m[0]+8:
                if m[1] <= event.y <= m[1]+8:
                    cells[(m[0],m[1])] = "baby"
                    sprites[(m[0],m[1])] = BabyCell
                    BabyCell((m[0],m[1]))
            else:
                cells[(m[0],m[1])] = "nothing"

    def clear(self,event):
        b=0
        for n in self.madecells:
            n.destroy()
        self.madecells = []
        longtermcells = []
        for m in self.Cells:
            self.madecells.append(sprites.get((m[0],m[1]))((m[0],m[1])))
            sprites.get((m[0],m[1]))((m[0],m[1]))
        for n in self.madecells:
            B = self.madecellslist[b]
            if B[0] == "baby":
                sprites[B[1]] = "old"
            b+=0
        print(sprites)
        
            

        



myapp = Game(500,500)
myapp.run()