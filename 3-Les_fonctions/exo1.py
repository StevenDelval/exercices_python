def est_pair():
    nb_utilisateur = int(input("Entrez un nombre entier : "))
    if nb_utilisateur % 2 == 0:
        print("Le nombre {} est pair".format(nb_utilisateur))
    else:
        print("Le nombre {} est impair".format(nb_utilisateur))

est_pair()
