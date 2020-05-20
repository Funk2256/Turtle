import turtle

turtle.shape('turtle')
step = 10
step2 = 20
def figure(step, angle):
    for x in range(36):
        if x > 0:
            turtle.pendown()  # Pen down for draw
            turtle.forward(step)  # Step
            turtle.left(angle)  # Turn left on 90 angle
            x -= 1
        else:
            turtle.left(90)
            pass

turtle.goto(0,0)
figure(step, 10)







