import random

cmpt_part = 1
win_random, win_smat, val = 0

while val != 100:
        a, i, i2 = 0
        b = 100
        rep = "z"
        nbr = int(input("Combien veux-tu d'essais ? "))
        while (rep != "b" and nbr != i):
                print("Je cherche un nombre entre",a," et",b,"(",nbr-i,"essais )")
                y = random.randint(a,b)
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

        i, a = 0
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


