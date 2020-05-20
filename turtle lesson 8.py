from math import pi, sin, cos
import turtle
turtle.shape('turtle')

lenght = 10
count = 0
degree = 90

while count < 1000:
    turtle.forward(lenght)
    turtle.left(90)
    lenght +=5
    count += 1

    if count == 1000:
        print("Count = 20")
        break