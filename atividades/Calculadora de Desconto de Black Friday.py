valor_c = float(input('valor da compra: '))

if valor_c <= 100.00:
    print(f'valor da sua compra é {valor_c}, vc não obteve desconto')
elif valor_c <= 300.00:
    print(f'valor da sua compra é {valor_c}, vc obteve desconto de {valor_c*0.05}, oq trouxe o valor FINAL de {valor_c-(valor_c*0.05)}')
elif valor_c <= 500.00:
    print(f'valor da sua compra é {valor_c}, vc obteve desconto de {valor_c*0.1}, oq trouxe o valor FINAL de {valor_c-(valor_c*0.1)}')
elif valor_c >= 500.00:
    print(f'valor da sua compra é {valor_c}, vc obteve desconto de {valor_c*0.15}, oq trouxe o valor FINAL de {valor_c-(valor_c*0.15)}')
