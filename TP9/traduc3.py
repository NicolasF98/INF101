fr = {"salut":"hey", "tu":"you", "il":"he", "bien":"great"}

def init_scores():
    i = 0
    dico = {}
    nbr = int(input("Combien de joueurs total ? "))
    while(i < nbr):
        nom = input("Nom du joueur ? ")
        dico[nom] = ""
        i += 1
    return dico

init_scores()

def jeu(dico_scores, dico):
    i = 0
    nbr_tours = int(input("Combien de mot faut-il deviner ? "))
    while( i != nbr_tours ):
        for j in dico:
            index = j
