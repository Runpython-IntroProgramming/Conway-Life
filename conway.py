"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

xsize=4
ysize=4
pixelsize=6

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
white=Color(0xf0f0f0, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(0, black)

life1=(RectangleAsset(pixelsize-1, pixelsize-1, tline, green))
life2=(RectangleAsset(pixelsize-1, pixelsize-1, tline, blue))
none=(RectangleAsset(pixelsize-1, pixelsize-1, tline, white))

l1=[]
l2=[]
n=xsize*ysize

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

def createlife(xx,yy):
    Sprite(life1,(xx*pixelsize,yy*pixelsize))
def staylife(xx,yy):
    Sprite(life2,(xx*pixelsize,yy*pixelsize))
def death(xx,yy):
    Sprite(none,(xx*pixelsize,yy*pixelsize))

l2=[]
for i in range(0,n):
    k=coor(i)
    l2+=[k]
    l1=["none","none","none","none","none","life1","life1","life1","none","none","none","none","none","none","none","none",]
#    i="none"
#    l1=l1+[i]

#while True:
for c in range(1):
    for j in range(0,len(l1)):
#        mcoor=coor(j)
        w=nei(j)
        if w==8:
            ldeath=[]
            llife=[]
            lstay=[]
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
            l3=[one]+[two]+[three]+[four]+[five]+[six]+[seven]+[eight]
            for z in l3:
                pos=l2.index(z)
                for pox in range(0, len(l1)):
                    h=l1[pox]
                    if pos==pox:
                        if h=="none":
                            ldeath+=[h]
                        if h=="life1":
                            llife+=[h]
                        if h=="life2":
                            lstay+=[h]
                if (len(ldeath)>=4) or (len(ldeath)<=1):
                    u="none"
                    l1.remove(h)
                    l1.insert(h,u)
                if (len(ldeath)==5) and (h=="none"):
                    u="life1"
                    l1.remove(h)
                    l1.insert(h,u)
                if (len(ldeath)==5) or (len(ldeath)==6) and ((h=="life1") or (h=="life2")):
                    u="life2"
                    l1.remove(h)
                    l1.insert(h,u)
            for sprite in l1:
                mcoor=coor(j)
                if sprite=="none":
                    x=mcoor[0]
                    y=mcoor[1]
                    death(x,y)
                if sprite=="life1":
                    x=mcoor[0]
                    y=mcoor[1]
                    createlife(x,y)
                if sprite=="life2":
                    x=mcoor[0]
                    y=mcoor[1]
                    staylife(x,y)


myapp = App()
myapp.run()