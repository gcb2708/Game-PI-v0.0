import pygame
from classe_personagem import Soldado
from auxiliar import larguraTela, alturaTela

pygame.init()


# def game_start():

def game_loop():
    # Criando o personagem com o modelo da classe Soldado
    carlinhos = Soldado(perX=larguraTela * 0.45,
                        perY=alturaTela * 0.8,
                        perW=100,
                        perH=100,
                        perImg=pygame.image.load('Imagens/mario.png'))

    # Criando o aviao com o modelo da classe Aviao


if __name__ == '__main__':
    game_loop()

    pygame.quit()
    quit()
