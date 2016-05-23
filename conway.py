"""
conway.py
Author: Adam Glueck
Credit: Glen Passow
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import Frame, App, Color, RectangleAsset, Sprite, ImageAsset, LineStyle 

black=Color(0x000000,1.0)
celestegreen=Color(0x00FFB7,1.0)
red=Color(0xBA0000,1.0)
line=LineStyle(1, black)
a=0
b=0
height=20
width=20
squares={}
thinline=LineStyle(1, black)
livecell=RectangleAsset(20,20,line,celestegreen)
deadcell=RectangleAsset(20,20,line,red)

class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.visible=False
        self.sca=0

for x in range(0,height):
            for y in range(0,width):
                Sprite(deadcell,(x*height,y*width))
                squares[(x,y)]=cell(livecell,(x*height,y*width))
          
class ConwayGame(App):
    
    def __init__(self):
        ConwayGame.listenKeyEvent("keydown", "space",self.spaceclick)
        SCREEN_WIDTH=640
        SCREEN_HEIGHT=480
        self.going = False
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        ConwayGame.listenMouseEvent("click",self.create)
    def create(self, event):
        self.cx=int(event.x/20)
        self.cy=int(event.y/20)
        squares[(self.cx, self.cy)].visible=not squares[(self.cx, self.cy)].visible
    
    def spaceclick(self,event):
        self.going=not self.going
    def step(self):
        if self.going==True:
            for g in range(0,height):
                for f in range(0,width):
                    if squares[(g,f)].visible==True:
                        squares[(g,f)].sca=squares[(g,f)].sca-1
                    for w in range(-1,2):
                        for h in range(-1,2):
                            if (w+g, h+f) in squares and squares[(w+g,h+f)].visible==True:
                                squares[(g,f)].sca=squares[(g,f)].sca+1
            
            for s in range(0,height):
                for d in range(0,width):
                    if squares[(s, d)].visible==True and squares[(s, d)].sca<2:
                        squares[(s, d)].visible=False
                    elif squares[(s, d)].visible==True and squares[(s, d)].sca>3:
                        squares[(s, d)].visible=False
                    elif squares[(s, d)].visible==False and squares[(s, d)].sca==3:
                        squares[(s, d)].visible=True
                    squares[(s,d)].sca=0
myapp=ConwayGame()
myapp.run()
