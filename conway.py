"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

xsize=3
ysize=3
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
    l1=l2
    print(l2)
    l1=l1+[i]

def coor(u):
    a=u % xsize
    b=int((u-a)/xsize)
    return[a,b]

def nei(r):
    mycoor=coor(r)
    rx=int(mycoor[0])
    ry=int(mycoor[1])
    if rx==0 or rx==xsize-1 or ry==0 or ry==ysize-1:
        if rx==ry or (rx==0 and ry==xsize-1) or (rx==xsize-1 and ry==0):
            d=3
        else:
            d=5
    else:
        d=8
    return(d)

l3=[]
for e in l2:
    l3 += [e]
print(l3)

for j in range(0,len(l1)):
    w=nei(j)
    if w==8:
        s=coor(j)
        jx=(s[0])
        jy=(s[1])
        one=[jx-1,jy-1]
        two=[jx,jy-1]
        three=[jx+1,jy-1]
        four=[jx-1,jy]
        five=[jx+1,jy]
        six=[jx-1,jy+1]
        seven=[jx,jy+1]
        eight=[jx+1,jy+1]
    

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