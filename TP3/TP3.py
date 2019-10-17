import turtle

turtle.shape('turtle')
ligne = 0

turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.speed('fastest')

while (ligne != 4):
    turtle.up()
    turtle.goto(-200,200-(60*ligne))
    turtle.down()
    nbr = 0

    while nbr != 4:
        turtle.up()
        turtle.forward(60)
        turtle.down()
        i_carrer = 0
        i_triangle = 0

        while (i_carrer != 4):
            turtle.forward(50)
            turtle.right(90)
            i_carrer += 1

        turtle.up()
        turtle.forward(60)
        turtle.down()

        while (i_triangle != 3):
            turtle.forward(50)
            turtle.right(120)
            i_triangle += 1
        nbr += 1
    ligne += 1