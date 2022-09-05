#22. Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o
# cálculo da respectiva área. Enviar mensagem de erro se o usuário escolher uma opção inexistente.

#Encerrar o programa somente quando selecionada a opção de finalização.
# (Fazer esse exercício utilizando If..Else e/ou Case)

#1 – Triângulo
#2 – Quadrado
#3 – Retângulo
#4 – Círculo
#5 – Fim de processo

char = '*'
print(char*10, 'SELECIONE A FORMA DESEJADA PARA CALCULAR A AREA', char*10)
print(f'{char:<25} 1.TRIANGULO {char:>30}')
print(f'{char:<25} 2.QUADRADO {char:>31}')
print(f'{char:<25} 3.RETANGULO {char:>30}')
print(f'{char:<25} 4.CIRCULO {char:>32}')
print(f'{char:<25} 5.FIM DO PROCESSO {char:>24}')
print(char*68)
op = int(input('Selecione a opçao desejada 1,2,3,4 ou 5 para sair: '))
if op == 1:
    b = float(input('Digite a base do triangulo: '))
    h = float(input('Digite a altura do triangulo: '))
    a = (b * h) / 2
    print(f'A area de um triangulo de base {b} e altura {h}  é {a} ')
elif op == 2:
    a = float(input('Digite a aresta do quadrado para calcular sua area: '))
    area = a * a
    print(f'um quadrado com aresta de {a} tem uma area de {area}')
elif op == 3:
    b = float(input('Digite o tamanho da base: '))
    h = float(input('Digite a altura: '))
    a = b * h
    print(f'a area do retangulo de base {b} e altura {h} é {a}')
elif op == 4:
    r = float(input('Digite o valor do raio do circulo: '))
    a = (3.141592653589793 * r ** 2)
    print(f'a area do circulo é {a:.3f}')
elif op == 5:
    print('FIM DO PROCESSO!')
else:
    print('OPÇAO INVALIDA! TENTE DE NOVO...')