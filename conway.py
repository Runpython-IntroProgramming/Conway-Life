"""
conway.py
Author: Mary Feyrer
Credit: Tess Snyder
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, 
from ggame import LineStyle, Color, Sprite, Sound

white = Color(0xffffff, 1.0)
blue = Color(0x000000, 1.0)
black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
noline = LineStyle(.00001, black)

for x in range(0,50):
    square = RectangleAsset(2, 2, noline, black) 
    for y in range(0,50):
        Sprite(rectangle, (x,y))
    

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)

myapp.run()
