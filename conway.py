"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset

day1 = Color(0xffffff, 1.0)
day2 = Color(0x000000, 1.0)
grey = Color(0xC0C0C0, 1.0)
gridgrey = LineStyle(1, grey)
noline = LineStyle(0, grey)