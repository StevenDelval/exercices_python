from exo2 import somme_liste,creation_liste

def moyenne_liste(liste):
    '''
    Moyenne des nombres d'une liste.\n
    Param:
            liste : (list) une liste de nombre
    Return:
            (number) moyenne des nombres de la liste
    
    '''
    somme=somme_liste(liste)
    longueur=len(liste)
    return somme/longueur

liste=creation_liste(4)
print(liste)
print("Somme de la liste", somme_liste(liste))
print("Moyenne de la liste",moyenne_liste(liste))
    
