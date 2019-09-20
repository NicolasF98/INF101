import random

play = "o"
cmpt_part = 1
win_random = 0
win_smart = 0 
rep = "z"
save_rep = rep
val = 1

while val != 100:
        a = 0
        b = 100
        i = 0
        i2 = 0
        rep = "z"
        nbr = int(input("Combien veux-tu d'essais ?"))
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
                win_random += 1
        else:
                print("Perdu")
        rep = save_rep
        print("L'IA aleatoire a gagné",win_random,"partis sur",cmpt_part)
        print("L'IA aleatoire a mis en moyenne", i/cmpt_part,"essais pour gagner")

        i = 0
        a = 0
        b = 100
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
                win_smart +=1
        else:
                print("Perdu")
        print("L'IA intelligente a gagné",win_smart,"partis sur",cmpt_part)
        print("L'IA int a mis en moyenne", i/cmpt_part,"essais pour gagner")
        val += 1
        cmpt_part += 1


