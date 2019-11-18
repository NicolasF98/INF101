def ajouteMot(dico, mot, word):
    dico[mot] = word

def supprimeMot(dico, mot):
    del dico[mot]

def afficheDico(dico):
    for i in dico:
        print(i,"=",dico[i])

def afficheDicoLettre(dico, lettre):
    for i in dico:
        if  lettre in dico[i][0]:
            print(dico[i])

def afficheDicoLettre2(dico, long):
    for i in dico:
        if  (long == len(dico[i])):
            print(dico[i])

def main():
    fr = {"salut":"hey", "tu":"you", "il":"he", "bien":"great"}
    fran = input("Donnes un mot en Francais: ")
    angl = input("Quelle est sa traduction en Anglais ? ")
    ajouteMot(fr, fran, angl)
    afficheDico(fr)
    del_fran = input("Quelle mot souhaites-tu supprimer ? ")
    supprimeMot(fr, del_fran)
    afficheDico(fr)
main()