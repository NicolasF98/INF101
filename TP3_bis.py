import turtle

turtle.shape('turtle')

turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.speed('slowest')

nbr = 0

val = int(input("Combien veux-tu de figures ?"))

while nbr != val:
    turtle.up()
    turtle.forward(60)
    turtle.down()
    
    i_carrer = 0
    i_triangle = 0

    def carre(longueur):
        while (i_carrer != 4):
            turtle.forward(longueur)
            turtle.right(90)
            i_carrer += 1
    
    def triangle(longueur):
        while (i_triangle != 3):
            turtle.forward(longueur)
            turtle.right(120)
            i_triangle += 1
    nbr += 1
