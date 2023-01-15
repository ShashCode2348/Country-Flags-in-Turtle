import turtle as t

def rectangle_with_fill(horizontal, vertical, color):
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

#setup
t.setup(1000, 600)
t.penup()

#Black Stripe
t.goto(-500, 300)
t.setheading(0)
rectangle_with_fill(1000, 200, '#000000')

#Red Stripe
t.goto(-500, 100)
t.setheading(0)
rectangle_with_fill(1000, 200, '#DD0000')

#Yellow Stripe
t.goto(-500, -100)
t.setheading(0)
rectangle_with_fill(1000, 200, '#FFCE00')
t.hideturtle()
