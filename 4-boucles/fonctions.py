from random import random



def creation_liste(longueur):
    '''
    Création d'une liste d'une longueur donner.\n
    Param:
            longueur : (number) un nombre
    Return:
            liste : (list) une liste de nombre
    
    '''
    liste=[]
    for i in range(longueur):
        liste.append(round(random()*10))
    return liste
    

    