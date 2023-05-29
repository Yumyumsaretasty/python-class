import turtle
colors = ['red', 'blue', 'teal', 'green', 'orange', 'yellow','white','misty rose','dark slate blue','orange red','wheat','seashell','purple','gold','medium purple','tomato','dark red','dark red','black']
t = turtle.Pen()
turtle.bgcolor('pink')
for x in range(360):
    t.pencolor(colors[x%19])
    t.width(x//100 + 1)
    t.speed(0)
    t.forward(x)
    t.left(59)