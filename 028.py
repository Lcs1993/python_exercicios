from random import randint
from time import sleep

n = int(input('Digite um número entre 0 e 5'))
sorteio = randint(0, 5)
print('processando...')
sleep(2)
if n == sorteio:
    print('\033[42m você acertou o número')
else:
    print('\033[41m você errou o número. eu pensei no número {}'.format(sorteio))