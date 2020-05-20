import turtle

turtle.shape('turtle')

def figure(step, angle):
    for x in range(40):
        if x > 0:
            turtle.pendown()  # Pen down for draw
            turtle.forward(step)  # Step
            turtle.right(angle)  # Turn left on 90 angle
            x -= 1
        else:
            pass

figure(10,5)