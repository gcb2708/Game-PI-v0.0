"""
Arquivo para criação da classe Soldado
"""
import pygame
from auxiliar import tela, larguraTela, alturaTela, framesEsquerda, framesDireita, framesParado, framesPulo, \
    framesPuloE


class Soldado(object):

    def __init__(self, perX, perY, perW, perH, perImg):
        self.perX = perX            # Posição do personagem no eixo X
        self.perY = perY            # Posição do personagem no eixo Y
        self.perW = perW            # Largura da imagem do personagem
        self.perH = perH            # Altura da imagem do personagem
        self.perImg = perImg        # Imagem do personagem
        self.perVelX = 0            # Velocidade HORIZONTAL do personagem
        self.perVelY = 0            # Velocidade VERTICAL do personagem
        self.perAY = 445.73         # Aceleração VERTICAL do personagem
        self.walkCount = 0          # Contador para animação de andar
        self.jumpCount = 0          # Contador para animação do pulo
        self.teste_boost = 0        # Teste pro boost

    # Atualiza a posição HORIZONTAL do personagem
    def anda(self, boost):

        # Verifica a posição do personagem no eixo Y
        if self.perY < alturaTela - self.perW:
            boost = 0

        # Equação do MRU descrito pelo personagem no plano HORIZONTAL
        self.perX += (self.perVelX + boost) * (1/60)

        # verificar se existe boost
        if boost != 0:
            self.teste_boost = -1
        else:
            self.teste_boost = 0

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

        # .... depois atualiza-se a posição VERTICAL
        self.perY += self.perVelY * (1 / 60) + ((1 / 2) * self.perAY * (1 / 60) ** 2)

        # .... e por fim trava numa altura máxima
        # if self.perY <= 250:
        #    self.perY = 250
        #    self.perVelY = 0
        #   self.perAY = 2000

        # Trava o personagem na altura da tela
        if self.perY > alturaTela - self.perH:
            self.perY = alturaTela - self.perH
            self.perVelY = 0

        elif self.perY < 0:
            self.perY = 0
            self.perVelY = 0

        return True

    # trocar os frames do personagem
    def troca_frames(self, esquerda, direita, teste_dir, teste_pulo):
        # contador
        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.jumpCount + 1 >= 36:
            self.jumpCount = 0

        # varifica a posição do personagem no eixo Y
        if self.perY >= alturaTela - self.perW:
            teste_pulo = False

        # o personagem está pulando
        if teste_pulo:
            if esquerda:
                tela.blit(framesPuloE[self.jumpCount // 6], (self.perX, self.perY))
                self.jumpCount += 1

            elif direita:
                tela.blit(framesPulo[self.jumpCount // 6], (self.perX, self.perY))
                self.jumpCount += 1

            # o personagem so tem momento no eixo Y
            else:
                # teste da direção anterior
                if teste_dir == 0:
                    tela.blit(framesPuloE[self.jumpCount // 6], (self.perX, self.perY))
                    self.jumpCount += 1

                else:
                    tela.blit(framesPulo[self.jumpCount // 6], (self.perX, self.perY))
                    self.jumpCount += 1

        # o personagem não está pulando
        elif not teste_pulo:
            if esquerda:
                tela.blit(framesEsquerda[self.walkCount // (4 + self.teste_boost)], (self.perX, self.perY))
                self.walkCount += 1

            elif direita:
                tela.blit(framesDireita[self.walkCount // (4 + self.teste_boost)], (self.perX, self.perY))
                self.walkCount += 1

            else:
                if teste_dir == 0 or teste_dir == 1:
                    tela.blit(framesParado[teste_dir], (self.perX, self.perY))
                    self.walkCount = 0

        # personagem parado
        else:
            if teste_dir == 0 or teste_dir == 1:
                tela.blit(framesParado[teste_dir], (self.perX, self.perY))
                self.walkCount = 0

        pygame.display.update()
