import random
a=str(input('digite o nome do 1o aluno'))
b=str(input('digite o nome do 2o aluno'))
c=str(input('digite o nome do 3o aluno'))
d=str(input('digite o nome do 4o aluno'))
list=[a, b, c, d]
random.shuffle(list)
print(f'a ordem de apresentação será{list}')