Fournout Nicolas - IMA9



# TP8 : Propagation d'une nouvelle:

## 3.8.1:
On sait que:
- Au debut de l'experience, seule la personne numéro 1 est dans le status `C`.
- Ordre de propagation d'une personne est: `I -> C -> M`.
- Si aucune personne du couple n'est dans le status `C`, alors le status des deux personnes ne change pas.

## 3.8.3:

### Ex1:

```py
def init(n):                  
    i = 1                                        
    liste = []               
    #initialisation d'une liste contenant n-1 "I" et 1 "C"   
    liste.append("C")               
    while(i <= n):                  
        liste.append("I")           
        i += 1
    return liste

def jours(liste):
    l = init(n)
    i,jours = 0,0   

    while ((l.count("C") != 0)):
        i = 0
        liste_index = []
        #cette liste va contenir les index de nos couples
        maxi = len(l)
        liste_index_to = list(range(0,maxi)) 
        #creation d'une liste qui contient tous les index

        while(i != 2):
            liste_index.append(liste_index_to[random.randint(0,maxi-1)]) 
            i += 1

        while (liste_index[0] == liste_index[1]): 
        #si nos index sont identiques, alors on refait un tirage jusqu'a qu'ils 
        #soient different.
            liste_index = [] 
            i = 0
            while(i != 2):
                liste_index.append(liste_index_to[random.randint(0,maxi-1)])
                i += 1

        if (l[liste_index[0]] == "C" and l[liste_index[1]] == "I"):
            l[liste_index[1]] = "C"

        elif (l[liste_index[0]] == "I" and l[liste_index[1]] == "C"):
            l[liste_index[0]] = "C"
            
        elif (((l[liste_index[0]] == "C") or (l[liste_index[0]] == "M")) and 
        ((l[liste_index[1]] == "C") or (l[liste_index[1]] == "M"))):
            l[liste_index[0]] = "M"
            l[liste_index[1]] = "M"
        jours += 1

        print(l)
        print(liste_index)
        print(l[liste_index[0]])
        print(l[liste_index[1]])
        print(jours)

jours(init(n))
```
### Ex2:

```py
import random

n = int(input("Nbr de personne : "))

def init(n):                  
    i = 1                                        
    liste = []                
    #initialisation d'une liste contenant n-1 "I" et 1 "C"      
    liste.append("C")               
    while(i <= n):                  
        liste.append("I")           
        i += 1
    return liste

def jours(liste):
    l = init(n)
    i,jours = 0,0   

    while ((l.count("C") != 0)):
        i = 0
        liste_index = [] 
        # cette liste va contenir les index de nos couples
        maxi = len(l)
        liste_index_to = list(range(0,maxi)) 
        # creation d'une liste qui contient tous les index

        while(i != 2):
            liste_index.append(liste_index_to[random.randint(0,maxi-1)]) 
            i += 1

        while (liste_index[0] == liste_index[1]):
        #si nos index sont identiques, alors on refait un tirage jusqu'a qu'ils 
        #soient different.
            liste_index = [] 
            i = 0
            while(i != 2):
                liste_index.append(liste_index_to[random.randint(0,maxi-1)])
                i += 1

        if (l[liste_index[0]] == "C" and l[liste_index[1]] == "I"):
            l[liste_index[1]] = "C"

        elif (l[liste_index[0]] == "I" and l[liste_index[1]] == "C"):
            l[liste_index[0]] = "C"
            
        elif (((l[liste_index[0]] == "C") or (l[liste_index[0]] == "M")) and 
        ((l[liste_index[1]] == "C") or (l[liste_index[1]] == "M"))):
            l[liste_index[0]] = "M"
            l[liste_index[1]] = "M"
        jours += 1
    
    print(l)
        

jours(init(n))
```

## Ex3:

```py
import random

n = int(input("Nbr de personne : "))
ns = int(input("Nbr de simulation successives : "))

def init(n):                  
    i = 1                                        
    liste = []                
    #initialisation d'une liste contenant n-1 "I" et 1 "C"      
    liste.append("C")               
    while(i <= n):                  
        liste.append("I")           
        i += 1
    return liste

def jours(l, ns):
    i,jours = 0,0  
    val_i,val_j = 0,0
    n = 1
    while (n <= ns):                 
        #boucle des ns simulations
        while ((l.count("C") != 0)):
            i = 0
            liste_index = [] 
            # cette liste va contenir les index de nos couples
            maxi = len(l)
            liste_index_to = list(range(0,maxi)) 
            # creation d'une liste qui contient tous les index

            while(i != 2):
                liste_index.append(liste_index_to[random.randint(0,maxi-1)]) 
                i += 1

            while (liste_index[0] == liste_index[1]): 
            #si nos index sont identiques, alors on refait un tirage jusqu'a qu'ils 
            #soient different.
                liste_index = [] 
                i = 0
                while(i != 2):
                    liste_index.append(liste_index_to[random.randint(0,maxi-1)])
                    i += 1

            if (l[liste_index[0]] == "C" and l[liste_index[1]] == "I"):
                l[liste_index[1]] = "C"

            elif (l[liste_index[0]] == "I" and l[liste_index[1]] == "C"):
                l[liste_index[0]] = "C"
                
            elif (((l[liste_index[0]] == "C") or (l[liste_index[0]] == "M")) and 
            ((l[liste_index[1]] == "C") or (l[liste_index[1]] == "M"))):
                l[liste_index[0]] = "M"
                l[liste_index[1]] = "M"
            jours += 1
        n += 1

        #parti des calculs de moyennes
        val_j += jours       
        moy_j = val_j/n
        val_i += l.count("I")
        moy_i = val_i/n

    print("Moyenne jours: ",moy_j)
    print("Moyenne ignorant: ",moy_i)
        

jours(init(n),ns)
```


