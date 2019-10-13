def minimum(liste):
    ret = liste[0]
    i = 1
    while (i < len(liste)):
        if (liste[i] < ret):
            ret = liste[i]
        i += 1
    return ret

def contient(liste, elem):
    i = 0
    ret = False
    while (i < len(liste)):
        if (elem == liste[i]):
            ret = True
        i += 1
    return ret

def minimum2(liste):
    liste.remove(minimum(liste))
    return minimum(liste)
    #faut il remove uniquement 1 valeur de la liste ou toutes les répétitions de la valeur ?

def temperature(liste):
    posi = [] #liste des valeurs positives et nulle de notre liste d'origine
    nega = [] #liste des valeurs negatives

    if (len(liste)==0):
        return 0

    i = 0
    while (i < len(liste)):
        if (liste[i] < 0):
            nega.append(liste[i])
        else:
            posi.append(liste[i])
        i += 1
    if (minimum(posi)< -(minimum(nega))):
        ret = nega[0]
        i = 1
        while (i < len(nega)):
            if (nega[i] >= ret):
                ret = nega[i]
            i += 1
        return ret
    else:
        return minimum(posi)
    


liste = [66,12,42,-100,-7,-0]
print(temperature(liste))