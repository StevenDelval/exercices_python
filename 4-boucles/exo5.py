liste=[0,1,2,3,4,5,6]

def inverse_ordre(liste):
    '''
    Inverse l'ordre des élements.\n
    Param:
            liste : (list) une liste
    Return:
            (list) liste contenant les mêmes éléments, mais dans l'ordre inverse
    
    '''
    longueur_liste=len(liste)
    for i  in range(int(longueur_liste/2)):
        
        (liste[i],liste[longueur_liste-i-1])=(liste[longueur_liste-i-1],liste[i])
        
    return liste


print(liste)
print(inverse_ordre(liste))


