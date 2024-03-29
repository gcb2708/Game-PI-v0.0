"""
Arquivo principal do jogo
"""
import pygame
from classe_personagem import Soldado
from classe_aviao import Airplane
from auxiliar import tela, larguraTela, alturaTela, display_message, clock

pygame.init()


def game_start():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    intro = False
                    soldado_loop()

        tela.fill((255, 255, 255))
        display_message("Press Enter", (255, 0, 255))
        clock.tick(15)


def soldado_loop():
    # Criando o personagem com o modelo da classe Soldado
    carlinhos = Soldado(
        perX=larguraTela * 0.2,
        perY=alturaTela * 0.85,
        perW=88,
        perH=88,
        perImg=pygame.image.load('Imagens/SoldadoParado/SR1.png')
    )

    left = False
    right = False
    teste_dir = 1
    teste_pulo = False
    boost = 0

    while True:

        tela.fill((0, 0, 0))

        # tratamento dos eventos
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # botao foi pressionado
            if event.type == pygame.KEYDOWN:
                # esquerda
                if event.key == pygame.K_LEFT:
                    carlinhos.perVelX = -272.72
                    left = True
                    right = False
                    teste_dir = 0
                # direita
                elif event.key == pygame.K_RIGHT:
                    carlinhos.perVelX = 272.72
                    left = False
                    right = True
                    teste_dir = 1
                # pulo
                elif event.key == pygame.K_SPACE:
                    if carlinhos.perY >= alturaTela - carlinhos.perH:
                        carlinhos.perVelY = -300
                        teste_pulo = True

                elif event.key == pygame.K_LSHIFT:
                    if left:
                        boost = -100
                    elif right:
                        boost = 100

                # Quando apertada a tecla ESC, alterna para o aviao
                elif event.key == pygame.K_ESCAPE:
                    mct_loop()

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carlinhos.perVelX = 0
                    left = False
                    right = False

                if event.key == pygame.K_LSHIFT:
                    boost = 0

        carlinhos.pulo()

        if carlinhos.anda(boost):
            carlinhos.troca_frames(left, right, teste_dir, teste_pulo)

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def mct_loop():
    # Criando o avião com o modelo da classe Airplane
    aviao = Airplane(airX=0,
                     airY=alturaTela-128,
                     airW=128,
                     airH=128,
                     airImg=pygame.image.load('Imagens/Aviao/MCT.png'))

    while True:

        tela.fill((0, 0, 0))

        # tratamento dos eventos
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # botao foi pressionado
            if event.type == pygame.KEYDOWN:
                # esquerda
                if event.key == pygame.K_LEFT:
                    aviao.airAX = -50
                # direita
                elif event.key == pygame.K_RIGHT:
                    aviao.airAX = 50
                # cima
                elif event.key == pygame.K_UP:
                    aviao.airAY = -100
                # baixo
                elif event.key == pygame.K_DOWN:
                    aviao.airAY = 100

                # Quando apertada a tecla ESC, alterna para o personagem
                elif event.key == pygame.K_ESCAPE:
                    soldado_loop()

            # botao foi solto
            if event.type == pygame.KEYUP:
                # HORIZONTAL
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    aviao.airAX = 0
                # VERTICAL
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    aviao.airAY = 0

        if aviao.atualizaX():
            aviao.draw()

        if aviao.atualizaY():
            aviao.draw()

        if aviao.combustivel():
            game_start()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_start()

    pygame.quit()
    quit()
