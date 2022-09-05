#10. Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário,
# enviar mensagem avisando que os números são idênticos.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
if v1 == v2:
    print('Os valores sao identicos!')
elif v1 > v2:
    print(f'O primeiro valor {v1} é maior que o segundo {v2} ')
else:
    print(f'O segundo valor {v2} é maior que o primeiro {v1}')