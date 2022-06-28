from fonctions import *


def somme_liste(liste):
    '''
    Somme des nombres d'une liste.\n
    Param:
            liste : (list) une liste de nombre
    Return:
            somme: (number) somme des nombres de la liste
    
    '''
    somme =0
    for i in liste :
        somme+=i
    return somme
