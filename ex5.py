def calcular_comprimento(valor):
    return float((2*3.14)*valor)

def calcular_area(valor):
    return float(3.14*(valor*valor))

raio = float(input('Digite o raio: '))
print('O comprimnto do circulo é: '+str(calcular_comprimento(raio)))
print('A area do circulo é: '+str(calcular_area(raio)))