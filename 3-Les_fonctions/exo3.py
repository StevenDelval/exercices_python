def min_trois_nb(nb1,nb2,nb3):
    if nb1 > nb2:
        if nb2>nb3:
            return nb3
        else:
            return nb2
    else:
        if nb1>nb3:
            return nb3
        else:
            return nb1

nb_utilisateur1 = int(input("Entrez un nombre entier : "))
nb_utilisateur2 = int(input("Entrez un nombre entier : "))
nb_utilisateur3 = int(input("Entrez un nombre entier : "))

print("Le plus petit des trois est {}".format(min_trois_nb(nb_utilisateur1,nb_utilisateur2,nb_utilisateur3)))