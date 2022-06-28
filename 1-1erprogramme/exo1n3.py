import turtle
import math


turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)



turtle.forward(170)
turtle.right(135)
turtle.forward(50)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(50)
turtle.penup()
turtle.goto(0, 20)
turtle.pendown()
turtle.right(135)
turtle.forward(170)
turtle.right(240)
turtle.forward(170)
turtle.right(240)
turtle.forward(170)
turtle.right(240)
turtle.forward(170/2)
turtle.left(90)
turtle.forward(int(math.sqrt(3)*170/2))

turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin
