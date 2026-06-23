#importando bibliotecas
import pygame as pg
import random as rd 

#criando um display que execute fora do console em uma janela unica
pg.init()
tela = pg.display.set_mode((600,400))
pg.display.set_capition('game2')


#setando o tamanho e movimentação da cobra
cobra = [(100, 50)]
direcao = [(rd.randint(0,600), rd.randint(0,400))]


