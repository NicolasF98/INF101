import turtle

def reset():
    turtle.up()
    turtle.forward(10)
    turtle.down()

def carre(longueur):
    i_carrer = 0
    while (i_carrer != 4):
        turtle.forward(longueur)
        turtle.right(90)
        i_carrer += 1
    turtle.forward(longueur)

def triangle(longueur):
    i_triangle = 0 
    while (i_triangle != 3):
        turtle.forward(longueur)
        turtle.right(120)
        i_triangle += 1
    turtle.forward(longueur)

val = int(input("Combien veux-tu de figures ?"))
nbr = 0

while (nbr != val):
    carre(45+(15*nbr))
    reset()
    nbr += 1
    triangle(45+(15*nbr))
    reset()
    nbr += 1