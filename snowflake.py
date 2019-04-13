import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

my_pen = turtle.Turtle()
my_pen.speed(0)

# Create a list of colors
sfcolor = [ "blue","blue", "#73bdec", "white"]


# Define a function to create different sized snowflakes
def snowflake(size):
    my_pen.penup()
    my_pen.forward(10 * size)
    my_pen.left(45)
    my_pen.pendown()
    my_pen.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for _ in range(8):
        branch(size)
        my_pen.left(45)


# This function creates one branch of the snowflake
def branch(size):
    for _ in range(3):
        for _ in range(3):
            my_pen.forward(10.0 * size / 3)
            my_pen.back(10.0 * size / 3)
            my_pen.right(45)
        my_pen.left(90)
        my_pen.back(10.0 * size / 3)
        my_pen.left(45)
    my_pen.right(90)
    my_pen.forward(10.0 * size)



for i in range(6):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sfsize = random.randint(1, 4)
    my_pen.penup()
    my_pen.goto(x, y)
    my_pen.pendown()
    snowflake(sfsize)


turtle.done()