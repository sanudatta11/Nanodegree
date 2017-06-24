import turtle
def draw_R(my_turtle):
        my_turtle.pd()
        my_turtle.circle(120, 180)
        my_turtle.home()
        my_turtle.sety(-200)
        my_turtle.home()
        my_turtle.setheading(300)
        my_turtle.fd(225)

def draw_S(last):
        last.right(300)
        last.pu()
        last.forward(200)
        last.pd()
        last.circle(110, 170)
        last.circle(-110, 170)

def draw_heart(hr):
        hr.color("red")
        hr.pu()
        hr.fillcolor("red")
        hr.bk(700)
        hr.setheading(90)
        hr.bk(100)
        hr.begin_fill()
        hr.pd()
        hr.circle(110, 210)
        hr.setheading(310)
        hr.fd(320)
        hr.setheading(51)
        hr.fd(300)
        hr.circle(110, 210)
        hr.end_fill()
        


        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    sam = turtle.Turtle()
    sam.color("blue")
    sam.shape("turtle")
    sam.speed(1)
    sam.pensize(10)
    draw_R(sam)
    draw_S(sam)
    draw_heart(sam)
    window.exitonclick()
draw_art()
