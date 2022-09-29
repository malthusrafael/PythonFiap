#37. Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez.
# Entre as tabuadas, solicitar que o usuário pressione uma tecla.

for i in range(1,21,1):
    for j in range(1,11,1):
        t = i*j
        print(f'{i} x {j} = {t}')
    if (i<20):
        input('Aperte uma tecla para continuar: ')
    print('Fim da tabuada')