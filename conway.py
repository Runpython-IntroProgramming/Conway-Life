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

list1=[]

square = RectangleAsset(20,20, line, white)
Rsquare = RectangleAsset(20,20, line, red)


for x in range(0,20):
    for y in range(0,20):
        Sprite(square, (20*x,20*y))
        list1.append(Sprite(square, (20*x,20*y)))



class Conway(App):
    
    def __init__(self):
        super().__init__()
        self.listenMouseEvent('click', self.mouseClick)
        
    def mouseClick(self, event):
        x=event.x
        y=event.y
        for sprite in list1:
            print("here!")
            xsprite =sprite.x
            ysprite=sprite.y
            if x<= xsprite + 7.5 and x>= xsprite -7.5 and y<=ysprite + 7.5 and y>= ysprite -7.5:
                sprite = Rsquare


myapp = Conway()
myapp.run()