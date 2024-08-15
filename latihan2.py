from turtle import *

hideturtle()
speed(100)
bgcolor('black')
for i in range(25):
    for j in range(15):
        color((j/15, i/25, 0.8))
        right(90)
        circle(200-i*4,90)
        left(90)
        circle(200-i*4,90)
        right(180)
        circle(50,24)
done()