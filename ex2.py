lista = []
i = 0

while i<20:
    valor = float(input('Digite um valor: '))
    lista.append(valor)
    if i==0:
        valormax = lista[0]

    if valor>valormax:
        valormax = valor
    
    i += 1

print(valormax)