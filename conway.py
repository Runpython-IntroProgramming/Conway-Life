"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
white=Color(0xffffff, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(0, black)

life1=(RectangleAsset(6, 6, tline, green))
life2=(RectangleAsset(6, 6, tline, blue))
none=(RectangleAsset(6, 6, tline, white))

l1=[]
n=2500

for i in range(0,n):
    i=none
    l1=l1+[i]


def createlife():
    Sprite(life1,(x,y))
    return
def staylife():
    Sprite(life2,(x,y))
    return
def death():
    Sprite(none,(x,y))

for x in range(0,300,6):
    for y in range(0,300,6):
        death()


myapp = App()
myapp.run()