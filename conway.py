"""
conway.py
Author: Eric Goodney
Credit: Jack, Patrick, Teacher, http://brythonserver.github.io/ggame/#ggame.MouseEvent
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""


from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor

myapp = App()

red = Color(0xFF4040, 1.0)
green = Color(0x00FF00, 1.0)
blue = Color(0x1C86EE, 1.0)
white = Color(0xF8F8FF, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xFF7D40, 1.0)
thinline1 = LineStyle(1, black)
thinline = LineStyle(1, blue)
#Making the grid. Square 400 by 400 goes up by 40
grid1 = RectangleAsset(1300,800, thinline1, black)
Sprite(grid1, (0,0))
grid = RectangleAsset(400,400, thinline, blue)
Sprite(grid, (320,120))
line1 = RectangleAsset(1,400, thinline, blue)
line2 = RectangleAsset(400,1, thinline, blue)
for x in range(11):
    Sprite(line1, (((x*40)+320), 120))
    Sprite(line2, (320, ((x*40)+120)))
ball_asset = ImageAsset("Conway-life.png", Frame(62,210,275,275),3)
#blue=image(0) [dead]  red=image(1)[baby] black=image(2)[old]
#have beginning of the games start out with 
sprites = {}
for g in range (10):
    x = ((g)*40)+320
    for h in range(10):
        y = ((h)*(40))+120
        sball = Sprite(ball_asset,(x, y))
        sprites[sball.position] = sball
        sball.setImage(0)
        sball.scale = 0.145
#allows user to make cells alive 
def mouseClick(event):
    x = floor(event.x/40)*40
    y = floor(event.y/40)*40
    s = sprites[(x,y)]  
    s.setImage(1)
    

#Getting into the actual conway game of life
#Finding which neighboring cells are alive or dead. 
def livingneighbors(position):
    neighbors = 0
    if sprites[(position[0]+40,position[1])].index in [0,2]:
        neighbors += 1
        #right
    if sprites[(position[0]+40,position[1]+40)].index in [0,2]:
        neighbors += 1
        #bottom right
    if sprites[(position[0]+40,position[1]-40)].index in [0,2]:
        neighbors += 1
        #top right
    if sprites[(position[0]-40,position[1])].index in [0,2]:
        neighbors += 1
        #left
    if sprites[(position[0]-40,position[1]-40)].index in [0,2]:
        neighbors += 1
        #top left
    if sprites[(position[0]-40,position[1]+40)].index in [0,2]:
        neighbors += 1
        #bottom left 
    if sprites[(position[0],position[1]+40)].index in [0,2]:
        neighbors += 1
        #bottom
    if sprites[(position[0],position[1]-40)].index in [0,2]:
        neighbors += 1
        #top
    return neighbors
    

def step():
    spritestokill = []
    spritestobirth = []

    for pos in sprites:
        if pos[0] > 320 and pos[0] < 680 and pos[1] < 480 and pos[1]> 120:
            #alive = livingcell(pos)
            n = livingneighbors(pos)
            if n < 2 or n > 3:
                spritestokill.append(pos)
            if n == 2:
                spritestobirth.append(pos)
            if n ==3:
                spritestobirth.append(pos)
    
    for pos in spritestokill:
        # kill this sprite
        sprites[pos].setImage(0)
    
    for pos in spritestobirth:
        # set this sprite to born
        sprites[pos].setImage(1)
    
def spaceKey(event):
#START WITH THIS 

myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenMouseEvent('click', mouseClick)
myapp.run(step)
