#criando um game de descoberta de numeros trabalhando encima do random
# Primeiro importamos a biblioteca, renomeamos e criamos as variaveis iniciais
import random as rd
import time as tm

#importando uma biblioteca para trabalhar com matrizes de forma mais eficiente
import pandas as pd 
# de inicio vou criar um sistema de pontuação do qual será guardado o nome e o numero de tentativas do usuario
score = []
nome = []
#Testando um novo sistema de pontuação utilizando pandas
Pontuacao = {
    'nomes' : [nome],
    'score' : [score]
}

#Agora será criado um layout para se iniciar os trabalhos que irar funcionar dentro de um loop
while True:
    print('''
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
          
          NUMERO SECRETO
esse game consiste em acerta o numero definido pela maquina
          
1_Jogar
2_Score
3_Sair
''')

# colocando o sistema de sorteio do numero dentro do while para que ele se atualize toda vez que vier para tela inicial
    numero_secreto = rd.randint(0,100)

#agora vamos fazer os inputs para que a seleção seja possivel
    opcao = int(input("digite sua escolha: "))

#Agora chegou a hora de transformar essa resposta em ação, antes iremos criar uma variavél que ira contar a quantidade de partidas e também será usado para zerar a quantidade de partidas
    partida = 0

#Neste primeiro if referente a opção 1 ele fara o sistema do jogo onde ele ira comparar o numero secreto com o numero que o usuario propos, posteriormente também ira contar quantas vezes o jogador ja errou e quão proximo ele esta do numero seja para cima ou para baixo

    if opcao == 1:
        while True:
            partida = partida +1
            print (f"rodada ({partida}), boa sorte")
            n_j = int(input('qual o numero: '))
#Agora vamos trabalhar o sistema de resposta do jogador onde iremos entrgar se a resposta é maior ou menor do numero secreto
            if n_j > numero_secreto:
                print('Hey, isso está muito alto')
            
            elif n_j < numero_secreto:
                print('Pq tão baixo')
#Iremos colocar agora um sistema que reconheça o nome do usuario a partir do momento em que o game é finalizado
            else:
                print('Parabens meu caro, faça melhor da Próxima')
                name = input('digite seu playername: ')
                nome.append(name)
                score.append(partida)
                break
    
#Neste iremos trabalhar a segunda opção 'O score' onde iremos criar um contador que utilizara o sistema de variaveis e listas dentro de lista para que seja coletado após o termino do jogo e aplicado em tabela ultilizando o pandas
    elif opcao == 2:
        print(f'''
Aqui está a tabela dos campeoes 
    {pd.Series(Pontuacao)}
              ''')
#colocando um tempo de exibição para o score, antes que ele volte ao menu, pois está seção ainda não tem interação além da exibição do escore
        tm.sleep(5)

#Agora vamos trabalhar com a saida do usuario

    elif opcao == 3:
        print('muito obrigado por jogar')
        break

#Agora vamos criar uma condição de erro onde invalida a resposta do usuario
    else:
        print('opção invalida tente novamente')



