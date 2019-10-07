
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


