
def capital(nb_annees, capital_debut):
    i = 0
    while(nb_annees != i):
        capital_debut = capital_debut * 1.05 - 11
        i += 1
    return capital_debut

def gagne_argent(nb_annees, capital_debut):
    if (capital(nb_annees, capital_debut) >= capital_debut):
        return True
    else:
        return False

def placement_min(nb_annees, but):
    i = 10.45
    while (capital(nb_annees, i) <= but):
        i += 0.001
    return i

def duree_min(capital, but):
    i = 0
    if capital <= 220:
        return "Valeur trop petite"
    else:
        while(but >= capital):
            capital = (capital * 1.05) - 11
            i += 1
        return (i)

def est_premier(nb):
	i = 2
	if (nb <= 0):
		return (0)
	while (i < nb and (nb % i != 0)):
		i += 1
	if (i == nb):
		return True
	else:
		return False

print(est_premier(1000))

def plus_grand_diviseur_premier(n):
    i = 0
    pgdp = 0
    if (est_premier(n) == True):
        return n
    else:
        while (i != n):
            if (est_premier(i) == True):
                if (n % i == 0):
                    pgdp = i
            i += 1
    return pgdp

def pgcd(a,b):
    if (a > b):
        resu = a
        while resu != 0:
            resu = 

