"""
conway.py
Author: Sean Healey
Credit: Tutorial, Stack Overflow
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, CircleAsset

# Colors
red = Color(0xff0000, 1.0)
orange = Color(0xffa500, 1.0)
yellow = Color(0xffff00, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
purple = Color(0x800080, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

noline = LineStyle(0, white)

colorslist = [red, orange, yellow, green, blue, purple, black]

class Cell(Sprite):
    """
    Cell
    """
    
    def __init__(self):
        super().__init__()
        
        self.alive = 1
        self.age = 0
        self.color = colorslist[self.age]
        
        # Display Cell
        if self.alive == 1:
            circle = CircleAsset(5, noline, self.color)

class Conway(App):
    """
    Play Conway's Game
    """
    
    def __init__(self):
        super().__init__()
        
        Cell()

myapp = Conway()
myapp.run()