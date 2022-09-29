#33. Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou “M” como respostas válidas.

s = input('Digite o seu sexo F para feminino ou M para masculino:  ').upper()

while s != 'F' and s != 'M':
    print('OPÇAO IVALIDA TENTE NOVAMENTE')
    s = input('Digite o seu sexo F para feminino ou M para masculino:  ').upper()