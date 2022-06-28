import turtle


turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)
turtle.goto(-100,0 )
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.goto(200,0 )
turtle.pendown() 
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin