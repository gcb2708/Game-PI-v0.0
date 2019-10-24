""""
Arquivo para definir questões auxiliares
"""
import pygame

larguraTela = 800
alturaTela = 600

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Soldado Carlinhos")
pygame.display.set_icon(pygame.image.load('Imagens/OutrasImagens/iconeTela.png'))
clock = pygame.time.Clock()

framesEsquerda = [pygame.image.load('Imagens/SoldadoLeft/L00.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L01.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L02.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L03.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L04.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L05.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L06.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L07.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L08.png'),
                  pygame.image.load('Imagens/SoldadoLeft/L09.png')]

framesDireita = [pygame.image.load('Imagens/SoldadoRight/R00.png'),
                 pygame.image.load('Imagens/SoldadoRight/R01.png'),
                 pygame.image.load('Imagens/SoldadoRight/R02.png'),
                 pygame.image.load('Imagens/SoldadoRight/R03.png'),
                 pygame.image.load('Imagens/SoldadoRight/R04.png'),
                 pygame.image.load('Imagens/SoldadoRight/R05.png'),
                 pygame.image.load('Imagens/SoldadoRight/R06.png'),
                 pygame.image.load('Imagens/SoldadoRight/R07.png'),
                 pygame.image.load('Imagens/SoldadoRight/R08.png'),
                 pygame.image.load('Imagens/SoldadoRight/R09.png')]

framesParado = [pygame.image.load('Imagens/SoldadoParado/SL1.png'),
                pygame.image.load('Imagens/SoldadoParado/SR1.png')]


# renderiza o texto
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# apresenta texto na tela
def display_message(text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 115)

    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (larguraTela / 2, alturaTela / 2)

    tela.blit(TextSurf, TextRect)
    pygame.display.update()
