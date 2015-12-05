import turtle


def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(1,37):
        for x in xrange(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("pink")
    angie.circle(50)

def draw_triangle():
    tritri = turtle.Turtle()
    tritri.color("white")
    tritri.shape("turtle")
    for x in xrange(3):
        tritri.forward(60)
        tritri.right(120)
    


window = turtle.Screen()
window.bgcolor("black")


draw_square()
draw_circle()
draw_triangle()
