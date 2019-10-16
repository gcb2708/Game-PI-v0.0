"""
Arquivo para criação da classe Soldado
"""
from auxiliar import tela, larguraTela, framesEsquerda, framesDireita, framesPulo


class Soldado(object):

    def __init__(self, perX, perY, perW, perH, perImg):
        self.perX = perX            # Posição do personagem no eixo X
        self.perY = perY            # Posição do personagem no eixo Y
        self.perW = perW            # Largura da imagem do personagem
        self.perH = perH            # Altura da imagem do personagem
        self.perImg = perImg        # Imagem do personagem
        self.perVel = 0             # Velocidade HORIZONTAL do personagem
        self.perAY = 0              # Aceleração VERTICAL do personagem

    # Desenha na tela
    def draw(self):
        tela.blit(self.perImg, (self.perX, self.perY))

    # Atualiza a posição HORIZONTAL do personagem para direita
    def atualizaX(self):
        self.perX += self.perVel

        if self.perX > larguraTela - self.perW:
            self.perX = larguraTela - self.perW

        elif self.perX < 0:
            self.perX = 0

        """
        Insirir o código para animação correndo para direita AQUI !!!!!!!!!!!!!
        """

        return True

    # Atualiza a posição VERTICAL do personagem
    # def pulo(self):
