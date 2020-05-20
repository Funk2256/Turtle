import turtle

turtle.shape('turtle')

def figure(step, angle):
    for x in range(36):
        if x > 0:
            turtle.pendown()  # Pen down for draw
            turtle.forward(step)  # Step
            turtle.left(angle)  # Turn left on 90 angle
            x -= 1
        else:
            turtle.goto(0,0)

figure(10, 10)
figure(-10, 10)
turtle.left(90)
figure(10, 10)
turtle.left(45)
figure(-10, 10)
turtle.left(27)
figure(10, 10)
turtle.left(27)
figure(-10, 10)

turtle.left(65)
figure(10, 10)

