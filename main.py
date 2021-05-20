import turtle
import random
a=turtle.Screen()
boundary=turtle.Turtle()
boundary.penup()
boundary.goto(-650 ,-325)
boundary.speed(0)
for i in range(2):
    boundary.forward(1300)
    boundary.right(90)
    boundary.forward(700)
    boundary.right(90)
lil=turtle.Turtle()
lil.shape("circle")
lil.penup()
b=turtle.Turtle()
b.shape("square")
b.penup()
def turnleft():
    b.setheading(180)
    b.forward(10)
def down():
    b.setheading(270)
    b.forward(10)
def up():
    b.setheading(90)
    b.forward(10)
def right():
    b.setheading(0)
    b.forward(10)
def scoreprint(boundary):
    boundary.undo()
    boundary.penup()
    boundary.hideturtle()
    boundary.setposition(-600,-300)
    scorestr="score:%s"%score
    boundary.write(scorestr,font=("Arial,22"))
turtle.onkey(turnleft,"Left")
turtle.onkey(down,"Down")
turtle.onkey(up,"Up")
turtle.onkey(right,"Right")
turtle.listen()
score=0
segments=[]
while True:
    lil.forward(1)
    b.forward(0.0000001)
    if b.xcor()>650 or b.xcor()<-650:
        turtle.bye()
    if b.ycor()>350 or b.ycor()<-350:
        turtle.bye()
    g=lil.distance(b)
    if g<15:
        score= score+1
        lil.setposition(random.randint(-650,650),random.randint(-350,350))
        new_segments=turtle.Turtle()
        new_segments.shape("turtle")
        new_segments.speed(0)
        new_segments.color("grey")
        new_segments.penup()
        segments.append(new_segments)
        scoreprint(boundary)
        for index in range(len(segments)-1,0,-1):
            x=segments[index-1].xcor()
            y = segments[index - 1].ycor()
            segments[index].setposition(x,y)
        if len (segments)>0:
            x=b.xcor()
            y=b.ycor()
            segments[0].setposition(x,y)
a.mainloop()
