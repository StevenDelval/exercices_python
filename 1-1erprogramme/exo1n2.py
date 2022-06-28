import turtle


turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)


for i in range(0,5):
    turtle.forward(100)
    turtle.left(360/5)

turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin
