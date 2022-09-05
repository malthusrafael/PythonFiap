#15. A partir de três valores que serão digitados, verificar se formam ou não um triângulo.
# Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”.
# Triângulo escaleno possui todos os lados diferentes, o isósceles, dois lados iguais e o eqüilátero,
# todos os lados iguais. Para existir triângulo é necessário que a soma de dois lados quaisquer seja maior que o outro,
# isto, para os três lados.
v1 = float(input('Digite o primeiro lado: '))
v2 = float(input('Digite o segundo lado: '))
v3 = float(input('Digite o terceiro lado: '))
if v1 + v2 > v3:
    print('É um Triangulo ')
    if v1 != v2 != v3:
        print('Triangulo escaleno')
    elif v1 == v2 == v3:
        print('Triangulo equilatero')
    else:
        print('Triangulo Isóceles')
else:
    print('Nao é um triangulo!')
