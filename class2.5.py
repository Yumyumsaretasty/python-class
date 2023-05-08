from turtle import *
color('red', 'yellow')
begin_fill()
for x in range(1000000):
    if x == 3: break
speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
penup()
backward(300)
pendown()
color('blue', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
  

done()
for x in range(10): # 0 - 9
    if x == 1: print('monkey')
    if x == 2: print('banana')
    if x == 3: print('gorilla')
    if x == 4: print('yum yum')
    if x == 5: print('bay bay')
    if x == 9: print('too too')
    if x == 10: print('ponpon')