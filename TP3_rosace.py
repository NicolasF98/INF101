import turtle

turtle.speed("fastest")
x = -200
y = 200
nb = 8
r = 50
ligne, col = 1, 1

def reset(i):
    turtle.up()
    turtle.forward(50+(10*i))
    turtle.down()

def rosace(x, y, nb, r):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    i = 1
    angle = 360 / nb
    while (i != nb+1):
        turtle.circle(r)
        turtle.right(angle * i)
        i += 1


while(col != 4):
    rosace(x,y,nb,r)
    col += 1
col = 1
x = x + ((50*col) + 15)
y = y + ((50*col) + 15)
ligne += 1
