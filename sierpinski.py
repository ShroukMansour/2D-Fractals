import turtle

my_pen = turtle.Turtle()



def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2  # find midpoint


def sierpinski_triangle(points, depth):
    my_pen.up()
    my_pen.goto(points[0][0], points[0][1])
    my_pen.down()
    my_pen.goto(points[1][0], points[1][1])
    my_pen.goto(points[2][0], points[2][1])
    my_pen.goto(points[0][0], points[0][1])

    if depth > 0:
        my_pen.pencolor('red')
        sierpinski_triangle([points[0],
                             get_mid(points[0], points[1]),
                             get_mid(points[0], points[2])],
                            depth - 1)
        my_pen.pencolor('blue')
        sierpinski_triangle([points[1],
                             get_mid(points[0], points[1]),
                             get_mid(points[1], points[2])],
                            depth - 1)
        my_pen.pencolor('orange')
        sierpinski_triangle([points[2],
                             get_mid(points[2], points[1]),
                             get_mid(points[0], points[2])],
                            depth - 1)


def sierpinski_carpet(depth, box_size):
    if depth == 0: 
        my_pen.pencolor('black')
        my_pen.begin_fill()
        for _ in range (4):
            my_pen.forward(box_size)
            my_pen.left(90)
        my_pen.end_fill()
    else:
        for _ in range(4):
            # first rectangle
            sierpinski_carpet(depth - 1, box_size / 3)
            my_pen.forward(box_size / 3)
            # second rectangle
            sierpinski_carpet(depth - 1, box_size / 3)
            my_pen.forward(box_size / 3)
            # go to next corner
            my_pen.forward(box_size / 3)
            my_pen.left(90)
        turtle.Screen().update()


my_pen.penup()
my_pen.goto(-200,-200)
turtle.Screen().tracer(0)
sierpinski_carpet(3, 400)
my_pen.ht()
my_pen.speed(5)
my_pen.pencolor('orange')
sierpinski_triangle([[-175, -125], [0, 175], [175, -125]], 1)
turtle.Screen()._root.mainloop()
