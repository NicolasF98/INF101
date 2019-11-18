import random

fr = {"salut":"hey", "tu":"you", "il":"he", "bien":"great"}

def traduire(dico, mot):
    return dico[mot]

def jouerUnMot(dico):
    cpt = 0
    val = random.randint(0, len(dico)-1)
    for i in dico:
        if (cpt == val):
            index = i
        cpt += 1    
    print(dico[index])
