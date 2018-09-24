"""
conway.py
Author: Emma Tysinger
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import Color, Sound, SoundAsset

myapp = App()

# Background
#black = Color(0, 1)
#noline = LineStyle(0, black)
#bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
#bg = Sprite(bg_asset, (0,0))

#making list of grid coordinates
width=myapp.width
height=myapp.height
grid=[1,2,3]
x_coordinates=list(range(0,width,20))
y_coordinates=list(range(0,height,20))
for x in x_coordinates:
    for y in y_coordinates:
        grid.append((x,y))

#colors for game#
black=Color(0,1)
pink= Color(0xee1289,1)
green=Color(0x66cdaa4,1)
nocolor=Color(0,0)
line=LineStyle(1,black)
noline=LineStyle(1,nocolor)

class NewCell(Sprite):
    asset=RectangleAsset(7,7,line,green)
    def __init__(self,position):
        super().__init__(NewCell.asset,position)

class DeadCell(Sprite):
    asset=RectangleAsset(7,7,noline,nocolor)
    def __init__(self,position):
        super().__init__(DeadCell.asset,position)

for i in grid:
    x,y=i
    new=list(x,y)
    print (new)


Rectangle=RectangleAsset(30,40,line,green)
Sprite(Rectangle)
myapp.run()




#class ConwayGame(App):
    #def __init__(self):
        #super().__init__()
        #x=self.width
        #y=self.height
        #x_coordinates=list(range(x,20))
        #y_coordinates=list(range(y,20))
        #black = Color(0,1)
        #nocolor = Color(0,0)
        #thinline=LineStyle(2,black)
        #grid_asset=RectangleAsset(20,20,thinline,nocolor)
        #grid=[Sprite(grid_asset, (x,x)) for x in x_coordinates]
        #print(x_coordinates)
        
        

#myapp = ConwayGame()
#myapp.run()