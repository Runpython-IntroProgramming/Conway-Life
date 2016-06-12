"""
conway.py
Author: Adam Glueck
Credit: Glen Passow, Stack overflow
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import Frame, App, Color, RectangleAsset, Sprite, ImageAsset, LineStyle 
black=Color(0x000000,1.0)
celestegreen=Color(0x00FFB7,1.0)
red=Color(0xBA0000,1.0)
line=LineStyle(1, black)
height=30
width=30
#imports graphics, gets color, sets dimensions of squares
dictionary={}
#creates an aptly named dictionary
thinline=LineStyle(1, black)
livingcell=RectangleAsset(30,30,line,celestegreen)
zombiecell=RectangleAsset(30,30,line,red)
#creates squares
class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.visible=False
        self.sca=0
for x in range(0,height):
            for y in range(0,width):
                Sprite(zombiecell,(x*height,y*width))
                dictionary[(x,y)]=cell(livingcell,(x*height,y*width))
class ConwayGame(App):
    def __init__(self):
        ConwayGame.listenKeyEvent("keydown", "space",self.spaceclick)
        SCREEN_WIDTH=960
        SCREEN_HEIGHT=720
        self.moving = False
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        ConwayGame.listenMouseEvent("click",self.create)
        #creates the screen
    def create(self, event):
        self.cx=int(event.x/30)
        self.cy=int(event.y/30)
        #identifies mouse location
        dictionary[(self.cx, self.cy)].visible=not dictionary[(self.cx, self.cy)].visible
        #makes dead living by checking if inivis and if so making vis
    
    def spaceclick(self,event):
        self.moving=not self.moving
    def step(self):
        if self.moving==True:
            for a in range(0,height):
                for b in range(0,width):
                    if dictionary[(a,b)].visible==True:
                        dictionary[(a,b)].sca=dictionary[(a,b)].sca-1
                    for c in range(-1,2):
                        for d in range(-1,2):
                            if (c+a, d+b) in dictionary and dictionary[(c+a,d+b)].visible==True:
                                dictionary[(a,b)].sca=dictionary[(a,b)].sca+1
            
            for e in range(0,height):
                for f in range(0,width):
                    if dictionary[(e,f)].visible==True and dictionary[(e,f)].sca<2:
                        dictionary[(e,f)].visible=False
                    elif dictionary[(e,f)].visible==True and dictionary[(e,f)].sca>3:
                        dictionary[(e,f)].visible=False
                    elif dictionary[(e,f)].visible==False and dictionary[(e,f)].sca==3:
                        dictionary[(e,f)].visible=True
                    dictionary[(e,f)].sca=0
                    #check
myapp=ConwayGame()
myapp.run()
