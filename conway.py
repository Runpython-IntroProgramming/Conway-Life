"""
conway.py
Author: Mary Feyrer
Credit: Tess Snyder, Mr. Dennison 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset
from ggame import LineStyle, Color, Sprite, Sound

white = Color(0xffffff, 1.0)
black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
noline = LineStyle(0, black)
line = LineStyle(.2, black)
list1 = []

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
        self.running = False
        self.listenKeyEvent("keydown", "space", self.spacebar)
        self.listenKeyEvent("keydown", "s", self.skey)
    
    def click(self, event):
        x = event.x
        y = event.y
        for sprite in list1:
            if x<= sprite.x +10 and x>= sprite.x-10 and y<= sprite.y+10 and y>= sprite.y-10:
                sprite.visible = True
                
    def spacebar(self, event):
        self.running = True
    
    def skey(self, event):
        self.running = False
    
    def step(self):
        if self.running == True:
            redlist=[]
            for spr in list1:
                if spr.visible==True:
                    redlist.append(spr)
            for sprite in list1:
                surroundlist=[]
                for redsprite in redlist:
                    if abs(sprite.x-redsprite.x) <= 20 and abs(sprite.y-redsprite.y) <= 20 "and redsprite!=sprite" :
                        surroundlist.append(redsprite)
                        num=len(surroundlist)
                        if sprite.visible==True:
                            num=len(surroundlist) - 1
                        if num>3:
                            sprite.visible = False
                        elif num==3:
                            sprite.visible = True
                        elif num<2:
                            sprite.visible = False
        

myapp = Conway()
myapp.run()
