#11. Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados.
# Se a área for maior que 100, exibir a mensagem “Terreno grande”.
b = float(input('Digite o tamanho da base: '))
h = float(input('Digite a altura: '))
a = b*h
if a>100:
    print('terreno grande')
