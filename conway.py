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
#imports graphics and defines colors and lines
height=30
length=30
#defines dimensions of cell
dictionary={}
#creates empty dictionary to store cell data
thinline=LineStyle(1, black)
livingcell=RectangleAsset(30,30,line,celestegreen)
zombiecell=RectangleAsset(30,30,line,red)
#defines the look and dimensions of living cells and unliving cells :)

class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.visible=False
        self.sca=0

for x in range(0,height):
            for y in range(0,length):
                Sprite(zombiecell,(x*height,y*length))
                dictionary[(x,y)]=cell(livingcell,(x*height,y*length))
          
class ConwayLife(App):
    
    def __init__(self):
        ConwayLife.listenKeyEvent("keydown", "space",self.spaceclick)
        #listens for click
        SCREEN_length=960
        SCREEN_HEIGHT=720
        #sets display dimensions
        self.moving = False
        super().__init__(SCREEN_length, SCREEN_HEIGHT)
        ConwayLife.listenMouseEvent("click",self.create)
    def create(self, event):
        self.cx=int(event.x/30)
        self.cy=int(event.y/30)
        dictionary[(self.cx, self.cy)].visible=not dictionary[(self.cx, self.cy)].visible
        #this makes it so if you click on an undead cell, it becomes alive
    
    def spaceclick(self,event):
        self.moving=not self.moving
    def step(self):
        if self.moving==True:
            for a in range(0,height):
                for b in range(0,length):
                    if dictionary[(a,b)].visible==True:
                        #check to see if alive
                     dictionary[(a,b)].sca dictionary[(a,b)].sca-1
                    for c in range(-1,2):
                        for d in range(-1,2):
                            if (c+a, d+b) in dictionary and dictionary[(c+a,d+b)].visible==True:
                             dictionary[(a,b)].sca dictionary[(a,b)].sca+1
            
            for e in range(0,height):
                for f in range(0,length):
                    if dictionary[(e,f)].visible==True and dictionary[(e, f)].sca<2:
                     dictionary[(e,f)].visible=False
                    elif dictionary[(e,f)].visible==True and dictionary[(e, f)].sca>3:
                     dictionary[(e,f)].visible=False
                    elif dictionary[(e,f)].visible==False and dictionary[(e, f)].sca==3:
                     dictionary[(e,f)].visible=True
                 dictionary[(e,f)].sca=0
myapp=ConwayLife()
myapp.run()
