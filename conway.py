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

square = RectangleAsset(15,15, line, white)
Rsquare = RectangleAsset(15,15, line, red)


for x in range(0,20):
    for y in range(0,20):
        Sprite(square, (15*x,15*y))
        list.append(Sprite(square, (15*x,15*y)))



class Conway(App):
    
    def __init__(self):
        myapp.listenMouseEvent('click', self.mouseClick)

    def mouseClick(event):
        x=event.x
        y=event.y
        for sprite in list:
            print("here!")
            xsprite =sprite[1][0]
            ysprite=sprite[1][1]
            if x<= xsprite + 7.5 and x>= xsprite -7.5 and y<=ysprite + 7.5 and y>= ysprite -7.5:
                sprite = Rsquare


myapp = App()
myapp.run()