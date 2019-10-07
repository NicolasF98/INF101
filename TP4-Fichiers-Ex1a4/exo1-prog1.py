# TP4
# Exercice 1
# Programme 1
def est_solution(x,a,b,c):
    # Renvoie True si x est solution de 
    # ax^2+bx+c=0
    y=a*x**2+b*x+c
    if y==0:
        rep=True
    else:
        rep=False
    return rep

# prog. principal
rep=est_solution(1,1,-2,1)
print(rep)
print(est_solution(5, 2, -20, 50))
print(est_solution(2.5, 1, 2, 3))
