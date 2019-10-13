import turtle
import math

def carre(n):
    i = 0
    while (i != 4):
        turtle.forward(n)
        turtle.right(90)
        i += 1

def carres_imbriques(cote,nb):
    j = 1
    while(j != nb+1):
        cote = cote*2/3
        carre(cote)
        j += 1

def aller_sans_tracer(x, y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

def descendre_sans_tracer(n):
    turtle.right(90)
    turtle.up()
    turtle.forward(n)
    turtle.down()
    turtle.left(90)

def polygone(nb_cotes,cotes):
    i = 0
    if nb_cotes >= 3:
        while(i != nb_cotes):
            turtle.forward(cotes)
            turtle.right(360/nb_cotes)
            i += 1

def diametre_polygone(nb_cotes, cotes):
    return (cotes/(math.sin(math.pi/nb_cotes)))

def colonne_polygone(nb_poly, cote):
    i = 0
    nb_cotes = 3
    while (i < nb_poly):
        i += 1
        d = diametre_polygone(nb_cotes,cote)
        polygone(nb_cotes,cote)
        descendre_sans_tracer(d)
        descendre_sans_tracer(5)
        nb_cotes += 1

def pavage()