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
    if sprites[(position[0]+40,position[1])].index ==1:
        neighbors += 1
        #right
    if sprites[(position[0]+40,position[1]+40)].index ==1:
        neighbors += 1
        #bottom right
    if sprites[(position[0]+40,position[1]-40)].index ==1:
        neighbors += 1
        #top right
    if sprites[(position[0]-40,position[1])].index ==1:
        neighbors += 1
        #left
    if sprites[(position[0]-40,position[1]-40)].index ==1:
        neighbors += 1
        #top left
    if sprites[(position[0]-40,position[1]+40)].index ==1:
        neighbors += 1
        #bottom left 
    if sprites[(position[0],position[1]+40)].index ==1:
        neighbors += 1
        #bottom
    if sprites[(position[0],position[1]-40)].index ==1:
        neighbors += 1
        #top
    return neighbors

spritestokill = []

for pos in sprites:
    if pos.position.x > 320 and pos.position.x < 680 and pos.position.y < 480 and pos.position.y > 120:
    #print noting 
        if pos > (680,480)
        #alive = livingcell(pos)
        n = livingneighbors(pos)
        if n < 2 or n > 3:
            spritestokill.append(pos)
            s = sprites[(x,y)]
            s.setImage(0)
        
        # do something to make the sprite at pos be DEAD
"""
def living neigbors (position):
neighbors = 0
if sprites[(position[0] + 40,position[1])].
index == 1:
neighbors +=1


do this for all surrounding cells. 
return neighbors 

for pos in sprites:
    alive = lving cell (pos)
    n = livingneigbors(pos)
    if alive and n <2 or n>3:
    cell must step. 

#If empty cell is touching three live balls- ball image 0 

check (x,y) to (x+40,y) (x-40,y) (x+40,y+40) (x-40,y-40) (x,y+40) (x,y-40) (x+40,y-40) (x-40,y+40)

#If ball is touching one or fewer balls - image 2

#If ball is touching four or more balls -- image 2

#If ball is touching 2 or 3 balls- image 1


#list of every sprite location
# should start out with 100 dead sprites (image 2)

"""
myapp = App()

myapp.listenMouseEvent('click', mouseClick)

myapp.run()