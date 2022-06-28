dictionnaire={
    	'nonantaine':"En Belgique et en Suisse, nombre de quatre-vingt-dix ou environ ; âge d'environ quatre-vingt-dix ans."
}

mot_utilisateur=input("Entre un mot : ")

if mot_utilisateur in dictionnaire:
    print(dictionnaire[mot_utilisateur])
else:
    print("Nous ne connaissons pas ce mot")