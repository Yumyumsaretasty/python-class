from turtle import*
speed(0)
pensize(5)
penup()
color('red')
setposition(-400,0)
pendown()
number = 0
begin_fill()
while number <= 10:
    if number < 4:
        forward(50)
        left(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        left(90)        
    if number >= 4:
        forward(10)
        left(90)
        forward(10)
        right(90)
        forward(10)
        right(90)
        forward(10)
        left(90)
    number=number+1
color('blue')
end_fill()
done()