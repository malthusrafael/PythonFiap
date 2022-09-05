#7. Entrar via teclado com o valor de cinco produtos.
#Após as entradas, digitar um valor referente ao pagamento da somatória destes valores.
#Calcular e exibir o troco que deverá ser devolvido.
p1 = float(input('Digite o valor do primeiro produto R$'))
p2 = float(input('Digite o valor do primeiro produto R$'))
p3 = float(input('Digite o valor do primeiro produto R$'))
p4 = float(input('Digite o valor do primeiro produto R$'))
p5 = float(input('Digite o valor do primeiro produto R$'))
t = p1+p2+p3+p4+p5
print(f'O valor total da compra é R${t:.2f}')
p = float(input('Digite o valor do pagamento para calcular o troco R$'))
troco = p-t
print(f'O valor do troco é R${troco:.2f}')