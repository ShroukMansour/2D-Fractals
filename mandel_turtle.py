import turtle

class Mandelbrot:
    def __init__(self, c, limit=50):
        self.__limit = int(limit)
        self.__colormap = ['black','white']
        self.__cardinality = limit
        z = 0
        for i in range(limit):
            z = z * z + c
            if abs(z) > 2:
                self.__cardinality = i
                return

    def getColor(self):
        if self.__cardinality == self.__limit:
            return self.__colormap[0]
        return self.__colormap[1]

def turtleConvert(x,y): #converts from turtle pixels to the complex plane
    return complex((x/300)*4,(y/300)*4)

class Display:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.ht();self.t.turtlesize(1)
        self.t.speed(0)
        turtle.Screen().tracer(2000,0)
        for x in range(-150,151):
            for y in range(-150,151):
                self.t.color(Mandelbrot(turtleConvert(x,y)).getColor())
                self.t.goto(x,y)
            self.t.up()
            self.t.goto(x + 1, -150)
            self.t.down()



d = Display()