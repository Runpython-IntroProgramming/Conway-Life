"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
black=Color(0x000000, 1.0)
line=LineStyle(1, black)

life1=(RectangleAsset(3,3,line,green))
life2=(RectangleAsset,(3,3,line,blue))

Sprite(life1,(30,30))
Sprite(life2,(40,40))

myapp = App()
myapp.run()