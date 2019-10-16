import pygame
from classe_personagem import Soldado
from auxiliar import larguraTela, alturaTela, persEsquerda, persDireita

carlinhos = Soldado(x=larguraTela*0.45,
                    y=alturaTela*0.8,
                    larg= 100,
                    alt= 100,
                    img= pygame.image.load('Imagens/mario.png'))


