# Basic PingPong in Python 3 

#
from fontTools.ttLib import TTFont
import turtle
import winsound

wn = turtle.Screen()
wn.bgcolor("red")
wn.setup(width=600, height=400)
wn.tracer(0)
wn.title("PingPong")

# Paddle 1 
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=4, stretch_len=0.7)
paddle_1.color("white")
paddle_1.fillcolor("yellow")
paddle_1.penup()
paddle_1.goto(-250, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=4, stretch_len=0.7)
paddle_2.color("white")
paddle_2.fillcolor("yellow")
paddle_2.penup()
paddle_2.goto(250, 0)

# Ball 

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.15
Ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 160)
pen.write("Player R: 0   Player L: 0", align="center", font=('VT323', 18, "normal"))


# Function

def paddle_1_up():
    y = paddle_1.ycor()
    y += 15
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 15
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 15
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 15
    paddle_2.sety(y)

#Keyboard Player 1
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")

#Keyboard Player 2
wn.onkeypress(paddle_2_up, "8")
wn.onkeypress(paddle_2_down, "2")


# Score

score_1 = 0
score_2 = 0

# Main game Loop
while True: 
    wn.update()

    # Ball Moving
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border checking
    if Ball.ycor() > 190:
        Ball.sety(190)
        Ball.dy *= -1
        winsound.PlaySound('bounce.wav' ,winsound.SND_ASYNC)

    if Ball.ycor() < -190:
        Ball.sety(-190)
        Ball.dy *= -1
        winsound.PlaySound('bounce.wav' ,winsound.SND_ASYNC)

    if Ball.xcor() > 320:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player R: {}   Player L: {} ".format(score_1, score_2), align="center", font=('VT323', 18, "normal"))

    if Ball.xcor() < -320:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player R: {}   Player L: {} ".format(score_1, score_2), align="center", font=('VT323', 18, "normal"))

    # Collisions
    if (Ball.xcor() > 240 and Ball.xcor() < 250) and (Ball.ycor() < paddle_2.ycor() + 40 and Ball.ycor() > paddle_2.ycor() -40):
        Ball.setx(240)
        Ball.dx *= -1
        winsound.PlaySound('PingPong.wav' ,winsound.SND_ASYNC)

    if (Ball.xcor() < -240 and Ball.xcor() > -250) and (Ball.ycor() < paddle_1.ycor() + 40 and Ball.ycor() > paddle_1.ycor() -40):
        Ball.setx(-240)
        Ball.dx *= -1
        winsound.PlaySound('PingPong.wav' ,winsound.SND_ASYNC)
   