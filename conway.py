"""
conway.py
Author: Andrew Chen
Credit:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
http://brythonserver.github.io/ggame/

Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life

Rules of the Game:
Any live cell with fewer than two live neighbors dies, as if by under population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Rules of the Program:
As the Wikipedia article described, your "playing area" may have fixed boundaries, boundaries that wrap around top and bottom, or may be entirely unbounded (in some ways, the easiest approach!).
The user must be able to "turn on" cells by clicking on them with the mouse, or by click-dragging across the window.
If your playing area is unbounded, then the up/down/right/left cursor keys should allow the user to scroll the playing area within the window.
Your live cells should be two different colors: one for its first day of “life”, the second for all subsequent days.

1. define a grid area and borders
2. create reference system for points and their 8 neighbors
3. utilize reference system each tick to check every point and its neighbors simultaneously
4. actvate changes and restart
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset
black = Color(0x000000, 1.0)
darkgrey = Color(0x2C3E40, 1.0)
lightgrey = Color(0xEAECEE, 1.0)
white = Color(0xffffff, 1.0)
line = LineStyle(1, black)

deadcell = RectangleAsset(10, 10, line, darkgrey)
newcell = RectangleAsset(10, 10, line, white)
oldcell = RectangleAsset(10, 10, line, lightgrey)


mapsize = 10

# Creates coordinate plane and sets all cells to dead
coordinates = {}
for x in range(mapsize+1):
    for y in range(mapsize+1):
        coordinates[(x,y)] = 0

# Function that checks and compiles cells to change
def ticker():
    birthcell = []
    agecell = []
    killcell = []
    for x in range(1,mapsize):
        for y in range(1,mapsize):
            
            liveneigh = 0
            for xneigh in range(x-1,x+1):
                for yneigh in range(y-1,y+1):
                    if coordinates[(xneigh,yneigh)] != 0:
                        liveneigh += 1
            if coordinates[(x,y)] == 0 and liveneigh == 3:
                birthcell.append((x,y))
            elif coordinates[(x,y)] == 1 and liveneigh == 2  or liveneigh == 3:
                agecell.append((x,y))
            elif coordinates[(x,y)] != 0 and liveneigh != 2  or liveneigh != 3:
                killcell.append((x,y))
            
    for birth in birthcell:
        coordinates[birth] = 1
    for age in birthcell:
        coordinates[age] += 1
    for kill in killcell:
        coordinates[kill] = 0
    
    for x in range(1,mapsize):
        for y in range(1,mapsize):
            if coordinates[(x,y)] == 0:
                Sprite(deadcell,(x*10,y*10))
            if coordinates[(x,y)] == 1:
                Sprite(newcell,(x*10,y*10))
            else:
                Sprite(oldcell,(x*10,y*10))
    
ticker():

app = App()
app.run()

    