# TP4
# Exercice 1
# Programme 2
def distance(xA,yA,xB,yB):
    # renvoie la distance entre (xA,yA) et (xB,yB)
    d=(xB-xA)**2+(yB-yA)**2
    d=d**(1/2)
    return d

def appartient_cercle(xA,yA,rayon):
    # teste si le point (xA,yA) appartient
    # au cercle de rayon r centré à l'origine
    if distance(0,0,xA,yA)==rayon:
        return True
    else:
        return False

# prog. principal
d=distance(1,2,2,1)
print(d)
rep=appartient_cercle(1,1,2)
print(rep)
print(appartient_cercle(1,0,1))
