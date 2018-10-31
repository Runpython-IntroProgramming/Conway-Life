"""
conway.py
Author: Ella Edmonds
Credit: None
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
'''
class grid(Sprite):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    asset = RectangleAsset(8,8,side,grey)
    
    def __init__(self, position):
        super().__init__(grid.asset, position)
    
    grid(10,10)


class grid(App):
  
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        grid((100,100))
'''
'''
grid=[]
for m in range(10):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
    a = Sprite(square,(10,10+(8*m)))
    m=m+1
    grid.append(a)
    
moregrid=[]
for m in range(10):
    Sprite(grid(m))
'''
w = int(input("How wide would you like youre grid? "))
l = int(input("How long would you like youre grid? "))

'''grey = Color(0x000000,.3)
side = LineStyle(1,grey)
square = RectangleAsset(8,8,side,grey)
    
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
    
print(x)
print(y)

for m in range(len(x)):
    a.append(square)

d = zip(x,y)
e = zip(a,d)

for m in d:
    print(m[0],m[1])

#spritlist = []

for m in e:
   Sprite(m[0],m[1])
  #  spritlist.append(Sprite(m[0],m[1]))'''

class DeadCell(Sprite):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
    def __init__(self,position):
        super().__init__(DeadCell.square,position)

class BabyCell(Sprite):
    green = Color(0x00ff00,.8)
    side = LineStyle(1,green)
    square1 = RectangleAsset(8,8,side,green)
    
    def __init__(self,position):
        super().__init__(BabyCell.square1,position)
        
class LiveCell(Sprite):
    yellow = Color(0xffff00,.8)
    side = LineStyle(1,yellow)
    square2 = RectangleAsset(8,8,side,yellow)
    
    def __init__(self,position):
        super().__init__(LiveCell.square2,position)


class Game(App):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
        
    def __init__(self, width, height):
        super().__init__(width, height)
        
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
        
        for m in d:
            DeadCell((m[0],m[1]))
        
        #for n in range(len(d)):
         #   Cell((x,y))
        
        Game.listenKeyEvent("keydown","mouseclick",BabyCell)
        
        
        
        BabyCell((26,58))
        LiveCell((18,50))
        
    

    


#def grid()

#spritelist = {spritlist}








myapp = Game(800, 800)
myapp.run()