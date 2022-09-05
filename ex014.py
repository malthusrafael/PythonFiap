#14. Entrar com o peso e a altura de uma determinada pessoa. Após a digitação,
# exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))
imc = (p/(a*a))
if imc<19:
    print('Abaixo do peso')
elif 19 <= imc <24:
    print('Peso ideal')
else:
    print('Acima do peso')