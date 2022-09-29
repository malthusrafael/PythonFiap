#55. Armazenar um máximo de 20 valores em um vetor. A quantidade de valores a serem armazenados será escolhida pelo
# usuário. Enviar mensagem de erro, caso a quantidade de valores escolhida esteja fora da faixa possível e solicitar
# a quantidade novamente. Após a digitação dos valores, criar uma rotina de consulta, onde o usuário digita um número
# e o programa exibe em qual posição do vetor este número está localizado. Se o número não for encontrado,
# enviar mensagem “Valor não encontrado!”. Perguntar ao usuário se deseja ou não fazer uma nova consulta,
# consistir a resposta e encerrar o programa em caso negativo.

valores = []
novamente = 's'
qtd = int(input('Digite a quantidade de valores a ser digitados: '))

while (qtd <= 0 or qtd > 20):
    print('O limite é até 20!')
    qtd = int(input('Digite a quantidade de valores a ser digitados: '))
for i in range(0, qtd, 1):
    x = int(input('Digite um valor: '))
    valores.append(x)
while novamente == 's':
    num = int(input('Digite o valor a ser localizado no array: '))
    pos = -1
    for i in range(0, qtd, 1):
        if (valores[i] == num):
            pos = i
    if pos != -1:
        print(f'O valor foi encontrado na  {pos}')
    else:
        print('valor nao encontrado')