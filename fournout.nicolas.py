#Travail de Nicolas FOURNOUT et Gabriel CHOMBART du groupe IMA-9

import random

cmpt_part = 1 #compteur de parti total
win_random, win_smart, val = 0, 0, 0 #compteur de victoir pour chaque IA, val correspond à la valeur que nous allons essayer de trouver, elle est initialisé à 0

while val != 100:
        a, i = 0, 0  #a correspond à la borne inférieur de notre interval, i et i2 sont les compteurs respectif de l'IA_ aléatoire et l'IA_intelligente
        b = 100 #b est la borne supérieur de notre interval
        rep = "z"
        nbr = int(input("Combien veux-tu d'essais ? "))
        while (rep != "b" and nbr != i):
                print("Je cherche un nombre entre",a," et",b,"(",nbr-i,"essais )")
                y = random.randint(a,b) #nombre aléatoire proposé par l'IA
                print(y)
                if val < y :
                        print("p")
                        b = y-1
                elif val > y:
                        print("g")
                        a = y+1
                elif val == y:
                        print("b")
                        rep = "b"
                i += 1
        if rep == "b":
                print("Gagné")
                print("[",val,"]","*"*i)
                win_random += 1
        else:
                print("Perdu")
        print("L'IA aleatoire a gagné",win_random,"partis sur",cmpt_part)
        print("L'IA aleatoire a mis en moyenne", i/cmpt_part,"essais pour gagner")

        i, a = 0, 0 #on re-initialise nos compteurs
        b = 100
        rep = "z"

        while (rep != "b" and nbr != i):
                print("Je cherche un nombre entre",a," et",b,"(",nbr-i,"essais )")
                y = (b+a)//2
                if a == b:
                        print(a)
                        print("b")
                        rep = "b"
                else:
                        print(y)
                        if val < y:
                                print("p")
                                b = y-1
                        elif val > y:
                                print("g")
                                a = y+1
                        elif val == y:
                                print("b")
                                rep = "b"
                i=i+1
        if rep == "b":
                print("Gagné")
                print("[",val,"]","-"*i)
                win_smart +=1
        else:
                print("Perdu")
        print("L'IA intelligente a gagné",win_smart,"partis sur",cmpt_part)
        print("L'IA int a mis en moyenne", i/cmpt_part,"essais pour gagner")
        val += 1
        cmpt_part += 1


