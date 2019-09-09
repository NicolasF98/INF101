er = 0
note = 0
total = 0
i = 0
while i!=4 and er == 0:
    note = int(input())
    if note>=0 and note<=20:
        total = total + note
    else:
        er = 1
    i+=1
moyenne = total/4
if er==1:
    print("Incorrecte")
else:
    print("La moyenne est de:",moyenne)