"""
Arquivo para criação da classe Aviao
"""
from auxiliar import tela, larguraTela


class Airplane(object):

    def __init__(self, airX, airY, airW, airH, airImg):
        self.airX = airX            # Posição do avião no eixo X
        self.airY = airY            # Posição do avião no eixo Y
        self.airW = airW            # Largura da imagem do avião
        self.airH = airH            # Altura da imagem do avião
        self.airImg = airImg        # Imagem do avião
        self.airVel = 0             # Velocidade do avião
        self.airAX = 0              # Aceleração HORIZONTAL
        self.airAY = 0              # Aceleração VERTICAL
        self.airARR = 0             # Coeficiente de ARRASTO do avião

    def draw(self):
        tela.blit(self.airImg, (self.airX, self.airY))

    # Atualiza a posição HORIZONTAL do personagem
    def atualizaX(self):
        self.airX += self.airVel

        if self.airX > larguraTela - self.airW:
            self.airX = larguraTela - self.airW

        elif self.airX < 0:
            self.airX = 0

        return True
