

# Importa a biblioteca pygame para criação de jogos e a função randint para gerar números aleatórios
import pygame
from random import randint

# Função para criar a janela do jogo com as dimensões 1080x720
def cria_tela():

    # Cria a janela com as dimensões especificadas
    janela = pygame.display.set_mode((1080, 720))

    # Retorna a janela criada
    return janela


# Função principal para executar o jogo
def jogar():

    # Inicializa o Pygame, necessário para usar suas funcionalidades
    pygame.init()

    # Define a posição inicial do carro do jogador
    xp = 486
    yp = 500
    
    x1 = 195
    y1 = randint(-2000, -500)

    x2 = 340
    y2 = randint(-2000, -500)

    x3 = 486
    y3 = randint(-2000, -500)

    x4 = 630
    y4 = randint(-2000, -500)

    x5 = 775
    y5 = randint(-2000, -500)


    # Define a posição inicial da pista
    xpista = 0
    ypista = -720

    # Define um contador para o fundo
    contFundo = 1

    # Tempo de fundo (não está sendo utilizado atualmente)
    tempo_fundo = 0

    # Carrega a imagem de fundo usando a função escolheFundo
    fundo = pygame.image.load(escolheFundo(contFundo))

    # Carrega a imagem do carro NPC usando a função npc_aleatorio
    carro = pygame.image.load(npc_aleatorio())
    carro_pc1 = pygame.image.load(npc_aleatorio())
    carro_pc2 = pygame.image.load(npc_aleatorio())
    carro_pc3 = pygame.image.load(npc_aleatorio())
    carro_pc4 = pygame.image.load(npc_aleatorio())
    carro_pc5 = pygame.image.load(npc_aleatorio())

    # Cria a janela do jogo
    janela = cria_tela()

    # Variável para controlar se a janela do jogo está aberta
    janela_aberta = True

    # Loop principal do jogo, que continua enquanto a janela estiver aberta
    while janela_aberta:

        # pygame.time.delay(50)

        # for event in pygame.event.get():

        #     if event.type == pygame.QUIT:

        #         janela_aberta = False

     
        # if tempo_fundo > 16:

        #     tempo_fundo = 0

        #     fundo = pygame.image.load(escolheFundo(contFundo))

        # Desenha o fundo na tela na posição especificada
        janela.blit(fundo, (int(xpista), int(ypista)))

        # Desenha o carro na tela na posição especificada
        janela.blit(carro, (xp, yp))
        janela.blit(carro_pc1, (int(x1), int(y1)))
        janela.blit(carro_pc2, (int(x2), int(y2)))
        janela.blit(carro_pc3, (int(x3), int(y3)))
        janela.blit(carro_pc4, (int(x4), int(y4)))
        janela.blit(carro_pc5, (int(x5), int(y5)))

        # Atualiza a tela com as mudanças feitas
        pygame.display.update()

        
    


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