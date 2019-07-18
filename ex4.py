a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = (b*b) - (4*(a*c))
if delta>=0:
    valorx = ((-b)+(delta**(1/2)))/(2*a)
    valory = ((-b)-(delta**(1/2)))/(2*a)
    print(valorx)
    print(valory)
else:
    print('Não é possivel calcular')