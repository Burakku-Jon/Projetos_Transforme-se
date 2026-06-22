s_b = int(input('salario bruto: '))
v_p = int(input('valor parcela: '))
emp = s_b * 0.3

if v_p <= emp:
    print('emprestimo aprovado')
else:
    print('emprestimo negado')