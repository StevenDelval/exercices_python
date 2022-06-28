var1 = "Je dois être en seconde position"
var2 = "Je dois être en première position"

## Ajouter le code de l'exercice ici ##
def echange (var1,var2):
    var_echange=var1
    var1=var2
    var2=var_echange
    return var1,var2


var1,var2=echange(var1,var2)

print(var1 + " | " + var2) 