from random import choice
a=str(input('digite o nome do 1o aluno'))
b=str(input('digite o nome do 2o aluno'))
c=str(input('digite o nome do 3o aluno'))
d=str(input('digite o nome do 4o aluno'))

chosen=choice((a,b,c,d))

print('o aluno selecionado foi o(a) {}'.format(chosen))