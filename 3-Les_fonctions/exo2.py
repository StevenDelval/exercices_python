def est_pair(nb):
    
    if nb % 2 == 0:
        return True
    else:
        return False

nb_utilisateur = int(input("Entrez un nombre entier : "))
if est_pair(nb_utilisateur):
    print("Le nombre {} est pair".format(nb_utilisateur))
else:
    print("Le nombre {} est impair".format(nb_utilisateur))