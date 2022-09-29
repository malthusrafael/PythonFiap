#37. Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez.
# Entre as tabuadas, solicitar que o usuário pressione uma tecla.

n1 = 1
while n1<=20:

    i = 1
    while i<11:
        r = n1*i
        print(f'{n1} X {i} = {r}')
        i = i + 1
    input('Aperte uma tecla para continuar: ')
    n1 = n1+1