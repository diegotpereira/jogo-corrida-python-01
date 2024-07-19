

# Importa a biblioteca pygame para criação de jogos e a função randint para gerar números aleatórios
import pygame
from random import randint

# cria janela do jogo
def cria_tela():

    janela = pygame.display.set_mode((1080, 720))

    return janela

# Função para escolher o fundo do jogo com base no contador fornecido
def escolheFundo(contFundo):

    # Dicionário que mapeia o contador do fundo para o caminho da imagem do fundo
    opcao = {1: 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/pista1.png', 2: 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/pista2.png', 3: 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/pista3.png'}

    # Retorna o caminho da imagem do fundo correspondente ao contador
    return opcao[contFundo]

# Função para escolher um carro NPC aleatório
def npc_aleatorio():

    # Dicionário que mapeia números para o caminho da imagem do carro NPC
    carro_npc = {
        '1': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc1.png',
        '2': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc2.png',
        '3': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc3.png',
        '4': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc4.png',
        '5': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc5.png',
        '6': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc6.png',
        '7': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc7.png',
        '8': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc8.png',
        '9': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc9.png',
        '10': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc10.png',
        '11': 'C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/car_pc11.png'
    }

    # Escolhe um número aleatório entre 1 e 12 e o converte para string
    carro = str(randint(1, 12))

    # Retorna o caminho da imagem do carro NPC correspondente ao número aleatório
    return carro_npc[carro]


# Função para determinar a velocidade do NPC
def velocidade_npc():

    # Gera um número aleatório entre 8 e 12 (inclusive) e o atribui à variável v1
    v1 = (randint(8, 12))

    # Divide o valor de v1 por 10 para obter a velocidade final e a atribui à variável vFinal
    vFinal = v1/10

    # Retorna a velocidade final calculada
    return vFinal