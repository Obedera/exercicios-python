import random
lista = []
inpares = []
pares = []
i = 0

while i<10:
    lista.append(random.randint(0, 100))
    if lista[i]%2 == 0:
        pares.append(lista[i])
    else:
        inpares.append(lista[i])
    i +=1

print('Essa foi a lista gerada aleatóriamente:')
print(lista)
print('ímpares: '+str(inpares))
print('pares: '+str(pares))