"""
Arquivo para criação da classe Soldado
"""
import pygame
from auxiliar import tela, larguraTela, alturaTela, framesEsquerda, framesDireita, framesParado, framesPulo


class Soldado(object):

    def __init__(self, perX, perY, perW, perH, perImg):
        self.perX = perX            # Posição do personagem no eixo X
        self.perY = perY            # Posição do personagem no eixo Y
        self.perW = perW            # Largura da imagem do personagem
        self.perH = perH            # Altura da imagem do personagem
        self.perImg = perImg        # Imagem do personagem
        self.perVelX = 0            # Velocidade HORIZONTAL do personagem
        self.perVelY = 0            # Velocidade VERTICAL do personagem
        self.perAY = 0              # Aceleração VERTICAL do personagem
        self.walkCount = 0          # Contador para animação de andar
        self.jumpCount = 0          # Contador para animação do pulo

    # Desenha na tela
    def draw(self):
        if self.jumpCount + 1 >= 36:
            self.jumpCount = 0

        self.jumpCount += 1

        tela.blit(framesPulo[self.jumpCount // 6], (self.perX, self.perY))
        pygame.display.update()

    # Atualiza a posição HORIZONTAL do personagem
    def anda(self):
        # Equação do MRU descrito pelo personagem no plano HORIZONTAL
        self.perX += self.perVelX

        # Trava o personagem na largura da tela
        if self.perX > larguraTela - self.perW:
            self.perX = larguraTela - self.perW

        elif self.perX < 0:
            self.perX = 0

        return True

    # Atualiza a posição VERTICAL do personagem
    def pulo(self):

        # Primeiro calcula-se a velocidade do MRUV da VERTICAL .....
        self.perVelY += self.perAY * (1 / 60)

        # .... depois atualiza-se a posição VERTICAL ....
        self.perY += self.perVelY * (1 / 60) + ((1 / 2) * self.perAY * (1 / 60) ** 2)

        # .... e por fim trava numa altura máxima
        if self.perY <= 250:
            self.perY = 250
            self.perVelY = 0

        # Trava o personagem na altura da tela
        if self.perY > alturaTela - self.perH:
            self.perY = alturaTela - self.perH
            self.perVelY = 0

        elif self.perY < 0:
            self.perY = 0
            self.perVelY = 0

        return True

    # Atualiza os frames quando o personagem anda para esquerda ou direita
    def troca_frames(self, left, right, teste_dir):

        tela.fill((0, 0, 0))

        # Limita o contado para permenecer em LOOP
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        # Se é verdade que o personagem se move para ESQUERDA,
        # então a lista com os frames da animação é percorrida.
        if left:
            tela.blit(framesEsquerda[self.walkCount // 3], (self.perX, self.perY))
            self.walkCount += 1

        # Se é verdade que o personagem se move para DIREITA,
        # então a lista com os frames da animação é percorrida.
        elif right:
            tela.blit(framesDireita[self.walkCount // 3], (self.perX, self.perY))
            self.walkCount += 1

        # Se o persoganem está parado, então percorre-se uma lista com
        # os frames dessa situação.
        # - Quando teste_dir == 0, personagem fica parado virado pra ESQUERDA
        # - Quando teste_dir == 0, personagem fica parado virado pra DIREITA
        else:
            if teste_dir == 0 or teste_dir == 1:
                tela.blit(framesParado[teste_dir], (self.perX, self.perY))
                self.walkCount = 0

        pygame.display.update()
