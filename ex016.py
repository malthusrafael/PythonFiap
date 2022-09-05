#16. Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo.
# Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.
a = float(input('Digite o valor da hipotenusa: '))
b = float(input('Digite o valor do primeiro cateto: '))
c = float(input('Digite o valor do segundo cateto: '))
if a*a == (b*b) + (c*c):
    print('É um triangulo retangulo')
else:
    print('Não é um triangulo retangulo')