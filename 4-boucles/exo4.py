for i in range(1,101):
    if i%3==0 or i%5==0:
        if i%3==0 and i%5!=0:
            print("Fizz",end='-')
        if i%3!=0 and i%5==0:
            print("Fuzz",end='-')
        if i%3==0 and i%5==0:
            print("Fiuzz",end='-')
    else:
        print(i,end='-')
print()