import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for x in xrange(4):
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("pink")
    angie.circle(50)
    
    window.exitinclick()

draw_square()
