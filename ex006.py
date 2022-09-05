#6. Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares.
#Calcular e exibir o valor correspondente em Reais (R$).
c = float(input('Digite o valor em real da cotaçao do dólar R$'))
d = float(input('Digite o valor em dólares para saber seu preço em Reais. U$'))
r = c*d
print(f'O valor de U${c:.2f} dolares em reais é R${r:.2f}')