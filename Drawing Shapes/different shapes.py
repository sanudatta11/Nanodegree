import turtle
def draw_square():

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    count = 0
    while (count <4):
        brad.forward(100)
        brad.right(90)
        count+=1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    tri = turtle.Turtle()
    tri.shape("arrow")
    tri.color("yellow")
    count = 0
    while count < 3:
        tri.bk(200)
        tri.left(120)
        count += 1
    
window = turtle.Screen()
window.bgcolor("red")
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()

