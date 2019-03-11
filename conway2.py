"""
conway2.py
Author: Sean Healey
Credit: Tutorial, Stack Overflow
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, CircleAsset, RectangleAsset
import random

myapp = App()

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

circles = [redcircle, orangecircle, yellowcircle, greencircle, bluecircle, purplecircle, blackcircle]

# Get dimensions from user
# Width of grid
gridcolumns = int(input("How wide would you like the simulation to be? "))
# Height of grid
gridrows = int(input("How tall would you like the simulation to be? "))
# Total # of generations
num_generations = int(input("How many generations would you like to simulate? "))

# Create grid
# Grid[row][column]
grid = []
for i in range(0,gridrows):
    grid.append([0] * gridcolumns)
    for j in range(0,gridcolumns):
        grid[i][j] = random.randint(0,1)
        if grid[i][j] == 1:
            grid[i][j] = random.randint(1,7)

def tick():            
    # Keeps running simulation until reaching desired number of generations
    # Make this into a function
    #gen_count = 0
    #while gen_count < num_generations:
    # Clears grid
    Sprite(RectangleAsset(gridcolumns*10, gridrows*10, noline, white), (0,0))
    
    # Neighbors matrix counts neighbors for each cell (convert into function?)
    neighbors = [0] * len(grid)
    neighbors = [ [0] * len(grid[0]) for x in neighbors]

    for i in range(0, len(grid)): # rows
        for j in range(0, len(grid[0])): # columns
            count = 0
            if i-1 >= 0 and j-1 >= 0 and grid[i-1][j-1] != 0:
                count += 1
            if i-1 >= 0 and grid[i-1][j] != 0:
                count += 1
            if i-1 >= 0 and j+1 < len(grid[0]) and grid[i-1][j+1] != 0:
                count += 1
            if j-1 >= 0 and grid[i][j-1] != 0:
                count += 1
            if j+1 < len(grid[0]) and grid[i][j+1] != 0:
                count += 1
            if i+1 < len(grid) and j-1 >= 0 and grid[i+1][j-1] != 0:
                count += 1
            if i+1 < len(grid) and grid[i+1][j] != 0:
                count += 1
            if i+1 < len(grid) and j+1 < len(grid[0]) and grid[i+1][j+1] != 0:
                count += 1
            neighbors[i][j] = count
        
    for i in range(0, len(grid)):
        for j in range(0,len(grid[0])):
            if neighbors[i][j] < 2:
                grid[i][j] = 0
            elif neighbors[i][j] > 3:
                grid[i][j] = 0
            elif grid[i][j] != 0:
                grid[i][j] += 1
            elif neighbors[i][j] == 3:
                grid[i][j] += 1
    #gen_count += 1
    
    # Make this into it's own function
    # Create Sprites for each element in grid
    x = 0
    y = 0
    for i in grid:
        for j in i:
            if j > 7:
                Sprite(circles[6], (x,y))
            elif j > 0:
                Sprite(circles[j-1], (x,y))
            x += 10
        x = 0
        y += 10
                    
myapp.run(tick)
