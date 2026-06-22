user = input('digite usuario: ')
senha = int(input('senha: '))

if user == 'admin' and senha == 9988:
    print('acesso permitido')
else:
    print('Dados de acesso inválidos')