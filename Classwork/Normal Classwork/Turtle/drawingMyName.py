import turtle

# t = turtle.Turtle()
# for _ in range(4):
#     t.forward(100)
#     t.right(90)


t = turtle.Turtle()
# for _ in range(3):
#     t.forward(100)
#     t.right(120)

def drawM():
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.right(120)
    t.forward(100)

def drawA():
    t.left(45)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(180)
    t.penup()
    t.forward(50)
    t.left(60)
    t.pendown()
    t.forward(50)
    t.penup()
    t.right(180)
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.left(55)

def drawZ():
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.right(85)
    t.forward(100)
    t.right(140)
    t.forward(140)
    t.left(140)
    t.forward(100)

t.speed(10)

t.penup()
t.goto((-200, 0))
t.pendown()

drawM()

t.penup()
t.goto((-10, 0))
t.pendown()
t.left(75)

drawA()

t.penup()
t.goto((130, 0))
t.pendown()
t.left(20)

drawA()

t.penup()
t.goto(270, 0)
t.pendown()


drawZ()

t.hideturtle()

turtle.exitonclick()