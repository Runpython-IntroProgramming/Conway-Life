"""
conway.py
Author: johannes testorf
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life


def mouseclick(event):
    pixelpositionx = ((event.x)//10)*10
    pixelpositiony = ((event.y)//10)*10
    if colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]==0:
        Sprite(rsquare_asset, (pixelpositionx, pixelpositiony))
        colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=1
    else:
        Sprite(wsquare_asset, (pixelpositionx, pixelpositiony))
        colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=0


while z==0:

int is missing in neighbors definitions    
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import time
scrw= 100
scrh=100
SCREEN_WIDTH = scrw
SCREEN_HEIGHT = scrh

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)

width=list(range(0,int((scrw/10))+1))
height = list(range(0,int((scrh/10))+1))
print(width)
print(height)
click = 0

colors={"0101":"0"}
for x in width:
    for y in height:
        colors['0'+str(x)+'0'+str(y)]=0


thinline = LineStyle(1, black)
rsquare_asset =RectangleAsset(10,10, thinline, red)
wsquare_asset = RectangleAsset(10, 10, thinline, white)
for x in width:
    for y in height:
        Sprite(wsquare_asset,(x*10, y*10))

def mouseclick(event):
    global click
    click = 1
    pixelpositionx = ((event.x)//10)*10
    pixelpositiony = ((event.y)//10)*10
    if colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]==0:
        Sprite(rsquare_asset, (pixelpositionx, pixelpositiony))
        colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=1
    else:
        Sprite(wsquare_asset, (pixelpositionx, pixelpositiony))
        colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=0
        
def mouseup(event):        
    global click
    click = 0
    
def drag(event):
    global click
    if click==1:
        pixelpositionx = ((event.x)//10)*10
        pixelpositiony = ((event.y)//10)*10
        if colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]==0:
            Sprite(rsquare_asset, (pixelpositionx, pixelpositiony))
            colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=1
        else:
            Sprite(wsquare_asset, (pixelpositionx, pixelpositiony))
            colors['0'+str(round(pixelpositionx/10))+'0'+str(round(pixelpositiony/10))]=0

go=0
def spacekey(event):
    global colors
    colors1 =colors.copy()
    global go
    if go==0:
        go=1
    else:
        go=0
    global width
    global height
    
def enter(event):
    global colors
    global go
    global width
    global height
    print(go)
    while go == 1:
        for x in width:
            for y in height:
                print(x,y)
                if x==0 and y!=0 and y!=int(scrh/10):
                    neighbors = int(colors.get('0'+str(x+ 1)+'0'+str(y)))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+str(y+1)))+int(colors.get('0'+str(x)+'0'+str(y-1)))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y+1)))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y-1)))+int(colors.get('0'+str(x+1)+'0'+str(y+1)))+int(colors.get('0'+str(x+1)+'0'+str(y-1)))
                if y==0 and x!=0 and x!=int(scrw/10):
                    neighbors =int(colors.get('0'+str(x+ 1)+'0'+str(y)))+int(colors.get('0'+str(x-1)+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+str(y+1)))+int(colors.get('0'+str(x)+'0'+str(int(scrh/10))))+int(colors.get('0'+str(x-1)+'0'+str(y+1)))+int(colors.get('0'+str(x-1)+'0'+str(int(scrh/10))))+int(colors.get('0'+str(x+1)+'0'+str(y+1)))+int(colors.get('0'+str(x+1)+'0'+str(int(scrh/10))))
                if x==scrw/10 and y!=0 and y!=int(scrh/10):
                    neighbors=int(colors.get('0'+'0'+'0'+str(y)))+int(colors.get('0'+str(x-1)+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+str(y+1)))+int(colors.get('0'+str(x)+'0'+str(y-1)))+int(colors.get('0'+str(x-1)+'0'+str(y+1)))+int(colors.get('0'+str(x-1)+'0'+str(y-1)))+int(colors.get('0'+'0'+'0'+str(y+1)))+int(colors.get('0'+'0'+'0'+str(y-1)))
                if y==scrh/10 and x!=0 and x!=int(scrw/10):
                    neighbors=int(colors.get('0'+str(x+ 1)+'0'+str(y)))+int(colors.get('0'+str(x-1)+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+'0'))+int(colors.get('0'+str(x)+'0'+str(y-1)))+int(colors.get('0'+str(x-1)+'0'+'0'))+int(colors.get('0'+str(x-1)+'0'+str(y-1)))+int(colors.get('0'+str(x+1)+'0'+'0'))+int(colors.get('0'+str(x+1)+'0'+str(y-1)))
                if x==0 and y==0:
                    neighbors = int(colors.get('0'+str(x+ 1)+'0'+str(y)))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+str(y+1)))+int(colors.get('0'+str(x)+'0'+str(int(scrh/10))))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y+1)))+int(colors.get('0'+str(int(scrw/10))+'0'+str(int(scrh/10))))+int(colors.get('0'+str(x+1)+'0'+str(y+1)))+int(colors.get('0'+str(x+1)+'0'+str(int(scrh/10))))
                if x==0 and y==scrh/10:
                    neighbors = int(colors.get('0'+str(x+ 1)+'0'+str(y)))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+'0'))+int(colors.get('0'+str(x)+'0'+str(y-1)))+int(colors.get('0'+str(int(scrw/10))+'0'+'0'))+int(colors.get('0'+str(int(scrw/10))+'0'+str(y-1)))+int(colors.get('0'+str(x+1)+'0'+'0'))+int(colors.get('0'+str(x+1)+'0'+str(y-1)))
                if y==0 and x==scrw/10:
                    neighbors =int(colors.get('0'+'0'+'0'+str(y)))+int(colors.get('0'+str(x-1)+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+str(y+1)))+int(colors.get('0'+str(x)+'0'+str(int(scrh/10))))+int(colors.get('0'+str(x-1)+'0'+str(y+1)))+int(colors.get('0'+str(x-1)+'0'+str(int(scrh/10))))+int(colors.get('0'+'0'+'0'+str(y+1)))+int(colors.get('0'+'0'+'0'+str(int(scrh/10)))) 
                if y==scrh/10 and x==scrw/10:
                    neighbors=int(colors.get('0'+'0'+'0'+str(y)))+int(colors.get('0'+str(x-1)+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+'0'))+int(colors.get('0'+str(x)+'0'+str(y-1)))+int(colors.get('0'+str(x-1)+'0'+'0'))+int(colors.get('0'+str(x-1)+'0'+str(y-1)))+int(colors.get('0'+'0'+'0'+'0'))+int(colors.get('0'+'0'+'0'+str(y-1)))
                if x!=0 and y!=0 and y!=scrh/10 and x!=scrw/10:
                    neighbors=int(colors.get('0'+str(x+ 1)+'0'+str(y)))+int(colors.get('0'+str(x-1)+'0'+str(y)))+int(colors.get('0'+str(x)+'0'+str(y+1)))+int(colors.get('0'+str(x)+'0'+str(y-1)))+int(colors.get('0'+str(x-1)+'0'+str(y+1)))+int(colors.get('0'+str(x-1)+'0'+str(y-1)))+int(colors.get('0'+str(x+1)+'0'+str(y+1)))+int(colors.get('0'+str(x+1)+'0'+str(y-1)))
                if neighbors==3:
                    print(3)
                    colors1['0'+str(x)+'0'+str(y)]=1
                    Sprite(rsquare_asset,(x*10, y*10))
                if neighbors==2 and colors['0'+str(x)+'0'+str(y)]!=1:
                    print(2)
                    colors1['0'+str(x)+'0'+str(y)]=0
                    Sprite(wsquare_asset,(x*10, y*10))
                if neighbors<2:
                    print('less')
                    colors1['0'+str(x)+'0'+str(y)]=0
                    Sprite(wsquare_asset,(x*10, y*10))
                if neighbors>3:
                    print('more')
                    colors1['0'+str(x)+'0'+str(y)]=0
                    Sprite(wsquare_asset,(x*10, y*10))
        colors=colors1.copy() 



myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('mouseup', mouseup)
myapp.listenMouseEvent('mousedown', mouseclick)
myapp.listenMouseEvent('mousemove', drag)
myapp.listenKeyEvent('keydown', 'space', spacekey)
myapp.listenKeyEvent('keydown', 'enter', enter)


myapp = App()
myapp.run()