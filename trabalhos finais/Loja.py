#começando importando as bibliotecas necessárias:
import pandas as pd
import numpy as np
import time as tm
#criando o dicionário com os produtos disponíveis na loja:
produtos = {
    1 : {"nome": "Teclado magnético", "preço": 650.00, "quantidade": 15},
    2 : {"nome" : "Teclado mecânico", "preço": 300.00, "quantidade": 15},
    3 : {"nome" : "Monitor FHD 27", "preço": 600.00, "quantidade": 5},
    4 : {"nome" : "Monitor QHD 27", "preço": 900.00, "quantidade": 5},
    5 : {"nome" : "Monitor QHD 32", "preço": 1200.00, "quantidade": 5},
    6 : {"nome" : "Mouse gamer Razer Purgatory 6400 dpi", "preço": 100.00, "quantidade": 25},
    7 : {"nome" : "Mouse gamer Redragon cobra 10000 dpi", "preço": 250.00, "quantidade": 15},
    8 : {"nome" : "Headset gamer Havit h4008", "preço": 300.00, "quantidade": 25}
}
carrinho = []
while True:

    print("[1] Visualizar estoque.")
    print("[2] Adicionar item ao carrinho.")
    print("[3] Visualizar carrinho.")
    print("[4] Finalizar compra.")
    print("[0] Sair.")
    selection = int(input("Escolha sua opção:"))

    if selection == 1:
        print(f"[visualizar estoque]")
        for key, content in produtos.items():
            print(f" Código:{key} : Nome:{content["nome"]} : Quantidade:{content["quantidade"]} : Preço: R$:{content["preço"]}")

    elif selection == 2:
        print(f"[adicionar item ao carrinho]")
        id_produto = int(input("qual ID produto você deseja comprar?"))

        if id_produto in produtos:
            prod_amnt = int(input("Quantas unidades você quer?"))
            if prod_amnt <= 0:
                print("Produto esgotado.")
                break
            elif prod_amnt <= produtos[id_produto]["quantidade"]:
                item = {
                    "código" : id_produto,
                    "nome" : produtos[id_produto]["nome"],
                    "quantidade": prod_amnt,
                    "preço" : produtos[id_produto]["preço"],
                    "sub_total" : prod_amnt * produtos[id_produto]["preço"]
                }
                carrinho.append(item)
                produtos[id_produto]["quantidade"] -= prod_amnt
                print(item)
            else:
                print(f"Temos penas {produtos[id_produto]["quantidade"]} unidades em estoque.")
        else:
            print("Item inexistente")
    elif selection == 3:
        print(f"[visualizar carrinho]")
        if carrinho:
            print(carrinho)
        else:
            print("Carrinho vazio")
    elif selection == 4:
        print(f"[finalizar compra]")
    elif selection < 0:
        print("Opção inválida")
        break
    else:
        print("Saindo.")
        tm.sleep(2)
        print("Saindo..")
        tm.sleep(2)
        print("Saindo...")
        tm.sleep(2)
 