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
Bsquare = RectangleAsset(10, 10, line, blue)

for x in range(0,20):
    for y in range(0,20):
        Sprite(square, (20*x,20*y))
        list.append(Sprite(square, (15*x,15*y)))

class Conway(App):
    
    def __init__(self):
        Conway.listenMouseEvent( 'click', self.click)
    
    def click(self, event):
        x = event.x
        y = event.y
        for sprite in list:
            xsprite = sprite[1][0]
            ysprite = sprite[1][1]
            if x<= xsprite+5 and x>= xsprite-5 and y<= ysprite+5 and y>= ysprite-5:
                sprite = Rsquare
    
 

myapp = App()

myapp.run()
