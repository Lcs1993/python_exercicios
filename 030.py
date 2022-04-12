n = int(input('Digite um número'))
resto = n%2
if resto == 0:
    print('\033[32m número par')
else:
    print('\033[36m número impar')
