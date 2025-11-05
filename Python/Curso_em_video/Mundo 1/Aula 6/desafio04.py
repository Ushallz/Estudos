thx= input('digite algo')

print('você digitou uma letra?',thx.isalpha())
print('se é uma letra, foi digitada em capslock?', thx.isupper())
print('se é uma letra, foi digitada em minúsculo?', thx.islower())
print('você digitou um número?', thx.isnumeric())
print('se for um número, é decimal?', thx.isdecimal())
print('você digitou uma letra ou número? (ou ambos)?',thx.isalnum())
print('independente do que for, contém algum espaço?', thx.isspace())
