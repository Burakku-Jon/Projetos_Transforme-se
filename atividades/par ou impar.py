while True:
    try:
        numero = int(input('digite um número: '))
        if numero %2 == 0:
            print(f'O {numero} é par')
        elif numero %2 != 0:
            print(f'o {numero} é impar')
    except:
        print('dado invalido')