## followed tutorial provided by @TokyoEdtech
#import turtle module (graphics)
import turtle
import winsound


wn = turtle.Screen()
wn.title('Pong by Jacobkato49')
wn.bgcolor('blue') # background color of game

#set up screen
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating

#score
score_a=0
score_b=0

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

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A:0  Player B:0', align='center', font=('Courier', 24, 'normal'))

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
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    #ball reset in the middle if it goes off screen
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write('Player A:{}  Player B:{}'.format(score_a,score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write('Player A:{}  Player B:{}'.format(score_a,score_b), align='center', font=('Courier', 24, 'normal'))


    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
