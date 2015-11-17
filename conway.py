"""
conway.py
Author: Dimitri
Credit: Wikipedia
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELLWIDTH = 64
CELLHEIGHT = 48

black = Color(0, 1)
green = Color(0x00ff00, 1)
white = Color(0xffffff, 1)

class Conways(App):
    def _init__(self, width, height):
        super().__init__(width, height).fill(black)











myapp = Conways(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()