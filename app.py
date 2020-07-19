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
ball = turtle.Turtle()
ball.speed(0) #sets speed of animation
ball.shape('square') #box is 20x20
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1



#function (moving the paddle)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 #adds 20 pixels to y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 #adds 20 pixels to y
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 #adds 20 pixels to y
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 #adds 20 pixels to y
    paddle_b.sety(y)


#keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

#main game loop
while True:
    wn.update() #every time the loop runs it updates the screen

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #ball reset in the middle if it goes off screen
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
