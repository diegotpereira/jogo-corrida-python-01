

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

    # variáveis de tempo e placar
    timer = 0
    tempo_segundo = 0


    # Define a posição inicial da pista
    xpista = 0
    ypista = -720

    xcmd = 5
    ycmd = 100

    # Define um contador para o fundo
    contFundo = 1

    # Tempo de fundo (não está sendo utilizado atualmente)
    tempo_fundo = 0

    # variáveis de velocidade de deslocamento do objeto (círculo)

    # valor em pixels - velocidade do carro do jogador
    veloc_xp = 20

    # velocidade dos carros npc
    veloc_x1 = veloc_x2 = veloc_x3 = veloc_x4 = veloc_x5 = 20

    # valor em pixels - velocidade da pista
    veloc_pista = 30

    # Carrega a imagem de fundo usando a função escolheFundo
    fundo = pygame.image.load(escolheFundo(contFundo))

    # Carrega a imagem do carro NPC usando a função npc_aleatorio
    carro = pygame.image.load(npc_aleatorio())
    carro_pc1 = pygame.image.load(npc_aleatorio())
    # carro_pc2 = pygame.image.load(npc_aleatorio())
    # carro_pc3 = pygame.image.load(npc_aleatorio())
    # carro_pc4 = pygame.image.load(npc_aleatorio())
    # carro_pc5 = pygame.image.load(npc_aleatorio())

    cmd = pygame.image.load('C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/cmd.png')

    # Cria a janela do jogo
    janela = cria_tela()

    #mostra nome do jogo na janela
    pygame.display.set_caption('Corrida em PYTHON -> Jogar')

    # Variável para controlar se a janela do jogo está aberta
    janela_aberta = True

    # Loop principal do jogo, que continua enquanto a janela estiver aberta
    while janela_aberta:

        # pygame.time.delay(50)

        # captura eventos do jogo
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                janela_aberta = False


        # comandos para movimentação do objeto
        comandos = pygame.key.get_pressed()

        # comando movimentar para frente
        if(comandos[pygame.K_UP] or comandos[pygame.K_w]) and yp > 0: 

            yp -= veloc_xp

        # comando movimentar para trás
        if(comandos[pygame.K_DOWN] or comandos[pygame.K_s]) and yp < 600:

            yp += veloc_xp

        # comando movimentar para a direita
        if(comandos[pygame.K_RIGHT] or comandos[pygame.K_d]) and xp < 750:

            xp += veloc_xp

        # comando movimentar para a esquerda
        if(comandos[pygame.K_LEFT] or comandos[pygame.K_a]) and xp > 210:

            xp -= veloc_xp
        
        # # Movimentação dos carros NPC
        # y1 += veloc_x1
        # if y1 > 680:

        #     y1 = randint(-5000, -500)

        #     if tempo_segundo >= 1:

        #         veloc_x1 = velocidade_npc() * 10 * (1 + tempo_segundo/10)

        #     else:

        #         veloc_x1 = velocidade_npc() * 10


        y2 += veloc_x2
        y3 += veloc_x3
        y4 += veloc_x4
        y5 += veloc_x5

        # Movimentação da pista
        ypista += veloc_pista
        if ypista >= 0:

            ypista = -720

        # # Atualização do placar e velocidade
        # if timer < 20:

        #     timer += 1

        # else:

        #     if veloc_pista < 100:

        #         veloc_pista = veloc_pista * (1 + tempo_segundo/500)
    

        # Troca de fundo da pista
        if tempo_fundo > 16:

            tempo_fundo = 0

            contFundo += 1

            if contFundo > 3:

                contFundo = 1

            fundo = pygame.image.load(escolheFundo(contFundo))

        # Desenha o fundo na tela na posição especificada
        janela.blit(fundo, (int(xpista), int(ypista)))

        janela.blit(cmd, (xcmd, ycmd))

        # Desenha o carro na tela na posição especificada
        janela.blit(carro, (xp, yp))
        janela.blit(carro_pc1, (int(x1), int(y1)))
        # janela.blit(carro_pc2, (int(x2), int(y2)))
        # janela.blit(carro_pc3, (int(x3), int(y3)))
        # janela.blit(carro_pc4, (int(x4), int(y4)))
        # janela.blit(carro_pc5, (int(x5), int(y5)))



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


# Função para determinar a velocidade do NPC
def velocidade_npc():

    # Gera um número aleatório entre 8 e 12 (inclusive) e o atribui à variável v1
    v1 = (randint(8, 12))

    # Divide o valor de v1 por 10 para obter a velocidade final e a atribui à variável vFinal
    vFinal = v1/10

    # Retorna a velocidade final calculada
    return vFinal