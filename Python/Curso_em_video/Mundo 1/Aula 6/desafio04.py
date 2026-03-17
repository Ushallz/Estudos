thx= input('digite algo')

print('Você digitou uma letra?',thx.isalpha())
print('Se é uma letra, foi digitada em capslock?', thx.isupper())
print('Se é uma letra, foi digitada em minúsculo?', thx.islower())
print('Você digitou um número?', thx.isnumeric())
print('Caso seja um número, é decimal?', thx.isdecimal())
print('Você digitou uma letra, número ou ambos?',thx.isalnum())
print('O elemento em questão contém algum espaço?', thx.isspace())
