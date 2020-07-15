## followed tutorial provided by @TokyoEdtech
#import turtle module
import turtle


wn = turtle.Screen()
wn.title('Pong by Jacobkato49')
wn.bgcolor('blue') # background color of game

#set up screen
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating


#main game loop
while True:
    wn.update() #every time the loop runs it updates the screen
