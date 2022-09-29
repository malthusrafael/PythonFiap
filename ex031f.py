#31. Criar uma rotina de entrada que aceite somente um valor positivo.
n1 = int(input('Digite um valor positivo: '))
for n1 in range(1,1,0):
    if (n1<0):
        n1 = int(input('Digite um valor positivo: '))
