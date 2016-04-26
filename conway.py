"""
conway.py
Author: Glen Passow
Credit: 
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
thinline = LineStyle(1, black)
a = 0
b = 0
height = 20
width = 20
squares = {}
thinline = LineStyle(1, black)
rectangle = RectangleAsset(20, 20, thinline, green)


class cell(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.current = False
        self.sca = 0
        self.visible = True

for x in range(0, height):
            for y in range(0, width):
                squares[(x,y)] = cell(rectangle, (x*height, y*width))

class ConwayGame(App):
    
    def __init__(self):
        ConwayGame.listenKeyEvent("keydown", "space", self.spaceclick)
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 480
        self.going = False
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        ConwayGame.listenMouseEvent("click",self.breathlife)
   
    def breathlife(self, event):
        self.cx = event.x
        self.cy = event.y
    
    def spaceclick(self,event):
        self.going = False

    def step(self):
        if self.going == False:
            #self.cx = int(self.cx/20)
            #self.cy = int(self.cy/20)
            print(self.cx)
            print(self.cy)
            #squares[(self.cx, self.cy)].visible = False
            squares[(1, 1)].visible = False
            self.going = True
           


        if self.going == True:
            for g in range(0, height):
                for f in range(0, width):
                    if squares[(g,f)].sca == True:
                        squares[(g,f)].sca = squares[(g,f)].sca - 1
                    for w in range(-1, 2):
                        for h in range(-1, 2):
                            if (w, h) in squares and squares[(w, h)].current == True:
                                squares[(g,f)].sca += 1
                                print(squares[(g,f)].sca)
            
            for s in range(0, height):
                for d in range(0, width):
                    if squares[(s, d)].current == True and squares[(s, d)].sca < 3 or squares[(s, d)].sca > 3:
                        squares[(s, d)].current = False
                    elif squares[(s, d)].current == False and squares[(s, d)].sca == 3:
                        squares[(s, d)].current = True
                    else:
                        squares[(s, d)].current = True
myapp = ConwayGame()
myapp.run()