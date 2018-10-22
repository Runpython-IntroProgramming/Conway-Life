"""
conway.py
Author: Ella Edmonds
Credit: None
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame



for m in range(10):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
    Sprite(square,(10,10+(8*m)))
    m=m+1



myapp = App()
myapp.run()