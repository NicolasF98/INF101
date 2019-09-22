import random

play = "o"
cmpt_part = 0
win = 0 
es = 0
rep = "z"


while play != "n":
        cmpt_part += 1
        a = 0
        b = 100
        y = -1
        i = 0
        rep = random.randint(0,100)
        nbr = int(input("Combien veux-tu d'essais ?"))
        while (rep != "b" and nbr != i):
                print("Je cherche un nombre entre",a," et",b,"(",nbr-i,"essais )")
                y = (b+a)//2
                print(y)
                if rep < y :
                        print("p")
                        b = y-1
                elif rep > y:
                        print("g")
                        a = y+1
                elif rep == y:
                        print("b")
                        rep = "b"
                i=i+1
        es = i + es
        if rep == "b":
                print("Gagné")
                win+=1
        else:
                print("Perdu")
        print("L'IA a gagné",win,"partis sur",cmpt_part)
        print("L'IA a mis en moyenne", nbr/cmpt_part,"essais pour gagner")

        while (rep != "b" and nbr != i):
                print("Je cherche un nombre entre",a," et",b,"(",nbr-i,"essais )")
                y = (b+a)//2
                print(y)
                if rep < y :
                        print("p")
                        b = y-1 
                elif rep > y:
                        print("g")
                        a = y+1
                elif rep == y:
                        print("b")
                        rep = "b"
                i=i+1
        es = i + es
        if rep == "b":
                print("Gagné")
                win+=1
        else:
                print("Perdu")
        print("L'IA a gagné",win,"partis sur",cmpt_part)
        print("L'IA a mis en moyenne", nbr/cmpt_part,"essais pour gagner")
        play = input("Voulez-vous recommencez ? (o/n)\n") 



x = int(input())
y = random.randint(0,100)
