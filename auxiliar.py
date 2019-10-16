""""
Arquivo para definir questões auxiliares
"""
import pygame

larguraTela = 800
alturaTela = 600

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Game PI v0.0")
pygame.display.set_icon(pygame.image.load('Imagens/icone tela.png'))
clock = pygame.time.Clock()

framesEsquerda = []

framesDireita = []

framesPulo = []


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
