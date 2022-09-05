#13. Entrar via teclado com três valores distintos.Exibir o maior deles.
v1 = float(input('Digite o primeiro: '))
v2 = float(input('Digite o segundo valor: '))
v3 = float(input('Digite o terceiro valor: '))

if v1 == v2 == v3:
    print('iguais')
elif v1 < v2 > v3:
    print("O segundo valor é maior")
elif v3 < v1 > v2:
    print("O primeiro valor é maior")
elif v1 == v3 > v2:
    print("O primeiro e o terceiro são iguais e maiores que o segundo")
elif v1 == v2 > v3:
    print("O primeiro e o segundo são iguais e maiores que o terceiro")
elif v2 == v3 > v1:
    print("O  segundo e o terceiro são iguais e maiores que o primeiro")
else:
    print("Terceiro é maior")
