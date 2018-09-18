"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(1, black)

life1=(RectangleAsset(3, 3, tline, green))
life2=(RectangleAsset(3, 3, tline, blue))

#infinity=float'inf'

#x=range(0,401,3)
#y=range(0,401,3)
#x=list(x)
#y=list(y)
x=30
y=50

def createlife():
    Sprite(life1,(x,y))
    return
def staylife():
    Sprite(life2,(x,y))
    return
#def death():
    

staylife()

#in a period it has to assess all the pixels and do something for each pixel in the grid
#for x in range (0,400,3):
    #Sprite(life1,(x,400))
#Sprite(life2,(400, 400))


myapp = App()
myapp.run()