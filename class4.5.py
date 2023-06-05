import turtle

colors = ['red']
t = turtle.Pen()
turtle.pensize(25)
turtle.bgcolor('pink')
for x in range(65):
    t.pencolor(colors[x%1])
    t.width(x//25 + 1)
    t.speed(0)
    t.forward(x)
    t.left(25)
t.forward(100)
t.left(45)
t.pendown()
t.forward(200)
t.left(95)
t.forward(200)
turtle.done()