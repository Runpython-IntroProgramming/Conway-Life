"""
conway.py
Author: Tess Snyder
Credit: Mary Feyrer
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0) #color of dead cell
red = Color(0xff0000, 1.0) #color of first day of life
blue = Color(0x0000ff, 1.0) #color of subsequent days of life

line = LineStyle(.1, black)

list=[]

square = RectangleAsset(10,10, line, white)

for x in range(0,50):
    for y in range(0,50):
        Sprite(square, (10*x,10*y))
        list.append(Sprite(square, (10*x,10*y)))

print(list)


class Conway(App):
    
    def __init__(self):
        myapp.listenMouseEvent('click', mouseClick)

    def mouseClick(event):
        x=event.x


myapp = App()
myapp.run()