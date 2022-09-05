#17. Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa
#está ou não com seu peso ideal. Fórmula: peso/altura².
print('Calculadora IMC')
sexo = input('Digite M para Masculino ou F para feminino: ').upper()
p = float(input('Digite o peso: '))
a = float(input('Digite a altura'))
imc = p/(a*a)
if sexo == 'F' or sexo == 'FEMININO':
    if imc<19:
        print('Abaixo do peso!')
    elif 19<= imc <24:
        print('Peso ideal!')
    else:
        print('Acima do peso!')
elif sexo == 'M' or sexo == 'MASCULINO':
    if imc<20:
        print('Abaixo do peso')
    elif 20 <= imc <25:
        print('Peso ideal')
    else:
        print('Acima do peso')
else:
    print('Entrada invalida, tente de novo')
