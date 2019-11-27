import random

def init():
    i = 0
    new = []
    x = range(100,10000)
    while i < 365:
        y = random.randint(0, len(x))
        new.append(y/100)
        i += 1
    return new

# print(init())

def moyenne_j(liste, j):
    moy = 0
    div = 0
    for i in liste:
        if ( i%j ==0):
            moy += i
            div += 1
    return moy/div

print(moyenne_j(init(),2))

