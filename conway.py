"""
conway.py
Author: Eric Goodney
Credit: Jack, Patrick, Teacher, http://brythonserver.github.io/ggame/#ggame.MouseEvent
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor
red = Color(0xFF4040, 1.0)
green = Color(0x00FF00, 1.0)
blue = Color(0x1C86EE, 1.0)
white = Color(0xF8F8FF, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xFF7D40, 1.0)
thinline = LineStyle(1, black)
#Making the grid. Square 400 by 400 goes up by 40
line1 = RectangleAsset(1,400, thinline, black)
line2 = RectangleAsset(400,1, thinline, black)
for x in range(11):
    Sprite(line1, (x*40, 0))
    Sprite(line2, (0, x*40))
#mouseClick event 
cell_asset = RectangleAsset(40,40,thinline, blue)
def mouseClick(event):
    x = floor(event.x/40)*40 
    y = floor(event.y/40)*40
    if x < 400 and y < 400:
        Sprite(cell_asset,(x, y))

ball_asset = ImageAsset("Conway-life.png", Frame(0,0,100,100))

ball = Sprite(ball_asset, (0,0))

ball.scale = 0.1




myapp = App()
myapp.listenMouseEvent('click', mouseClick)
myapp.run()