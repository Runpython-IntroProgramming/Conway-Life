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
noline = LineStyle(0, black)
list1 = []

square = RectangleAsset(20, 20, noline, red) 


for x in range(0,20):
    for y in range(0,20):
        Sprite(square, (20*x,20*y))
        list1.append(Sprite(square, (20*x,20*y)))

class Conway(App):
    
    def __init__(self):
        super().__init__()
        self.listenMouseEvent( 'click', self.click)
    
    def click(self, event):
        x = event.x
        y = event.y
        for sprite in list1:
            if x<= sprite.x +10 and x>= sprite.x-10 and y<= sprite.y+10 and y>= sprite.y-10:
                sprite = Rsquare
    
 

myapp = Conway()
myapp.run()
