import turtle
turtle.speed("fastest")
turtle.up()
turtle.goto(0,0)
turtle.down()

i = 0

while (i != 4):
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(40)
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    i += 1
