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

grey = Color(0x000000,.3)
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

spritlist = []

for m in e:
    Sprite(m[0],m[1])
    spritlist.append(Sprite(m[0],m[1]))

class Cell(Sprite):
    red = Color(0xff0000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,red)
    def __init__(self,position):
        super.__init__(Cell.square,position)
        


class Game(App):
    def __init__(self):
        Cell((26,58))

    


#def grid()

#spritelist = {spritlist}








myapp = Game()
myapp.run()