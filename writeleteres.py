import turtle


def draw_u():
<<<<<<< HEAD
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
=======
    myu = turtle.Turtle()
    myu.shape("turtle")
    myu.color("yellow")
    myu.left(90)
    myu.backward(100)
    myu.setx(+30)
    myu.fd(100)
    myu.right(90)
    
    myu.pu()
    myu.setx(+30)
    myu.pd()
    for i in range(1,181):
        myu.fd(1)
        myu.right(1)

    myu.pu()
    myu.setx(+30)
    myu.pd()
    myu.righ(90)
    myu.fd(100)
    myu.righ(90)
    myu.fd(30)
    myu.righ(90)
    myu.fd(100)
>>>>>>> origin/master
    

window = turtle.Screen()
window.bgcolor("black")

<<<<<<< HEAD
=======

>>>>>>> origin/master
draw_u()
