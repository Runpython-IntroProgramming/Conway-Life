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
print("Edges are neighbors.")
print("Press 'n' every time you wish to move on a generation")
print("P.S.") 
print("with a 10x10 this progrma takes 1.72 seconds per generation")
print("with a 15x15 this progrma takes 6.38 seconds per generation")
print("I would recomend making your no larger for times sake")

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
        if cells[position] == "baby":
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
    
    sprites[(2,2)] = DeadCell
    cells[(2,2)] = "dead"
    
    i=0
    while i <= l:
        sprites[(2,(i*8)+10)] = DeadCell
        cells[(2,(i*8)+10)] = "dead"
        #print((2,(i*8)+10))
        #DeadCell((2,(i*8)+10))
        i+=1
        
    i=0
    while i <= l:
        sprites[((10+(8*w)),((i*8)+10))] = DeadCell
        cells[((10+(8*w)),((i*8)+10))] = "dead"
        #print(((10+(8*w)),((i*8)+10)))
        #DeadCell(((10+(8*w)),((i*8)+10)))
        i+=1
        
    i=0
    while i <= l:
        sprites[((10+(8*i)),(2))] = DeadCell
        cells[((10+(8*i)),(2))] = "dead"
        #print(((10+(8*i)),(2)))
        #DeadCell(((10+(8*i)),(2)))
        i+=1
        
    i=0
    while i <= l:
        sprites[((10+(8*i)),((l*8)+18))] = DeadCell
        cells[((10+(8*i)),((l*8)+18))] = "dead"
        #print(((10+(8*i)),((l*8)+10)))
        #DeadCell(((10+(8*i)),((l*8)+10)))
        i+=1
    
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
        #madecellslist.append((sprites.get((m[0],m[1])),((m[0],m[1]))))
        madecells.append(sprites.get((m[0],m[1]))((m[0],m[1])))
        Cells.append((m[0],m[1]))
    
    def baby(self,event):
        click = []
        #print(int(event.x),int(event.y))
        click.append((event.x,event.y))
        Babys = []
        for m in self.Cells:
            if m[0] <= event.x <= m[0]+8:
                if m[1] <= event.y <= m[1]+8:
                    cells[(m[0],m[1])] = "baby"
                    sprites[(m[0],m[1])] = BabyCell
                    self.madecells.append(sprites.get((m[0],m[1]))((m[0],m[1])))
                else:
                    cells[(m[0],m[1])] = "dead"
            else:
                cells[(m[0],m[1])] = "dead"

    def clear(self,event):
        
        left1 = {}
        right2 = {}
        below3 = {}
        above4 = {}
        dal5 = {}
        dar6 = {}
        dbl7 = {}
        dbr8 = {}
        zip1234578 = []
        
        for m in self.madecells:
            m.destroy()
            
        self.madecells = []
        
        for m in self.Cells:
            #print((m[0],m[1]))
            l = 'n'
            r = 'n'
            b = 'n'
            a = 'n'
            dal = 'n'
            dar = 'n'
            dbl = 'n'
            dbr = 'n'
            if sprites.get((m[0]-8,m[1])) != DeadCell:
                    #print("there is a cell to the left")
                    left1[(m[0],m[1])]="yes"
                    l = 'y'
            if sprites.get((m[0]+8,m[1])) != DeadCell:
                    #print("there is a cell to the right")
                    right2[(m[0],m[1])]="yes"
                    r = 'y'
            if sprites.get((m[0],m[1]+8)) != DeadCell:
                    #print("there is a cell below")
                    below3[(m[0],m[1])]="yes"
                    b = 'y'
            if sprites.get((m[0],m[1]-8)) != DeadCell:
                    #print("there is a cell above")
                    above4[(m[0],m[1])]="yes"
                    a = 'y'
            if sprites.get((m[0]-8,m[1]-8)) != DeadCell:
                    #print("there is a cell dal")
                    dal5[(m[0],m[1])]="yes"
                    dal = 'y'
            if sprites.get((m[0]+8,m[1]-8)) != DeadCell:
                    #print("there is a cell dar")
                    dar6[(m[0],m[1])]="yes"
                    dar = 'y'
            if sprites.get((m[0]-8,m[1]+8)) != DeadCell:
                    #print("there is a cell dbl")
                    dbl7[(m[0],m[1])]="yes"
                    dbl = 'y'
            if sprites.get((m[0]+8,m[1]+8)) != DeadCell:
                    #print("there is a cell dbr")
                    dbr8[(m[0],m[1])]="yes"
                    dbr = 'y'
            #print()
            zip1234578.append(((m[0],m[1]),l,r,b,a,dal,dar,dbl,dbr))

        for m in zip1234578:
            neighbors = {}
            for n in zip1234578:
                z=0
                if n[1]=="y":
                    z+=1
                if n[2]=="y":
                    z+=1
                if n[3]=="y":
                    z+=1
                if n[4]=="y":
                    z+=1
                if n[5]=="y":
                    z+=1
                if n[6]=="y":
                    z+=1
                if n[7]=="y":
                    z+=1
                if n[8]=="y":
                    z+=1
                neighbors[(n[0])] = z
        
        for m in zip1234578:
            if sprites.get((m[0])) != DeadCell:
                if neighbors.get((m[0])) < 2:
                    sprites[(m[0])] = DeadCell
                    cells[(m[0])] = "dead"
                    self.madecells.append(sprites.get(m[0])(m[0]))
                    
                elif neighbors.get((m[0])) > 3:
                    sprites[(m[0])] = DeadCell
                    cells[(m[0])] = "dead"
                    self.madecells.append(sprites.get(m[0])(m[0]))
                    
                else:
                    sprites[(m[0])] = LiveCell
                    cells[(m[0])] = "old"
                    self.madecells.append(sprites.get(m[0])(m[0]))
                    
            elif sprites.get((m[0])) == DeadCell:
                if neighbors.get((m[0])) == 3:
                    sprites[(m[0])] = BabyCell
                    cells[(m[0])] = "baby"
                    self.madecells.append(sprites.get(m[0])(m[0]))
                else:
                    sprites[(m[0],m[1])] = DeadCell
                    cells[(m[0],m[1])] = "dead"
                    self.madecells.append(sprites.get(m[0])(m[0]))
                    
            else:
                print("well this print statement is never suposed to pop so somethings wrong")
                    
        #for m in zip1234578: 
         #   self.madecells.append(sprites.get(m[0])(m[0]))
                    
            #self.madecells.append(sprites.get(m[0])(m[0]))
            #sprites.get(m[0])(m[0])
        #print(neighbors)
        #print(sprites)
        

myapp = Game(500,500)
myapp.run()