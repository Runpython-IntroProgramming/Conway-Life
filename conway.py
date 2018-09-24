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

coordinates = {}
for x in range(10):
    for y in range(10):
        coordinates[(x,y)] = "G"
        print(coordinates[(x,y)] , end = "")
    else:
        print("")







Sprite(cell,(10,10))
Sprite(cell,(10,0))








app = App()
app.run()

    