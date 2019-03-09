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

circles = [whitecircle, redcircle, orangecircle, yellowcircle, greencircle, bluecircle, purplecircle, blackcircle]

# Get dimensions from user
gridcolumns = 3
gridrows = 3
grid = []

# Create grid
# Grid[row][column]
for i in range(0,gridrows):
    grid.append([0] * gridcolumns)
    for j in range(0,gridcolumns):
        grid[i][j] = random.randint(0,1)
        if grid[i][j] == 1:
            grid[i][j] = random.randint(1,7)

# Create Sprites for each element in grid
# Make this into it's own function
x = 0
y = 0
for i in grid:
    for j in i:
        Sprite(circles[j%8], (x,y))
        x += 10
    x = 0
    y += 10

print(grid)

# Create tick function
# Use for loops to look through entirety of grid
# Need to use i & j as numbers
# Need to make old grid and new grid
# Need to include conditional statemens incase i < 0 or j < 0
newgrid = grid
for i in range(0, len(grid)): # rows
    for j in range(0, len(grid[0])): # columns
        neighbors = 0
        if i != 0 & j != 0:
            neighbors += (grid[i-1][j-1] != 0)
        if i != 0:
            neighbors += (grid[i-1][j] != 0)
        if i != 0 & j != len(grid[0]):
            neighbors += (grid[i-1][j+1] != 0)
        if j != 0:
            neighbors += (grid[i][j-1] != 0)
        if j != len(grid[0]):
            neighbors += (grid[i][j+1] != 0)
        neighbors += (grid[i+1][j-1] != 0)
        neighbors += (grid[i+1][j] != 0)
        neighbors += (grid[i+1][j+1] != 0)
        print(neighbors)
        if neighbors < 2:
            newgrid[i][j] = 0
        elif neighbors > 3:
            newgrid[i][j] = 0
        else:
            if grid[i][j] < 7:
                newgrid[i][j] = grid[i][j] + 1
            else:
                newgrid[i][j] = 1
                
print(newgrid)
        
    
myapp = App()
myapp.run()
