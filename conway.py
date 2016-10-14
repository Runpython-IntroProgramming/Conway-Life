"""
conway.py
Author: johannes testorf
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life


while z==0:
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)

width=list(range(0,64))
height = list(range(0,48))

thinline = LineStyle(1, black)
rsquare_asset =RectangleAsset(10,10, thinline, red)
wsquare_asset = RectangleAsset(10, 10, thinline, white)
for x in width:
    for y in height:
        
        Sprite(rectangle,(x*10, y*10))

def mouseclick(event):
    pixelpositionx = ((event.x)//10)*10
    pixelpositiony = ((event.y)//10)*10
    if rectangle == wsquareasset:
        rectangle = PolygonAsset(((pixelpositionx*10, pixelpositiony*10), ((pixelpositionx+1)*10, pixelpositiony*10),((pixelpositionx+1)*10, (pixelpositiony+1)*10),((pixelpositionx)*10, (pixelpositiony+1)*10)), thinline, red)
        Sprite(rectangle)
def spacekey(event):
    if z==0:
        z=1
    else:
        z=0


    
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', mouseclick)
myapp.listenKeyEvent('keydown', 'space', spacekey)

myapp = App()
myapp.run()