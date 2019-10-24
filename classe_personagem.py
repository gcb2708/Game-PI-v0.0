"""
Arquivo para criação da classe Soldado
"""
from auxiliar import tela, larguraTela, alturaTela, framesEsquerda, framesDireita, framesPulo


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

    # Desenha na tela
    def draw(self):
        tela.blit(self.perImg, (self.perX, self.perY))

    # Atualiza a posição HORIZONTAL do personagem
    def anda(self):
        self.perX += self.perVelX

        if self.perX > larguraTela - self.perW:
            self.perX = larguraTela - self.perW

        elif self.perX < 0:
            self.perX = 0

        return True

    # Atualiza a posição VERTICAL do personagem
    def pulo(self):

        # Primeiro calcula-se a velocidade VERTICAL .....
        self.perVelY += self.perAY * (1 / 60)

        # .... depois atualiza-se a posição VERTICAL ....
        self.perY += self.perVelY * (1 / 60) + ((1 / 2) * self.perAY * (1 / 60) ** 2)

        # .... e por fim trava numa altura máxima
        if self.perY <= 250:
            self.perY = 250
            self.perVelY = 0

        """
        O bloco de código a seguir trava o objeto na tela
        """
        if self.perY > alturaTela - self.perH:
            self.perY = alturaTela - self.perH
            self.perVelY = 0

        elif self.perY < 0:
            self.perY = 0
            self.perVelY = 0

        return True
