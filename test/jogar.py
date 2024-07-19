
# Importa a biblioteca pygame para criação de jogos e a função randint para gerar números aleatórios
import pygame
from random import randint
import telaJogo

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
    fundo = pygame.image.load(telaJogo.escolheFundo(contFundo))

    # Carrega a imagem do carro NPC usando a função npc_aleatorio
    carro = pygame.image.load(telaJogo.npc_aleatorio())
    carro_pc1 = pygame.image.load(telaJogo.npc_aleatorio())
    carro_pc2 = pygame.image.load(telaJogo.npc_aleatorio())
    carro_pc3 = pygame.image.load(telaJogo.npc_aleatorio())
    carro_pc4 = pygame.image.load(telaJogo.npc_aleatorio())
    carro_pc5 = pygame.image.load(telaJogo.npc_aleatorio())

    cmd = pygame.image.load('C:/Users/Suporte/Documents/Repositorio/jogo-corrida-python-01/test/image/cmd.png')

    # Cria a janela do jogo
    janela = telaJogo.cria_tela()

    #mostra nome do jogo na janela
    pygame.display.set_caption('Corrida em PYTHON -> Jogar')

    # Variável para controlar se a janela do jogo está aberta
    janela_aberta = True

    # Loop principal do jogo, que continua enquanto a janela estiver aberta
    while janela_aberta:

        pygame.time.delay(50)

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
        

        # Movimentação dos carros NPC

        # Atualiza a posição vertical do carro NPC 1
        y1 += veloc_x1

        # Verifica se o carro NPC 1 saiu da tela (posição y maior que 680)
        if y1 > 680:

            # Se o carro NPC 1 saiu da tela, reposiciona-o em uma nova posição aleatória 
            # acima da tela
            y1 = randint(-5000, -500)

            # Carrega uma nova imagem aleatória para o carro NPC 1
            carro_pc1 = pygame.image.load(telaJogo.npc_aleatorio())

            # Ajusta a velocidade do carro NPC 1 dependendo do tempo decorrido no jogo
            if tempo_segundo >= 1:

                # Se o tempo decorrido é de pelo menos 1 segundo, aumenta a velocidade 
                # do NPC proporcionalmente ao tempo
                veloc_x1 = telaJogo.velocidade_npc() * 10 * (1 + tempo_segundo/10)

            else:

                # Se o tempo decorrido é menos de 1 segundo, usa a velocidade base do NPC
                veloc_x1 = telaJogo.velocidade_npc() * 10

        # Atualiza a posição vertical do carro NPC 2
        y2 += veloc_x2

        # Verifica se o carro NPC 2 saiu da tela (posição y maior que 680)
        if y2 > 680:

            # Se o carro NPC 2 saiu da tela, 
            # reposiciona-o em uma nova posição aleatória acima da tela
            y2 = randint(-5000, -500)

            # Carrega uma nova imagem aleatória para o carro NPC 2
            carro_pc2 = pygame.image.load(telaJogo.npc_aleatorio())

            # Ajusta a velocidade do carro NPC 2 dependendo do tempo decorrido no jogo
            if tempo_segundo >= 1:

                # Se o tempo decorrido é de pelo menos 1 segundo, aumenta a velocidade 
                # do NPC proporcionalmente ao tempo
                veloc_x2 = telaJogo.velocidade_npc() * 10 (1 + tempo_segundo/10)

            else:
                
                # Se o tempo decorrido é menos de 1 segundo, usa a velocidade base do NPC
                veloc_x2 = telaJogo.velocidade_npc() * 10



        # Atualiza a posição vertical do carro NPC 3
        y3 += veloc_x3

        # Verifica se o carro NPC 3 saiu da tela (posição y maior que 680)
        if y3 > 680:
 
            # Se o carro NPC 3 saiu da tela, 
            # reposiciona-o em uma nova posição aleatória acima da tela
            y3 = randint(-5000, -500)

            # Carrega uma nova imagem aleatória para o carro NPC 3
            carro_pc3 = pygame.image.load(telaJogo.npc_aleatorio())

            # Ajusta a velocidade do carro NPC 3 dependendo do tempo decorrido no jogo
            if tempo_segundo >= 1:

                # Se o tempo decorrido é de pelo menos 1 segundo, aumenta a velocidade 
                # do NPC proporcionalmente ao tempo
                veloc_x3 = telaJogo.velocidade_npc() * 10 * (1 + tempo_segundo/10)

            # Se o tempo decorrido é menos de 1 segundo, usa a velocidade base do NPC
            else:

                # Se o tempo decorrido é menos de 1 segundo, usa a velocidade base do NPC
                veloc_x3 = telaJogo.velocidade_npc() * 10

        # Atualiza a posição vertical do carro NPC 4
        y4 += veloc_x4

        # Verifica se o carro NPC 4 saiu da tela (posição y maior que 680)
        if y4 > 680:

            # Se o carro NPC 4 saiu da tela, 
            # reposiciona-o em uma nova posição aleatória acima da tela
            y4 = randint(-5000, -500)

            # Carrega uma nova imagem aleatória para o carro NPC 3
            carro_pc4 = pygame.image.load(telaJogo.npc_aleatorio())

            # Ajusta a velocidade do carro NPC 4 dependendo do tempo decorrido no jogo
            if tempo_segundo >= 1:

                # Se o tempo decorrido é de pelo menos 1 segundo, aumenta a velocidade 
                # do NPC proporcionalmente ao tempo
                veloc_x4 = telaJogo.velocidade_npc() * 10 * (1 + tempo_segundo/10)

            else:

                # Se o tempo decorrido é menos de 1 segundo, usa a velocidade base do NPC
                veloc_x4 + telaJogo.velocidade_npc() * 10

        # Atualiza a posição vertical do carro NPC 5
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

            fundo = pygame.image.load(telaJogo.escolheFundo(contFundo))

        # Desenha o fundo na tela na posição especificada
        janela.blit(fundo, (int(xpista), int(ypista)))

        janela.blit(cmd, (xcmd, ycmd))

        # Desenha o carro na tela na posição especificada
        janela.blit(carro, (xp, yp))
        janela.blit(carro_pc1, (int(x1), int(y1)))
        janela.blit(carro_pc2, (int(x2), int(y2)))
        janela.blit(carro_pc3, (int(x3), int(y3)))
        janela.blit(carro_pc4, (int(x4), int(y4)))
        janela.blit(carro_pc5, (int(x5), int(y5)))



        # Atualiza a tela com as mudanças feitas
        pygame.display.update()