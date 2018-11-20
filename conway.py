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
thinline = LineStyle(1, red)

#Making the grid. Square 400 by 400 goes up by 40
grid1 = RectangleAsset(1300,800, thinline1, black)
Sprite(grid1, (0,0))

grid = RectangleAsset(400,400, thinline, green)
Sprite(grid, (0,0))
line1 = RectangleAsset(1,400, thinline, red)
line2 = RectangleAsset(400,1, thinline, red)
for x in range(11):
    Sprite(line1, (x*40, 0))
    Sprite(line2, (0, x*40))
ball_asset = ImageAsset("Conway-life.png", Frame(62,210,275,275),3)

#have beginning of the games start out with 
sprites = []
for g in range (10):
    x = (g)*40
    for h in range(10):
        y = (h)*(40)
        sball = Sprite(ball_asset,(x, y))
        sprites.append(sball)
        sball.setImage(1)
        sball.scale = 0.145
"""
#allows player to click cells to make them aive
def mouseClick(event):
    x = floor(event.x/40)*40 
    y = floor(event.y/40)*40



#(g+1)*40

#If empty cell is touching three live balls- ball image 0

#If ball is touching one or fewer balls - image 2

#If ball is touching four or more balls -- image 2

#If ball is touching 2 or 3 balls- image 1


#list of every sprite location
# should start out with 100 dead sprites (image 2)

"""


myapp = App()
"""
myapp.listenMouseEvent('click', mouseClick)
"""
myapp.run()