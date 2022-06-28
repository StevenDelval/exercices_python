def x(a, b):
    ''' Multilpie 2 nombre positif entre eux .
    Si l'un des nombres ou les deux sont négatif, on prend son opposé.
    Paraètres:
                a: (number) un nombre
                b: (number) un nombre
    Return:
            (number) la multiplication des deux nombres
    
    '''
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return a*b
print("Documentation de la fonction x: \n",x.__doc__)