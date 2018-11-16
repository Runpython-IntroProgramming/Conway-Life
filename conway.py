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
thinline1 = LineStyle(1, black)
thinline = LineStyle(1, red)

#Making the grid. Square 400 by 400 goes up by 40
grid1 = RectangleAsset(1300,800, thinline1, black)
Sprite(grid1, (0,0))

grid = RectangleAsset(400,400, thinline, green)
Sprite(grid, (0,0))
line1 = RectangleAsset(1,400, thinline, red)
line2 = RectangleAsset(400,1, thinline, red)
for x in range(11):
    Sprite(line1, (x*40, 0))
    Sprite(line2, (0, x*40))
    
ball_asset = ImageAsset("Conway-life.png", Frame(62,210,275,275),3)
"""
ball = Sprite(ball_asset, (0,0))
ball.setImage(0)
ball.scale = 0.145
"""
def mouseClick(event):
    x = floor(event.x/40)*40 
    y = floor(event.y/40)*40
    ball = Sprite(ball_asset,(x, y))
    ball.setImage(0)
    ball.scale = 0.145
    if x > 375 or y > 375:
        x = floor(event.x/40)*40 
        y = floor(event.y/40)*40
        ball = Sprite(ball_asset,(x, y))
        ball.setImage(2)
        ball.scale = 0.145

myapp = App()
myapp.listenMouseEvent('click', mouseClick)
myapp.run()