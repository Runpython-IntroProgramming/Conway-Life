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

width=myapp.width
height=myapp.height
grid=[]
x_coordinates=list(range(width,20))
y_coordinates=list(range(height,20))
for x in x_coordinates:
    for y in y_coordinates:
        grid.append(x,y)




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