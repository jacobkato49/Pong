## followed tutorial provided by @TokyoEdtech
#import turtle module (graphics)
import turtle


wn = turtle.Screen()
wn.title('Pong by Jacobkato49')
wn.bgcolor('blue') # background color of game

#set up screen
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed() #sets speed of animation
paddle_a.shape('square') #box is 20x20
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #box is now 100x20
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed() #sets speed of animation
paddle_b.shape('square') #box is 20x20
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #box is now 100x20
paddle_b.penup()
paddle_b.goto(350,0)


#ball
paddle_ball = turtle.Turtle()
paddle_ball.speed() #sets speed of animation
paddle_ball.shape('square') #box is 20x20
paddle_ball.color('white', 'black')
paddle_ball.penup()
paddle_ball.goto(0,0)


#function (moving the paddle)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 #adds 20 pixels to y
    paddle_a.sety(y)

#keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, 'w')

#main game loop
while True:
    wn.update() #every time the loop runs it updates the screen
