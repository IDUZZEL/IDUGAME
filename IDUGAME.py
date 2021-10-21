import turtle
z = turtle.Screen() 
z.title('IDUGAME(by IDUZZEL)') 
z.bgcolor('black') 
z.setup(width=600 , height=500) 
z.tracer(0)

#player1
x1 = turtle.Turtle()
x1.speed(0)
x1.shape('square')
x1.shapesize(stretch_wid=1, stretch_len=4)
x1.color('red')
x1.penup()
x1.goto(0,-220)
#b_border
x2 = turtle.Turtle()
x2.speed(0)
x2.shape('square')
x2.shapesize(stretch_wid=2, stretch_len=40)
x2.color('blue')
x2.penup()
x2.goto(0,250)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('green')
ball.penup()
ball.goto(0,0)
ball.dx = 0.6
ball.dy = 0.8

def control_left():
    position = x1.xcor()
    position += -35
    x1.setx(position)
z.listen()
z.onkeypress(control_left, 'a') 
def control_right():
    position = x1.xcor()
    position += +35
    x1.setx(position)
z.listen() 
z.onkeypress(control_right, 'd')
#score
scr = turtle.Turtle()
scr.speed(0)
scr.color("yellow")
scr.penup()
scr.hideturtle()
scr.goto(0,200)
score=0
while True:
    z.update() 
    #ball-mov
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border
    if ball.ycor() >220:
        ball.sety(220)
        ball.dy *= -1
    if ball.ycor() < -240:
        ball.goto(0, 0)
        ball.dy *= -1
        scr.clear()
        score *= 0
    if ball.xcor() >280:
        ball.setx(280)
        ball.dx *= -1
    if ball.xcor() < -280:
        ball.setx(-280)
        ball.dx *= -1
    if (ball.ycor() < -210 and ball.ycor() > -220) and (ball.xcor() < x1.xcor() + 30 and ball.xcor() > x1.xcor() -30):
        ball.sety(-210)
        score += 1
        scr.clear()
        ball.dy *= -1
        scr.write("score: {} ".format(score), align='center', font=('courier',15,'normal'))
