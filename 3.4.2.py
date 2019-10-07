import math

def valeur_abs(x):
    if (x >= 0):
        return x
    else:
        return -x 

def signe_different(x, y):
    if (x > 0 and y > 0):
        return True
    elif (x < 0 and y < 0):
        return True
    elif (x == 0 or y == 0):
        return False
    else:
        return False

def f(x):
    return 3 * x**2 + 2*x + 3

def nb_racine(a, b, c):
    discri = b**2 - 4*a*c
    if discri < 0:
        return 
    elif discri > 0:
        x1 = (-b + math.sqrt(discri)) / 2*a
        x2 = (-b - math.sqrt(discri)) / 2*a
        return x1, x2
    elif discri == 0:
        x3 = -b/2*a
        return x3

def lundi(mot):
    i = 0
    while i != 2:
        print(mot,end='')
        print(" ",end='')
        i += 1

def mardi(mot):
    if len(mot)%2 == 0:
        i = 0
        while i != 6:
            print(mot,end='')
            print(" ",end='')
            i += 1
    else:
        i = 0
        while i != 3:
            print(mot,end='')
            print(",",end='')
            i += 1

def mercredi(mot):
    if len(mot)%2 == 0:
        return mot
    else:
        return "impaire"

def jeudi(mot):
    x = len(mot)%3
    return mot*x

def vendredi(mot):
    return mot

def transforme(mot,num_j):
    if num_j == 1:
        lundi(mot)
    elif num_j == 2:
        mardi(mot)
    elif num_j == 3:
        mercredi(mot)
    elif num_j == 4:
        jeudi(mot)
    elif num_j == 5:
        vendredi(mot)

