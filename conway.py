"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
"""
You may use code supplied in the graphics tutorials as a starting point.
Live cells in your program may be represented as rectangles, circles, or any other shape that you would like to use. The example in the video above uses small circles.
The initial state of live cells may be preset or randomized by you, but it must be possible to start the game with a blank screen.
As the Wikipedia article described, your "playing area" may have fixed boundaries, boundaries that wrap around top and bottom, or may be entirely unbounded (in some ways, the easiest approach!).
The user must be able to "turn on" cells by clicking on them with the mouse, or by click-dragging across the window.
If your playing area is unbounded, then the up/down/right/left cursor keys should allow the user to scroll the playing area within the window.
Your live cells should be two different colors: one for its first day of “life”, the second for all subsequent days.
"""
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset


red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
#colors

black = Color(0, 1)
noline = LineStyle(0, black)






thinline = LineStyle(1, black)
#lines
rectangle = RectangleAsset(50, 20, thinline, blue)
Sprite(rectangle)

width = 500
height = 500





#class cell(object):
#    def __init__(self,10,10)
myapp = App(width,height)
myapp.run()


def leftKey(event):
    width = width
    

