import turtle

t = turtle.Pen()

turtle.bgcolor('pink')
t.number=1
while t.number<2000:
    t.width(t.number//100 + 1)
    t.speed(0)
    t.forward(t.number)
    t.left(90)
    t.number=t.number+10
turtle.done()