"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

xsize=10
ysize=20
pixelsize=6

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
white=Color(0xffffff, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(0, black)

life1=(RectangleAsset(pixelsize-1, pixelsize-1, tline, green))
life2=(RectangleAsset(pixelsize-1, pixelsize-1, tline, blue))
none=(RectangleAsset(pixelsize-1, pixelsize-1, tline, white))

l1=[]
n=xsize*ysize

for i in range(0,n):
    i=none
    l1=l1+[i]

def coor(u):
    a=u % xsize
    b=int((u-a)/xsize)
    return[a,b]

def nei(r):
    mycoor=coor(r)
    rx= mycoor[0]
    ry=mycoor[1]
    if rx==0 or rx==xsize-1 or ry==0 or ry==ysize-1:
        if rx==ry or (rx==0 and ry==9) or (rx==9 and ry==0):
            d=3
        else:
            d=5
    else:
        d=8

for j in range(0,len(l1)):
    nei(j)
    if d==3:
        
    if d==5:
        
    else:
        

def createlife():
    Sprite(life1,(x*pixelsize,y*pixelsize))
def staylife():
    Sprite(life2,(x*pixelsize,y*pixelsize))
def death():
    Sprite(none,(x*pixelsize,y*pixelsize))

#for x in range(0,xsize):
    #for y in range(0,ysize):
        #staylife()


#myapp = App()
#myapp.run()