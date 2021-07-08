import turtle


#Screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#Left Paddle
lpad =turtle.Turtle()
lpad.speed(0)
lpad.shape("square")
lpad.color("white")
lpad.shapesize(stretch_wid=5, stretch_len=1)
lpad.penup()
lpad.goto(-350, 0)

#Right Paddle
rpad = turtle.Turtle()
rpad.speed(0)
rpad.shape("square")
rpad.color("white")
rpad.shapesize(stretch_wid=5, stretch_len=1)
rpad.penup()
rpad.goto( 350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Score
score_1=0
score_2=0

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 25, "normal"))


#Movements
def lpad_up():
    y = lpad.ycor()
    y += 20
    lpad.sety(y)

def lpad_dw():
    y = lpad.ycor()
    y -= 20
    lpad.sety(y)

def rpad_up():
    y=rpad.ycor()
    y += 20
    rpad.sety(y)

def rpad_dw():
    y = rpad.ycor()
    y -= 20
    rpad.sety(y)


#Keyboard
screen.listen()
screen.onkeypress(lpad_up, "w")
screen.onkeypress(lpad_dw, "s")
screen.onkeypress(rpad_up, "Up")
screen.onkeypress(rpad_dw, "Down")

#Loop
while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#Border
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1


    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 25, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 25, "normal"))

#Paddle Collisions

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < rpad.ycor() + 40 and ball.ycor() > rpad.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ( ball.ycor() < lpad.ycor() + 40 and ball.ycor() > lpad.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

