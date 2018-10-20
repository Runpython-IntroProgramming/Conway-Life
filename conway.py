"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

xsize=5
ysize=5
pixelsize=6

def emmaprint(mylist):
    for y in range(0, ysize):
        mystri=""
        for x in range (0, xsize):
            mystri+= mylist[l2.index([x,y])] +' '
        print(mystri)
    print("")

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
white=Color(0xf0f0f0, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(0, black)

life1=(RectangleAsset(pixelsize-1, pixelsize-1, tline, green))
life2=(RectangleAsset(pixelsize-1, pixelsize-1, tline, blue))
none=(RectangleAsset(pixelsize-1, pixelsize-1, tline, white))

lifelist=[]
l2=[]
n=xsize*ysize

def coor(u):
    a=u % xsize
    b=int((u-a)/xsize)
    return[a,b]

def printing(newl1):
    doe=0
    for sprite in newl1:
        if doe>=xsize*ysize:
            break
        else:
            what=newl1.index(sprite, doe)
            doe=what+1
            ucoor=coor(what)
            if sprite=="none":
                x=ucoor[0]
                y=ucoor[1]
                death(x,y)
            elif sprite=="life1":
                x=ucoor[0]
                y=ucoor[1]
                createlife(x,y)
            elif sprite=="life2":
                x=ucoor[0]
                y=ucoor[1]
                staylife(x,y)

def thegame(l1, l3, j, newl1):
    ldeath=[]
    llife=[]
    lstay=[]
    for z in l3:
        pos=l2.index(z)
        h=l1[pos]
        if h=="none":
            ldeath+=[h]
        if h=="life1":
            llife+=[h]
        if h=="life2":
            llife+=[h]
    if (len(llife)==3) and (l1[j]=="none"):
        newl1[j]="life1"
    elif ((len(llife)==2) or (len(llife)==3)) and ((l1[j]=="life1") or (l1[j]=="life2")):
        newl1[j]="life2"
    elif (len(llife)>=4) or (len(llife)<=1):
        newl1[j]="none"

def nei(r):
    mycoor=coor(r)
    rx=int(mycoor[0])
    ry=int(mycoor[1])
    if rx==0 or rx==xsize-1 or ry==0 or ry==ysize-1:
        if rx==0 and ry==0:
            d=1
        elif rx==0 and ry==ysize-1:
            d=2
        elif rx==xsize-1 and ry==ysize-1:
            d=3
        elif rx==xsize-1 and ry==0:
            d=4
        elif rx==0:
            d=5
        elif rx==xsize-1:
            d=6
        elif ry==0:
            d=7
        elif ry==ysize-1:
            d=9
    else:
        d=8
    return(d)
    
    
def createlife(xx,yy):
    Sprite(life1,(xx*pixelsize,yy*pixelsize))
def staylife(xx,yy):
    Sprite(life2,(xx*pixelsize,yy*pixelsize))
def death(xx,yy):
    Sprite(none,(xx*pixelsize,yy*pixelsize))

space=""

l2=[]
for i in range(0,n):
    k=coor(i)
    l2+=[k]
#    i="none"
#    l1=l1+[i]
lifelist=["none","none","none","none","none","life1","life1","life1","none","life1","life1","life1","life1","life1","none","none","none","none","none","none","none","none","none","none","none"]

def conway(l1):
    newl1=list.copy(l1)
    for j in range(0,len(l1)):
        w=nei(j)
        if w==1:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            five=[jx+1,jy]
            seven=[jx,jy+1]
            eight=[jx+1,jy+1]
            l3=[five]+[seven]+[eight]
            thegame(l1, l3, j, newl1)
        if w==2:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            two=[jx,jy-1]
            three=[jx+1,jy-1]
            five=[jx+1,jy]
            l3=[two]+[three]+[five]
            thegame(l1, l3, j, newl1)
        if w==3:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            one=[jx-1,jy-1]
            two=[jx,jy-1]
            four=[jx-1,jy]
            l3=[one]+[two]+[four]
            thegame(l1, l3, j, newl1)
        if w==4:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            four=[jx-1,jy]
            six=[jx-1,jy+1]
            seven=[jx,jy+1]
            l3=[four]+[six]+[seven]
            thegame(l1, l3, j, newl1)
        if w==5:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            two=[jx,jy-1]
            three=[jx+1,jy-1]
            five=[jx+1,jy]
            seven=[jx,jy+1]
            eight=[jx+1,jy+1]
            l3=[two]+[three]+[five]+[seven]+[eight]
            thegame(l1, l3, j, newl1)
        if w==6:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            one=[jx-1,jy-1]
            two=[jx,jy-1]
            four=[jx-1,jy]
            six=[jx-1,jy+1]
            seven=[jx,jy+1]
            l3=[one]+[two]+[four]+[six]+[seven]
            thegame(l1, l3, j, newl1)
        if w==7:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            four=[jx-1,jy]
            five=[jx+1,jy]
            six=[jx-1,jy+1]
            seven=[jx,jy+1]
            eight=[jx+1,jy+1]
            l3=[four]+[five]+[six]+[seven]+[eight]
            thegame(l1, l3, j, newl1)
        if w==9:
            s=coor(j)
            jx=(s[0])
            jy=(s[1])
            one=[jx-1,jy-1]
            two=[jx,jy-1]
            three=[jx+1,jy-1]
            four=[jx-1,jy]
            five=[jx+1,jy]
            l3=[one]+[two]+[three]+[four]+[five]
            thegame(l1, l3, j, newl1)
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
            l3=[one]+[two]+[three]+[four]+[five]+[six]+[seven]+[eight]
            thegame(l1, l3, j, newl1)
    printing(newl1)
    l1=list.copy(newl1)
    emmaprint(l1)
    return l1


def spaceKey(event):
    global lifelist
    lifelist = conway(lifelist)
    

myapp = App()
step=myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.run(step)