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
        display_message("Press Start", (255, 0, 255))
        clock.tick(15)


def soldado_loop():
    # Criando o personagem com o modelo da classe Soldado
    carlinhos = Soldado(
        perX=larguraTela * 0.45,
        perY=alturaTela * 0.8,
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
                    carlinhos.perVel = -10
                # direita
                elif event.key == pygame.K_RIGHT:
                    carlinhos.perVel = 10
                elif event.key == pygame.K_ESCAPE:
                    if event.key == pygame.K_SPACE:
                        mct_loop()

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carlinhos.perVel = 0

        if carlinhos.atualizaX():
            carlinhos.draw()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


def mct_loop():
    # Criando o avião com o modelo da classe Airplane
    aviao = Airplane(airX=128,
                     airY=128,
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
                    aviao.airVel = -10
                # direita
                elif event.key == pygame.K_RIGHT:
                    aviao.airVel = 10

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    aviao.airVel = 0

        if aviao.atualizaX():
            aviao.draw()

        # atualiza a tela
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_start()

    pygame.quit()
    quit()
