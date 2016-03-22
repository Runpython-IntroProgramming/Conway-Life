"""
conway.py
Author: Mary Feyrer
Credit: Tess Snyder, Mr. Dennison 
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
line = LineStyle(.2, black)
list1 = []
redlist = []

square = RectangleAsset(20, 20, noline, red) 
screen = RectangleAsset(400,400, line, white)
Sprite(screen,(0,0))

for x in range(0,20):
    for y in range(0,20):
        s = Sprite(square, (20*x,20*y))
        s.visible = False
        list1.append(s)

class Conway(App):
    
    def __init__(self):
        super().__init__()
        self.listenMouseEvent( 'click', self.click)
    
    def click(self, event):
        x = event.x
        y = event.y
        for sprite in list1:
            if x<= sprite.x +10 and x>= sprite.x-10 and y<= sprite.y+10 and y>= sprite.y-10:
                sprite.visible = True
                
    
    for sprite in list1: #interation??
        if sprite.visible=True:
            redlist.append(sprite)
    for sprite in list1:
        surroudlist = []
        for redsprite in redlist:
            if abs(sprite.x - redsprite.x) >= 20 and abs(sprite.y - redsprite.y) >= 20:
                surroundlist.append(redsprite)
                n = surroundlist.count
                if n > 3:
                    sprite.visible = False
                elif n = 3:
                    sprite.visible = True
                elif n < 2:
                    sprite.visible = False
        
            

myapp = Conway()
myapp.run()
