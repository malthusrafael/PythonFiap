#30. Elabore um algoritmo que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e
# efetuar o cálculo adequado e exibir o valor a ser pago no final.
#Código Condição de pagamento
v1 = float(input('Qual o valor do produto R$'))
char = '*'
print(f'{char*17} OPÇOES DE PAGAMENTO {char*17}')
print('1.À vista em dinheiro ou cheque, recebe 10% de desconto.')
print('2.À vista no cartão de crédito, recebe 15% de desconto.')
print('3.Em duas vezes, preço normal de etiqueta sem juros.')
print('4.Em quatro vezes, preço normal de etiqueta mais juros de 10%.')
print('5. Cancelar compra.')
print(char*60)
fp = int(input('Digite a opçao de pagamento 1,2,3,4 ou 5 para cancelar compra: '))

if fp == 1:
    v2 = (v1/100)*90
    print(f'O valor R${v1:.2f} a ser pago com 10% de desconto é R${v2:.2f}')
elif fp ==2:
    v3 = (v1/100)*85
    print(f'O Valor R${v1:.2f} a ser pago com 15% de desconto é R${v3:.2f}')
elif fp == 3:
    v4 = v1/2
    print(f'O Valor a ser pago é R${v1:.2f} em 2x se juros de R${v4:.2f}')
elif fp == 4:
    v5 = (v1/100)*110
    v6 = v5/4
    print(f'O Valor a ser pago era R${v1:.2f}, em 4x de R${v6:.2f} totalizando R${v5:.2f} com 10% de juros')
elif fp == 5:
    print('Compra cancelada')
else:
    print('OPÇÃO INVALIDA! TENTE NOVAMENTE!')