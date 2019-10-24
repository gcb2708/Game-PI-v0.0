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
        perY=alturaTela * 0.9,
        perW=103,
        perH=97,
        perImg=pygame.image.load('Imagens/mario.png')
    )

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
                    carlinhos.perVelX = -5
                # direita
                elif event.key == pygame.K_RIGHT:
                    carlinhos.perVelX = 5
                # pulo
                elif event.key == pygame.K_SPACE:
                    carlinhos.perAY = -1000

                # Quando apertada a tecla ESC, alterna para o aviao
                elif event.key == pygame.K_ESCAPE:
                    mct_loop()

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carlinhos.perVelX = 0
                elif event.key == pygame.K_SPACE:
                    carlinhos.perAY = 1000

        if carlinhos.anda():
            carlinhos.draw()

        if carlinhos.pulo():
            carlinhos.draw()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def mct_loop():
    # Criando o avião com o modelo da classe Airplane
    aviao = Airplane(airX=50,
                     airY=400,
                     airW=128,
                     airH=128,
                     airImg=pygame.image.load('Imagens/MCT.png'))

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
                    aviao.airAX = -200
                # direita
                elif event.key == pygame.K_RIGHT:
                    aviao.airAX = 200
                # cima
                elif event.key == pygame.K_UP:
                    aviao.airAY = -200
                # baixo
                elif event.key == pygame.K_DOWN:
                    aviao.airAY = 200

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

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_start()

    pygame.quit()
    quit()
