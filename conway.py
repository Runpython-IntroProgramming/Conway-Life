"""
conway.py
Author: Emma Dunbar
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

green=Color(0x00ff00, 1.0)
blue=Color(0x0000ff, 1.0)
white=Color(0xffffff, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(0, black)

life1=(RectangleAsset(2, 2, tline, green))
life2=(RectangleAsset(2, 2, tline, blue))
none=(RectangleAsset(2, 2, tline, white))

l1=[]
n=10

for x in range(0,n):
    l1=l1+[x]
print(l1)



#def createlife():
    #Sprite(life1,(x,y))
    #return
#def staylife():
    #Sprite(life2,(x,y))
    #return
#def death():
    #Sprite(none,(x,y))

#staylife()
#death()

#in a period it has to assess all the pixels and do something for each pixel in the grid
#for x in range (0,400,3):
    #Sprite(life1,(x,400))
#Sprite(life2,(400, 400))


#myapp = App()
#myapp.run()