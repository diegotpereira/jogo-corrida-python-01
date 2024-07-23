

# Importa a biblioteca pygame para criação de jogos e a função randint para gerar números aleatórios
import pygame
from random import randint
import os

# cria janela do jogo
def cria_tela():

    janela = pygame.display.set_mode((1080, 720))

    return janela

# Função para escolher o fundo do jogo com base no contador fornecido
def escolheFundo(contFundo):

    caminho_base = os.path.dirname(__file__)

    # Dicionário que mapeia o contador do fundo para o caminho da imagem do fundo
    opcao = {
        1: os.path.join(caminho_base, 'image', 'pista1.png'), 
        2: os.path.join(caminho_base, 'image', 'pista2.png'), 
        3: os.path.join(caminho_base, 'image', 'pista3.png')}

    # Retorna o caminho da imagem do fundo correspondente ao contador
    return opcao[contFundo]
    
# caminho_imagem = escolheFundo(1)
# print(f"Caminho da imagem: {caminho_imagem}")

# if os.path.exists(caminho_imagem):
#     print("Arquivo encontrado.")
# else:
#     print("Arquivo não encontrado.")

# Função para escolher um carro NPC aleatório
def npc_aleatorio():

    caminho_base = os.path.dirname(__file__)

    # Dicionário que mapeia números para o caminho da imagem do carro NPC
    carro_npc = {
        '1': os.path.join(caminho_base, 'image', 'car_pc1.png'),
        '2': os.path.join(caminho_base, 'image', 'car_pc2.png'),
        '3': os.path.join(caminho_base, 'image','car_pc3.png'),
        '4': os.path.join(caminho_base, 'image','car_pc4.png'),
        '5': os.path.join(caminho_base, 'image','car_pc5.png'),
        '6': os.path.join(caminho_base, 'image','car_pc6.png'),
        '7': os.path.join(caminho_base, 'image','car_pc7.png'),
        '8': os.path.join(caminho_base, 'image','car_pc8.png'),
        '9': os.path.join(caminho_base, 'image','car_pc9.png'),
        '10': os.path.join(caminho_base, 'image','car_pc10.png'),
        '11': os.path.join(caminho_base, 'image','car_pc11.png')
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