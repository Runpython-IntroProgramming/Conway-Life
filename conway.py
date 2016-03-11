"""
conway.py
Author: Mary Feyrer
Credit: Tess Snyder
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset 
from ggame import LineStyle, Color, Sprite, Sound

white = Color(0xffffff, 1.0)
blue = Color(0x000000, 1.0)
black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
line = LineStyle(.1, black)
list=[]

square = RectangleAsset(10, 10, line, white) 
Rsquare = RectangleAsset(10, 10, line, red)
for x in range(0,50):
    for y in range(0,50):
        Sprite(square, (10*x,10*y))
        list.append(Sprite(square, (10*x,10*y)))

class Conway(App):
    
    def __init__(self):
        Conway.listenMouseEvent( 'click', self.click)
    
    def mouse(click, event):
        x = event.x
        y = event.y
        for sprite in list:
            xsprite = list[x][1][0]
            if x<= xsprite+5 or x>= xsprite-5:
                list[x] = Rsquare
    
 

myapp = App()

myapp.run()
