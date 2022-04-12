frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece \033[33m {} \033[m vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição \033[33m {}\033[m '.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição \033[33m {}'.format(frase.rfind('A')+1))
