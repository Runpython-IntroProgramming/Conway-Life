"""
conway.py
Author: Ella Edmonds
Credit: None
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
'''
class grid(Sprite):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    asset = RectangleAsset(8,8,side,grey)
    
    def __init__(self, position):
        super().__init__(grid.asset, position)
    
    grid(10,10)


class grid(App):
  
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        grid((100,100))
'''


grid=[]
for m in range(10):
    grey = Color(0x000000,.3)
    side = LineStyle(1,grey)
    square = RectangleAsset(8,8,side,grey)
    a = sprite(square,(10,10+(8*m)))
    m=m+1
    grid.append(a)
    
moregrid=[]
for m in range(10):
    sprite(grid(m))



myapp = App()
myapp.run()