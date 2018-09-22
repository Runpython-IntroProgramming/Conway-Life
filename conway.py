"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

xsize=50
ysize=50
pixelsize=6

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
white=Color(0xffffff, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(0, black)

life1=(RectangleAsset(pixelsize, pixelsize, tline, green))
life2=(RectangleAsset(pixelsize, pixelsize, tline, blue))
none=(RectangleAsset(pixelsize, pixelsize, tline, white))

l1=[]
n=xsize*ysize

for i in range(0,n):
    i=none
    l1=l1+[i]


def createlife():
    Sprite(life1,(x*pixelsize,y*pixelsize))
    return
def staylife():
    Sprite(life2,(x*pixelsize,y*pixelsize))
    return
def death():
    Sprite(none,(x*pixelsize,y*pixelsize))

for x in range(0,xsize):
    for y in range(0,ysize):
        death()


myapp = App()
myapp.run()