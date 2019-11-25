#3.10.1

def nouveau_nbr_poule(nbr_init, taux, t):
    cpt = 0
    #On boucle autant que le nombre d'année
    while (cpt != t):
        #On applique la formule donnée par le TP
        nbr_final = (nbr_init + (nbr_init*taux))
        nbr_init = nbr_final
        #On incrémente notre compteur
        cpt += 1
    return nbr_final

print(nouveau_nbr_poule(10, 0.1, 10))



