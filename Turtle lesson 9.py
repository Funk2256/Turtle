import turtle

turtle.shape('turtle')


def figure(a, step):
    turtle.pendown()
    angle = 360 / a
    for x in range(a):
        turtle.pendown()  # Pen down for draw
        turtle.forward(step)  # Step
        turtle.left(angle)  # Turn left on 90 angle
        x -= 1


def next_position(x, y, ):
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(39)  # Left turn angle


figure(3, 100)
next_position(+38, -60)
figure(4, 110)
next_position(+120, -65)
figure(5, 130)
next_position(+200, +10)
figure(6, 150)
