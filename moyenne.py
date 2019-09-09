er = 0
note = 0
total = 0
i = 0
while i!=4 and er==0 or er==1:
    note = int(input())
    if note>=0 and note<=20:
        total = total + note
    else:
        er+=1
        note = int(input())
        total = total + note
    i+=1
moyenne = total/4
if er==2:
    print("Incorrecte")
else:
    print("La moyenne est de:",moyenne)

if moyenne < 10:
    print("Ajournee")
elif moyenne >= 10 and moyenne < 12:
    print("Passable")
elif moyenne >= 12 and moyenne < 14:
    print("Assez bien")
elif moyenne >= 14 and moyenne < 16:
    print("Bien")
elif moyenne >= 16:
    print("Tres bien")