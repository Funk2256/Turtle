import turtle

turtle.shape('turtle')

i = 0
y = 4 # Счетчик для While
degree = 90 # Угол поворота в градусах
turtle.goto(0, 0)  # Позиция 0
turtle.forward(0)  # Черепашка ни куда не отправляется


def square_draw(y, i, a, *args):  # Цикл отвечающий за движение и поворот черепашки
    turtle.penup()  # поднимаем ручку
    turtle.goto(a)  # переходим на следующую позицию
    turtle.pendown()  # опускаем ручку
    print(a)
    while y > 0:
        turtle.forward(i)
        turtle.left(degree)
        y -= 1
    y = 4


square_draw(y, 10, (-10, -10))
square_draw(y, 30, (-20, -20))
square_draw(y, 50, (-30, -30))
square_draw(y, 70, (-40, -40))
square_draw(y, 90, (-50, -50))
square_draw(y, 110, (-60, -60))
square_draw(y, 130, (-70, -70))
