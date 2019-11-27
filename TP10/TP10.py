#3.10.1

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

#3.10.2

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

#def new(nbr_init, taux_nat_min, taux_nat_max, taux_mort_min, taux_mort_max, t):
 #   combi_total=[[]]
  #  toto = 0
   # nv = 10*(taux_nat_max-taux_nat_min) * 10*(taux_mort_max-taux_mort_min)
    
   # for i in range[taux_nat_min, taux_nat_max, 0.1]:
    #    for j in range[taux_mort_min, taux_mort_max, 0.1]:
     #       combi_total[].append(nouveau_nbr_poule_nat(nbr_init,i,t))
      #      combi_total[i*10].append(nouveau_nbr_poule_nat(nbr_init,i,t) - nouveau_nbr_poule_mort(nbr_init, i, j,t))
       #     combi_total[i*10].append(nouveau_nbr_poule_mort(nbr_init, i, j,t))

    #return combi_total
     
#print(new(100, 0.5, 1, 0.5, 1, 10))

# 3.10.3

def renard_poule(nbr_init_poule, nbr_init_renard, po1, po2, ren1, ren2, t):
    cpt = 0
    simulation = [[]]
    while(cpt != t):
        nat_renards = ren1 * nbr_init_poule
        nbr_init_poule = nat_renards

        mort_renards = ren2 / nbr_init_poule
        nbr_init_poule = mort_renards

        mort_poules = po1 + po2*nbr_init_renard
        nbr_init_renard = mort_poules
        cpt += 1 
        simulation[cpt].append(nat_renards - mort_renards)
        simulation[cpt].append((nbr_init_poule - mort_poules))

    return simulation


print(renard_poule(50, 10, 3, 10, 3, 10, 10))