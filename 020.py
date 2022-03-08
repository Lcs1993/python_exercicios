from random import shuffle
a1 = input('Digite o nome do primeiro aluno')
a2 = input('Digite o nome do segundo aluno')
a3 = input('Digite o nome do terceiro aluno')
a4 = input('Digite o nome do quarto aluno')
lista_aluno = [a1, a2, a3, a4]
shuffle(lista_aluno)
print('A ordem de apresentação é {}'.format(lista_aluno))



