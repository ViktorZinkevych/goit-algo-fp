import turtle
import math


screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Фрактал: Дерево Піфагора")


t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Функція побудови дерева
def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.begin_fill()
        for _ in range(4):  
            t.forward(length)
            t.left(90)
        t.end_fill()
        return

    
    t.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

    
    t.forward(length)
    t.left(45)

    # Вирахування нової довжини
    new_length = length / math.sqrt(2)

    draw_pythagoras_tree(t, new_length, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, new_length, level - 1)

    t.left(45)
    t.backward(length)


t.up()
t.goto(-50, -200)
t.down()
t.color("green", "lightgreen")


recursion_level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
draw_pythagoras_tree(t, 100, recursion_level)

turtle.done()