import turtle


def draw_u():
    udacity = turtle.Turtle()

    udacity.speed(3)
    
    udacity.shape("turtle")
    udacity.color("yellow")
    
#letter U
    udacity.pu()
    udacity.setx(-300)
    udacity.pd()
    udacity.left(90)
    udacity.backward(100)
    udacity.right(90)
    udacity.fd(40)
    udacity.left(90)
    udacity.fd(100)

    udacity.right(90)
    udacity.pu()
    udacity.fd(10)
    udacity.pd()

    for i in range(1,181):
        udacity.fd(1)
        udacity.right(1)
    
    udacity.pu()
    udacity.righ(180)
    udacity.fd(60)
    udacity.pd()
    udacity.left(90)
    udacity.fd(100)
    
    
    udacity.setx(+30)
    udacity.pd()
    udacity.righ(90)
    udacity.fd(100)
    udacity.righ(90)
    udacity.fd(30)
    udacity.righ(90)
    udacity.fd(100)
    

window = turtle.Screen()
window.bgcolor("black")

draw_u()
