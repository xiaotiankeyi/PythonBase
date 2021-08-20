import turtle
from time import sleep


class MyRectangle(object):

    def __init__(self, x=0, y=0, width=100, height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        """计算矩形面积"""
        return self.width * self.height

    @property
    def getPerimeter(self):
        """计算周长"""
        return 2 * (self.height + self.width)

    def draw(self):
        """海龟绘图"""
        pen = turtle.Pen()
        pen.color("red")
        pen.width(5)
        pen.goto(self.x, self.y)
        pen.forward(self.height)
        pen.left(90)
        pen.forward(self.width)
        pen.left(90)
        pen.forward(self.height)
        pen.left(90)
        pen.forward(self.width)


def function():
    pen = turtle.Pen()
    pen.width(8)
    color_list = ['purple', 'red', 'blue', 'black', 'orange']
    Y = 0
    d = 0
    for i in range(10, 100, 20):
        pen.penup()
        pen.goto(0, Y)
        pen.pendown()
        pen.pencolor(color_list[d])
        pen.circle(i)
        Y += -20
        d += 1
        sleep(1)

    sleep(5)


def can():
    pen = turtle.Pen()
    pen.pencolor('red')
    pen.width(2)
    pen.penup()
    pen.setx(-200)
    pen.sety(200)
    pen.pendown()

    for i in range(200, -160, -20):
        pen.penup()
        pen.goto(-200, i)
        pen.pendown()
        pen.forward(340)

    pen.right(90)
    pen.pencolor('blue')
    for i in range(-200, 160, 20):
        pen.penup()
        pen.goto(i, 200)
        pen.pendown()
        pen.forward(340)
        sleep(0.5)

    sleep(5)


def score(val):
    if 0 < val < 100 and val is not int:
        if 90 < val:
            print('A')
        elif 80 < val:
            print("B")
        elif 70 < val:
            print('C')
        elif 60 < val:
            print('D')
        else:
            print('E')
    else:
        print('不符合')




class Computer(object):

    def calculatte(self):
        pass




if __name__ == "__main__":
    pass
    # obj = MyRectangle(width=100, height=200)
    # print('面积是:', obj.getArea())
    # print('周长是:', obj.getPerimeter)
    # obj.draw()
    # sleep(3)
    # function()
    # can()
    # score(93)
