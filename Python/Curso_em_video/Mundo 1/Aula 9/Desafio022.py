Nome=input('digite o seu nome completo')

print(f'O seu nome com letras minúsculas é {Nome.lower()}')

print(f'O seu nome, com letras maiúsculas é {Nome.upper()}')

Space=Nome.count(' ')

print(f'Seu nome inteiro possui {len(Nome)-Space} letras')

Firstname=Nome.split()

print(f'seu primeiro nome possui {len(Firstname[0])}')
