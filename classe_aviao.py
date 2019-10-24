"""
Arquivo para criação da classe Aviao
"""
from auxiliar import tela, larguraTela, alturaTela


class Airplane(object):

    def __init__(self, airX, airY, airW, airH, airImg):
        self.airX = airX            # Posição do avião no eixo X
        self.airY = airY            # Posição do avião no eixo Y
        self.airW = airW            # Largura da imagem do avião
        self.airH = airH            # Altura da imagem do avião
        self.airImg = airImg        # Imagem do avião
        self.airVelX = 0            # Velocidade HORIZONTAL
        self.airVelY = 0            # Velocidade VERTICAL
        self.airAX = 0              # Aceleração HORIZONTAL
        self.airAY = 0              # Aceleração VERTICAL
        self.airARR = 0             # Coeficiente de ARRASTO do avião

    def draw(self):
        tela.blit(self.airImg, (self.airX, self.airY))

    # Atualiza a posição HORIZONTAL do aviao
    def atualizaX(self):

        # Primeiro calcula-se a velocidade HORIZONTAL .....
        self.airVelX += self.airAX * (1 / 60)

        # .... travando em uma velocidade máxima .....
        if self.airVelX >= 200:
            self.airVelX = 200

        # .... uma velocidade mínima ....
        elif self.airVelX <= -200:
            self.airVelX = -200

        # .... e depois atualiza-se a posição HORIZONTAL
        self.airX += self.airVelX * (1 / 60) + ((1 / 2) * self.airAX * (1 / 60) ** 2)

        """
        O bloco de código a seguir trava o objeto na tela
        """
        if self.airX > larguraTela - self.airW:
            self.airX = larguraTela - self.airW
            self.airVelX = 0

        elif self.airX < 0:
            self.airX = 0
            self.airVelX = 0

        return True

    # Atualiza a posição VERTICAL do personagem
    def atualizaY(self):

        # Primeiro calcula-se a velocidade VERTICAL .....
        self.airVelY += self.airAY * (1 / 60)

        # .... travando em uma velocidade máxima .....
        if self.airVelY >= 200:
            self.airVelY = 200

        # .... uma velocidade mínima ....
        elif self.airVelY <= -200:
            self.airVelY = -200

        # .... e depois atualiza-se a posição VERTICAL
        self.airY += self.airVelY * (1 / 60) + ((1 / 2) * self.airAY * (1 / 60) ** 2)

        """
        O bloco de código a seguir trava o objeto na tela
        """
        if self.airY > alturaTela - self.airH:
            self.airY = alturaTela - self.airH
            self.airVelY = 0

        elif self.airY < 0:
            self.airY = 0
            self.airVelY = 0

        return True
