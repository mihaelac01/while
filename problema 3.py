nr=0
suma=0
while((nr%2==0)or(nr%3!=0)):
    nr=eval(input("dati un numar: "))
    if nr%2==0:
        suma+=nr

print(suma)