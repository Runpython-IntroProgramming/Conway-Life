"""
conway.py
Author: Sean Healey
Credit: Tutorial, Stack Overflow
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, CircleAsset
import random

# Colors
red = Color(0xff0000, 1.0)
orange = Color(0xffa500, 1.0)
yellow = Color(0xffff00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

# LineStyle
noline = LineStyle(0, white)

#Circles
redcircle = CircleAsset(5, noline, red)
orangecircle = CircleAsset(5, noline, orange)
yellowcircle = CircleAsset(5, noline, yellow)
greencircle = CircleAsset(5, noline, green)
bluecircle = CircleAsset(5, noline, blue)
purplecircle = CircleAsset(5, noline, purple)
blackcircle = CircleAsset(5, noline, black)
whitecircle = CircleAsset(5, noline, white)


gridwidth = 2
gridheight = 3

grid = []

for i in range(0,gridheight):
    grid.append([0] * gridwidth)
    for j in range(0,gridwidth):
        grid[i][j] = random.randint(0,1)

grid[0][1] = 7

print(grid)
        

