# Fournout Nicolas IMA-9    Extra TP6 3.2.6

#programme 1
#ce programme va demander a l'utilisateur de fourni des nombres strictement positives non nulle et les ajoute dans une liste, il renvera la liste quand l'utilisateur donnera la valeur 0

def rempli_liste_entier():
    val = -1  #on donne une valeur a val afin de rentrer dans la boucle while
    liste = [] #creation d'une liste vide, qu'on remplira ulterieurement 
    while (val != 0):
        val = float(input("Entre un nombre positif, tape 0 pour stoper la saisie : "))
        while (val < 0): #si la valeur est négative on va demander a l'utilisateur de redonner une valeur jusqu'a quelle soit nulle ou positive
            val = float(input("Valeur invalide ! \nEntre un nombre positif, tape 0 pour stoper la saisie : "))
        if (val > 0): #si la valeur est positive et non nulle, on l'ajoute dans notre liste
            liste.append(val) 
    return liste

print(rempli_liste_entier())

#programme 2
#ce programme inverse l'ordre des valeurs d'une liste

def inverse_liste(liste):
    i = 0
    new_liste = []
    while (i < len(liste)): #on va boucler jusqu'a la fin de notre liste
        new_liste.append(liste[len(liste)-1-i]) #on ajoute à notre nouvelle liste la dernière valeur de l'ancienne liste, on enleve 1 car len(liste) nous donne 4, hors un liste commence par 0, il faut donc soustraire 1
        i += 1
    return new_liste

liste = ['a', 'b', 'c', 'd', 'e']
print(inverse_liste(liste))