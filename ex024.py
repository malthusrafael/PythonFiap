nome = input('Digite seu nome: ').upper()
sexo = input('Digite seu sexo, F para  Feminino ou M para Masculino: ').upper()
estado = input('Digite o estado civil').upper()

if (sexo == 'F' and estado == 'CASADA'):
    tempo = input('Digite a quanto tempo está casada: ')
else:
    print('Fim do processo!')