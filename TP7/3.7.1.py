def swapPositions(list, pos1, pos2): 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)
    return list

def tri_insertion(liste):
    new = []
    min = liste[0]
    i_rm = 0
    i = 0
    while (len(liste) != 0):
        while (i < len(liste)):
            if (liste[i] < min):
                min = liste[i]
                i_rm = i
            i += 1
        new.append(min)
        liste.pop(i_rm)
        if (len(liste) != 0):
            min = liste[0]
        i_rm = 0
        i = 0
    return new

liste = [10,9,1,1,2,7]
print(tri_insertion(liste))

def tri_selection(liste):
    i = 1
    while (i < (len(liste)) - 1):
        if (liste[i] > liste[i+1]):
            swapPositions(liste,i,i+1)
            i = -1
        i += 1
    return liste

#liste = [10,9,1,1,2,7]
#print(tri_selection(liste))




