"""
conway.py
Author: Glen Passow
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

thinline = LineStyle(1, black)
rectangle = RectangleAsset(20, 20, thinline, blue)

a = 0
b = 0

for x in range(0, 24):
    for x in range(0, 32):
        Sprite(rectangle, (a, b))
        a = a+1
    a = 0
    b = b+1
    
myapp = App()
myapp.run()