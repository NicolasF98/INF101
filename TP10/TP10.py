#3.10.1

def nbr_poule_nat(nbr_init, taux, t):
    cpt = 0
    #On boucle autant que le nombre d'année
    while (cpt != t):
        #On applique la formule donnée par le TP
        nbr_final = (nbr_init + (nbr_init*taux))
        nbr_init = nbr_final
        #On incrémente notre compteur
        cpt += 1
    return nbr_final

print(nbr_poule_nat(10, 0.1, 10))

#3.10.2

def nbr_poule(nbr_init, taux_nat, taux_mort, t):
    cpt = 0
    #On boucle autant que le nombre d'année
    while (cpt != t):
        #On applique la formule donnée par le TP
        nbr_final = (nbr_init + ((nbr_init*taux_nat) - (taux_mort*nbr_init))) 
        nbr_init = nbr_final
        #On incrémente notre compteur
        cpt += 1
    return nbr_final

print(nbr_poule(10, 0.9, 0.4, 10))

def simulation(nbr_init, taux_nat_min, taux_nat_max, taux_mort_min, taux_mort_max,  t):
    #liste qui va contenir toutes nos simulations
    simulations = []

    #initialisation d'une variable taux_nat et mort qui vont nous servir de compteur dans nos boucles
    taux_nat = taux_nat_min
    taux_mort = taux_mort_min

    #avec des deux boucles nous allons pouvoir simuler toutes les possibilités possibles
    while (taux_nat <= taux_nat_max):
        while (taux_mort <= taux_mort_max):

            #creation des variables comme demandé dans l'ennoncé
            nat_poules = nbr_poule_nat(nbr_init, taux_nat, t)
            mort_poules = nbr_poule_nat(nbr_init, taux_nat, t) - nbr_poule(nbr_init, taux_nat, taux_mort, t)
            pop_total = nbr_poule(nbr_init, taux_nat, taux_mort, t)

            #ajout de notre simulation sous forme de liste dans notre liste originel qui contient
            #l'ensemble de nos simulations
            simulations.append([nat_poules, mort_poules, pop_total])

            #on incrémente notre taux de mort de 0.1
            taux_mort += 0.1

        #ici on re-initialise notre taux_mort à sa valeur minimal pour pouvoir entrer à nouveau
        #dans notre 2eme boucle while, et on incrémente notre taux de nat de 0.1 
        taux_mort = taux_mort_min
        taux_nat += 0.1
    
    return simulations

print(simulation(100, 0.1, 1, 0.1, 1, 10))

# 3.10.3

def renard_poule(nbr_init_poule, nbr_init_renard, po1, po2, ren1, ren2, t):
    cpt = 0
    simulation = list(range(0,t))

    while(cpt != t):
        nat_renards = ren1 * nbr_init_poule
        nbr_init_poule = nat_renards

        mort_renards = ren2 / nbr_init_poule
        nbr_init_poule = mort_renards

        mort_poules = po1 + po2*nbr_init_renard
        nbr_init_renard = mort_poules
        simulation[cpt] = [cpt, nat_renards - mort_renards, nbr_init_poule - mort_poules]
        cpt += 1 

    return simulation


#print(renard_poule(50, 10, 3, 10, 3, 10, 10))