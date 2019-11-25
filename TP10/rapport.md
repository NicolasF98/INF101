- FOURNOUT Nicolas
- CHOMBART Gabriel

# Rapport TP 10:

## 3.10.1 - Natalité:
(1) Nous avons utilisé la formule donnée par le TP, et nous avons utilisé une boucle `while` afin d'appliquer le principe de temps.
```py
def nouveau_nbr_poule_nat(nbr_init, taux, t):
    cpt = 0
    #On boucle autant que le nombre d'année
    while (cpt != t):
        #On applique la formule donnée par le TP
        nbr_final = (nbr_init + (nbr_init*taux))
        nbr_init = nbr_final
        #On incrémente notre compteur
        cpt += 1
    return nbr_final

print(nouveau_nbr_poule_nat(10, 0.1, 10))
```

(2) Notre fonction est une fonction croissante linéaire.

(3) Si nous avons une ressource illimitée, notre population va tout le temps augementer.

## 3.10.2 - Mortalité:
(1) Nous avons utilisé le même algorithme que pour la partie `3.10.1` en changant uniquement la formule.
```py
def nouveau_nbr_poule_mort(nbr_init, taux_nat, taux_mort, t):
    cpt = 0
    #On boucle autant que le nombre d'année
    while (cpt != t):
        #On applique la formule donnée par le TP
        nbr_final = (nbr_init + ((nbr_init*taux_nat) - (taux_mort*nbr_init))) 
        nbr_init = nbr_final
        #On incrémente notre compteur
        cpt += 1
    return nbr_final

print(nouveau_nbr_poule_mort(10, 0.1,0.4, 10))
```

(2) 

## 3.10.3 - Renards:
(1) 