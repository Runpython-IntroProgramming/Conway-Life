"""
conway.py
Author: Noah Pikielny
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
#Any live cell with fewer than two live neighbors dies, as if by under population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by overpopulation.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset


class GameOfLife(App):
    
    def __init__(self):
        super().__init__()
        red = Color(0xff0000, 1.0)
        blue = Color(0x0000ff, 1.0)
        black = Color(0x000000, 1.0)
        noLine  = LineStyle(0, black)
        bg = RectangleAsset(self.width, self.height, noLine, black)
        Sprite(bg, (0,0))
        cell = CircleAsset(10, noLine, blue)
        Sprite(cell, (0,0))

    



myapp = GameOfLife()
myapp.run()