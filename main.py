"""
Arquivo principal do jogo
"""
import pygame
from classe_personagem import Soldado
from classe_aviao import Aviao
from auxiliar import tela, larguraTela, alturaTela, text_objects, display_message, clock

pygame.init()


def game_start():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    intro = False
                    game_loop()

        tela.fill((255, 255, 255))
        display_message("Press Start", (255, 0, 255))
        clock.tick(15)


def game_loop():
    # Criando o personagem com o modelo da classe Soldado
    carlinhos = Soldado(
        perX=larguraTela * 0.45,
        perY=alturaTela * 0.8,
        perW=100,
        perH=100,
        perImg=pygame.image.load('Imagens/mario.png')
    )

    """
    # Criando o aviao com o modelo da classe Aviao
    aviao = Aviao(
        airX=larguraTela * 0.1,
        airY=alturaTela * 0.2,
        airW=100,
        airH=100,
        airImg=pygame.image.load('Imagens/MCT.png')
    )
    """
    while True:
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
                    carlinhos.andaEsquerda()
                # direita
                elif event.key == pygame.K_RIGHT:
                    carlinhos.andaEsquerda()

            # botao foi solto
            if event.type == pygame.KEYUP:
                # esquerda ou direia
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carlinhos.stop()


if __name__ == '__main__':
    game_start()

    pygame.quit()
    quit()
