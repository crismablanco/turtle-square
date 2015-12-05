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
    udacity.rt(90)
    #U
    udacity.circle(50,180)

    udacity.pu()
    udacity.bk(75)
    udacity.rt(90)
    udacity.pd()

    #D
    udacity.circle(50,180)

    udacity.pu()
    udacity.lt(90)
    udacity.fd(75)
    udacity.lt(90)
    udacity.fd(150)
    udacity.lt(90)
    udacity.pd()
    
    #A
    udacity.circle(50,180)

    udacity.pu()
    udacity.lt(180)
    udacity.fd(75)
    udacity.rt(90)
    udacity.fd(150)
    udacity.rt(180)
    udacity.pd()

    #C
    udacity.circle(50,180)

    udacity.pu()
    udacity.fd(20)
    udacity.lt(90)
    udacity.pd()

    #i
    udacity.fd(70)
    udacity.pu()
    udacity.fd(15)
    udacity.rt(90)
    udacity.fd(7)
    udacity.lt(90)
    udacity.pd()
    #udacity.fd(10)
    udacity.circle(10)

    udacity.pu()
    udacity.rt(90)
    udacity.fd(10)
    udacity.pd()
    
    #t
    udacity.fd(100)
    udacity.bk(50)
    udacity.rt(90)
    udacity.fd(90)

    udacity.pu()
    udacity.lt(90)
    udacity.fd(25)
    udacity.lt(45)
    udacity.pd()

    #y
    udacity.fd(110)
    udacity.bk(40)
    udacity.lt(90)
    udacity.fd(40)

    udacity.pu()
    udacity.lt(53)
    udacity.fd(235)
    udacity.pd()

    udacity.circle(10)

    
    udacity.rt(110)
    udacity.pu()
    udacity.fd(100)
    
    
    

window = turtle.Screen()
window.bgcolor("black")

draw_u()
