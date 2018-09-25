"""
conway.py
Author: Andrew Chen
Credit:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
http://brythonserver.github.io/ggame/
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Advanced-Graphics-with-Classes
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Dictionaries-and-Classes

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

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, KeyEvent, MouseEvent
black = Color(0x000000, 1.0)
grey = Color(0x808080, 1.0)
white = Color(0xffffff, 1.0)
line = LineStyle(1, black)

deadcell = RectangleAsset(10, 10, line, black)
newcell = RectangleAsset(10, 10, line, white)
oldcell = RectangleAsset(10, 10, line, grey)

print("""==================================================
CONTROLS
Click anywhere on the coordinate plane to kill or birth a cell
Press "space" to advance time one frame
==================================================
RULES
1. Any live cell with fewer than two live neighbors dies, as if by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
==================================================""")

#mapsize = int(input("Please input how long the map should be: ")) + 1
mapsize = 10

# Creates coordinate plane and sets all cells to dead
coord = {}
for x in range(mapsize+1):
    for y in range(mapsize+1):
        coord[(x,y)] = 0

# Function that displays cell grid
def display():
    for x in range(1,mapsize):
        for y in range(1,mapsize):
            if coord[(x,y)] == 0:
                Sprite(deadcell,(x*10,y*10))
            elif coord[(x,y)] == 1:
                Sprite(newcell,(x*10,y*10))
            elif coord[(x,y)] == 2:
                Sprite(oldcell,(x*10,y*10))

# Function that checks and compiles cells to change
def ticker(test):
    birthcell = []
    agecell = []
    killcell = []
    for x in range(1,mapsize):
        for y in range(1,mapsize):
            
            liveneigh = 0
            for xneigh in range(x-1,x+2):
                for yneigh in range(y-1,y+2):
                    if coord[(xneigh,yneigh)] == 1 or coord[(xneigh,yneigh)] == 2:
                        liveneigh += 1
            if coord[(x,y)] == 0 and liveneigh == 3:
                birthcell.append((x,y))
            elif coord[(x,y)] == 1 or coord[(x,y)] == 2:
                if liveneigh == 3 or liveneigh == 4:
                    agecell.append((x,y))
                else:
                    killcell.append((x,y))
    for birth in birthcell:
        coord[birth] = 1
    for age in agecell:
        coord[age] = 2
    for kill in killcell:
        coord[kill] = 0
    display():

def change(info):
    if coord[(int(info.x/10),int(info.y/10))] == 1 or coord[(int(info.x/10),int(info.y/10))] == 2:
        coord[(int(info.x/10),int(info.y/10))] = 0
    elif coord[(int(info.x/10),int(info.y/10))] == 0:
        coord[(int(info.x/10),int(info.y/10))] = 1
    display()
        
display():

App.listenKeyEvent("keydown", "space", ticker)
App.listenMouseEvent("mousedown", change)

app = App()
app.run()
    