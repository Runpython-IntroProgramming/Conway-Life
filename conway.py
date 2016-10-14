"""
conway.py
Author: johannes testorf
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life



"""
from ggame import App, PolygonAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)

width=list(range(0,64))
height = list(range(0,48))

thinline = LineStyle(1, black)

for x in width:
    for y in height:
        rectangle = PolygonAsset(((x*10, y*10), ((x+1)*10, y*10),((x+1)*10, (y+1)*10),((x)*10, (y+1)*10)), thinline, white)
        Sprite(rectangle)

def mouseclick(event):
    pixelpositionx = ((event.x)//10)*10
    pixelpositiony = ((event.y)//10)*10
    if rectangle == PolygonAsset(((pixelpositionx*10, pixelpositiony*10), ((pixelpositionx+1)*10, pixelpositiony*10),((pixelpositionx+1)*10, (pixelpositiony+1)*10),((pixelpositionx)*10, (pixelpositiony+1)*10)), thinline, white):
        rectangle = PolygonAsset(((pixelpositionx*10, pixelpositiony*10), ((pixelpositionx+1)*10, pixelpositiony*10),((pixelpositionx+1)*10, (pixelpositiony+1)*10),((pixelpositionx)*10, (pixelpositiony+1)*10)), thinline, red)
        Sprite(rectangle)
def spacekey(event):
 print(poop)

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', mouseclick)
myapp.listenKeyEvent('keydown', 'space', spacekey)

myapp = App()
myapp.run()