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

#3.10.2

def nbr_poule(nbr_init, taux_nat, taux_mort, t):
    cpt = 0
    nbr_final = 0
    #On boucle autant que le nombre d'année
    while (cpt != t):
        #On applique la formule donnée par le TP
        nbr_final = (nbr_init + ((nbr_init*taux_nat) - (taux_mort*nbr_init))) 
        nbr_init = nbr_final
        #On incrémente notre compteur
        cpt += 1
    return nbr_final

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

# 3.10.3

def renard_poule(nbr_init_poule, nbr_init_renard, po1, po2, ren1, ren2, t):
    #creation d'un compteur 
    cpt = 0

    #creation de la liste qui va contenir toutes nos valeurs pour chaque pas de t
    simulations = []

    #boucle de 0 à t pour appliquer nos formule pour chaque pas de t
    while(cpt != t):

        #on applique les formules données par le tp
        nat_renards = ren1 * (nbr_init_poule - (po1 + po2)*cpt)
        mort_renards = ren2 / (nbr_init_poule - (po1 + po2)*cpt)
        mort_poules = po1 + po2 * nbr_poule(nbr_init_renard, nat_renards, mort_renards, cpt)

        #on ajoute notre liste de valeur à notre liste initiale
        simulations.append([cpt, nbr_init_poule - mort_poules, (nbr_init_renard + nat_renards) - mort_renards])

        #on incremete notre compteur
        cpt += 1 

    return simulations


def main():
    #demande de saisie de l'utilisateur
    po1 = float(input("Valeur de po1 (nbr poule morte naturellement / ans) : "))
    po2 = float(input("Valeur de po2 (nbr poule mangé par un renard / ans) : "))
    ren1 = float(input("Valeur de ren1 (coéf. nat des renards) : "))
    ren2 = float(input("Valeur de ren2 (coéf. mort des renards): "))

    #initialisation de notre compteur
    cpt = 0

    #t correspond à notre de pas maximal de temps
    t = 10

    #nombre initial de poule et de renard
    nbr_init_poule = 1000
    nbr_init_renard = 10

    #on boule pour appliquer notre forume pour chaque pas de t
    while(cpt != t):

        #applications des formules données dans le tp
        nat_renards = ren1 * (nbr_init_poule - (po1 + po2)*cpt)
        mort_renards = ren2 / (nbr_init_poule - (po1 + po2)*cpt)
        mort_poules = po1 + po2 * nbr_poule(nbr_init_renard, nat_renards, mort_renards, cpt)
        
        # incrementation de notre compteur
        cpt += 1 

        #affichage de nos valeurs
        print("Nombre de poule : ", nbr_init_poule - mort_poules)
        print("Nombre de renard : ", (nbr_init_renard + nat_renards) - mort_renards )
        
#lanchement de notre main
main()