# Conway's Game of Life - (Level III)

The purpose of this challenge is to practice building a graphical application with Python and ggame.

Your task is to create a program using Python and ggame that plays [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life). The 
Wikipedia article describes the rules and has an animated image that shows what it 
looks like. I also have a [screencast video on Youtube](http://youtu.be/I5Hb268rZyw) that demonstrates
the desired functionality.

## Some basic requirements for your submission:

* You may use code supplied in the graphics tutorials as a starting point.
* Live cells in your program may be represented as rectangles, circles, or any other shape that you 
  would like to use. The example in the video above uses small circles.
* The initial state of live cells may be preset or randomized by you, but it must be possible to start 
  the game with a blank screen.
* As the Wikipedia article described, your "playing area" may have fixed boundaries, boundaries that wrap 
  around top and bottom, or may be entirely unbounded (in some ways, the easiest approach!).
* The user must be able to "turn on" cells by clicking on them with the mouse, or by click-dragging across 
  the window.
* If your playing area is unbounded, then the up/down/right/left cursor keys should allow the user to scroll 
  the playing area within the window.
* Your live cells should be two different colors: one for its first day of “life”, the second for all 
  subsequent days.


There are TONS of implementations of Conway's Life "out there" on the Internet. Some live in the web browser, 
some use Java, etc. You may certainly look at these examples to build an understanding of how it works. 
There are also many implementations of Conway's Life written for Python, but you may not submit 
them for this project (obviously). You may look at other solutions for inspiration or ideas, but **you must 
fully understand all code that you submit and give credit for any borrowed code or ideas**.

My old "reference" implementation (which I certainly don't claim to be optimal) using Python and Pygame had 
166 lines (including blanks).

Note: your submitted program will not be automatically checked for correctness. Any submission will 
automatically “pass”. I will download and execute your submitted scripts, however.
