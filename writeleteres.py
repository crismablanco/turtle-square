import turtle


def draw_u():
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
    

window = turtle.Screen()
window.bgcolor("black")


draw_u()
