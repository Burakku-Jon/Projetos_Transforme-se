l1 = int(input('digte um numero: '))
l2 = int(input('digte um numero: '))
l3 = int(input('digte um numero: '))

if l1 + l2 > l3 or l1 + l3 > l2 or l3 + l2 > l1:
    if l1 == l2 and l1 == l3:
        print('equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('isosceles')
    else:
        print('escaleno')
else:
    print('não é triangulo')