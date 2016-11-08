"""
conway_large.py
Author: <your name here>
Credit: <list sources used, if any>
http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Using_defaultdict
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from collections import Counter
from math import floor
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, MouseEvent, Frame
myapp = App()
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
black = Color(0x000000, 1.0)
white=Color(0xffffff,1.0)
yellow=Color(0xffff00,1.0)

thinline = LineStyle(1, black)
noline=LineStyle(0,white)


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
cell_size=4

asset = ImageAsset("greenandyellow.jpg", Frame(0,0,100,50), 1, 'horizontal')
#asset = RectangleAsset(10,cell_size,noline,green)

Sprite(asset,(100,100))
myapp = App()
myapp.run()
