import random

fr = {"salut":"hey", "tu":"you", "il":"he", "bien":"great"}

def traduire(dico, mot):
    return dico[mot]

def jouerUnMot(dico):
    cpt = 0
    val = random.randint(0, len(dico)-1)
    for i in dico:
        if (cpt == val):
            index = i
        cpt += 1    
    print(index)

def main():
    rep = "non"
    mot = "salut"
    tours, win = 0,0
    rejou = "o"
    fr = {"salut":"hey", "tu":"you", "il":"he", "bien":"great"}
    while (rejou == "o"):
        while (traduire(fr, mot) != rep):
            fr = {"salut":"hey", "tu":"you", "il":"he", "bien":"great"}
            mot = jouerUnMot(fr)
            rep = input("Trad : ")
            tours += 1
        win += 1
        print("Tu as gg. \n Stats :",win/tours)
        rejou = input("Rejouer ? (o/n)")
main()