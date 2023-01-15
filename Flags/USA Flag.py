import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def star(length, points, color):
    sumangle = ((points*2)-2) * 180
    oneangle = sumangle/points
    smallangle = oneangle/3.5
    bigangle = oneangle - smallangle
    t.color(color)
    t.pendown()
    t.begin_fill()
    t.penup()
    for counter in range(points):
        t.forward(length)
        t.left(smallangle)
        t.forward(length)
        t.left(bigangle)
    t.end_fill()

t.penup()

gotoy = 222

t.speed(0)
t.setup(988,520)
t.goto(494,260)
t.pendown()

for counter in range(7):
    t.setheading(-90)
    rectangle(40,988,'#B22234')
    t.setheading(-90)
    t.forward(80)

t.penup()

t.setheading(0)
t.goto(-494,260)
t.pendown()

rectangle(494,280,'#3C3B6E')
t.goto(-474,245)
for counter in range(4):
    for counter in range(6):
        star(9,5,'white')
        t.setheading(0)
        t.forward(84)
        t.penup()
    t.goto(-434,gotoy)
    gotoy = gotoy - 28
    t.pendown()
    for counter in range(5):
        star(9,5,'white')
        t.setheading(0)
        t.forward(84)
    t.goto(-476,gotoy)
    gotoy = gotoy - 28

for counter in range(6):
        star(9,5,'white')
        t.setheading(0)
        t.forward(84)
        t.penup()

t.hideturtle()
