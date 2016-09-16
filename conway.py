"""
conway.py
Author: Peter Bynum
Credit: <list sources used, if any>
Assignment: Conway's Game of life
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

class Conway(app):
    black = Color(0, 1)
    green = Color(0x408000, 1.0)
    white = Color(0xffffff, 1.0)
    line = LineStyle(2, black)
    bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
    bg = Sprite(bg_asset, (0,0))


myapp = Conway(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()