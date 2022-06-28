from random import randint

#liste=[int(random()*99+1) for i in range(1000)]
liste=[randint(1,100) for i in range(1000)]
print(liste)

nouvelle_liste=[ i  for i in liste if i> 99 ]
print(nouvelle_liste)
""" nouvelle_liste=[]
for i in liste:
    if i> 99:
        nouvelle_liste.append(i)
print(nouvelle_liste) """
