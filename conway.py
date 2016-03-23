"""
conway.py
Author: Tess Snyder
Credit: Mr. Dennison, Mary Feyrer, https://realpython.com/blog/python/pygame-a-primer/
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
noline = LineStyle(0, black)

list1=[]


screen=RectangleAsset(400,400, line, white)
Sprite(screen, (0,0))

square = RectangleAsset(20,20, noline, red)



for x in range(0,20):
    for y in range(0,20):
        s=Sprite(square, (20*x,20*y))
        s.visible= False 
        list1.append(s)



class Conway(App):
    
    def __init__(self):
        super().__init__()
        self.listenMouseEvent('click', self.mouseClick)
        self.running = False
        self.listenKeyEvent("keydown", "space", self.spacebar)
        
    def mouseClick(self, event):
        x=event.x
        y=event.y
        for sprite in list1:
            xsprite =sprite.x
            ysprite=sprite.y
            if x<= xsprite + 10 and x>= xsprite -10 and y<=ysprite + 10 and y>= ysprite -10:
               sprite.visible= True 
               
    
    def spacebar(self, event):
        self.running = True

    def step(self):
        if self.running == True:
            for sprite1 in list1:
                surroundlist=[]
                listred=[]
                for spr in list1:
                    if spr.visible==True:
                        listred.append(spr)
                for redsprite in listred:
                    if abs(sprite1.x-redsprite.x) == 20 and abs(sprite1.y-redsprite.y) == 20:
                        surroundlist.append(redsprite)
                        num=surroundlist.count
                        if num>3:
                            sprite1.visible=False
                        elif num==3:
                            sprite1.visible=True
                        elif num<2:
                            sprite1.visible=False

myapp = Conway()
myapp.run()