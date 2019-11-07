"""
Arquivo para criação da classe Aviao
"""
from auxiliar import tela, larguraTela, alturaTela, display_message, fuel_message
import time


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
        self.gravity = 63.18        # Gravidade atuante sobre o avião
        self.fuel = 100             # Reservatório do combustível
        self.fuelCount = 0          # Decrementador do reservatório

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

        # O bloco de código a seguir trava o aviao na largura na tela
        if self.airX > larguraTela - self.airW:
            self.airX = larguraTela - self.airW
            self.airVelX = 0

        elif self.airX < 0:
            self.airX = 0
            self.airVelX = 0

        return True

    # Atualiza a posição VERTICAL do personagem
    def atualizaY(self):

        # verifica se está no solo
        if self.airX <= 30:
            if self.airY >= alturaTela - self.airH:
                self.airAY = 0

        # Primeiro calcula-se a velocidade VERTICAL .....
        self.airVelY += (self.airAY + self.gravity) * (1 / 60)

        # .... travando em uma velocidade máxima .....
        if self.airVelY >= 200:
            self.airVelY = 200

        # .... uma velocidade mínima ....
        elif self.airVelY <= -200:
            self.airVelY = -200

        # .... e depois atualiza-se a posição VERTICAL
        self.airY += self.airVelY * (1 / 60) + ((1 / 2) * (self.airAY + self.gravity) * (1 / 60) ** 2)

        # O bloco de código a seguir trava o aviao na altura na tela
        if self.airY > alturaTela - self.airH:
            self.airY = alturaTela - self.airH
            self.airVelY = 0

        elif self.airY < 0:
            self.airY = 0
            self.airVelY = 0

        return True

    def combustivel(self):
        # altualizar o valor do combustível
        if self.fuelCount >= 100:
            self.fuelCount = 0
        else:
            self.fuelCount += 0.001
            self.fuel -= 0.0001

        # verifica se o combustível acabou
        if self.fuel <= 0:
            self.airAY = 0
            self.airAX = 0
            self.fuel = 0
            display_message("Sem combustível!!!!", (255, 255, 255))

            if self.airY >= alturaTela - self.airH:
                time.sleep(2)
                return True

        # verifica se o avião levantou voo
        if self.airX <= 0 and self.airY >= alturaTela - self.airH:
            self.fuel = 100

        # verifica se tem aceleração em alguma direção
        if self.airAX != 0 or self.airAY != 0:
            self.fuel -= 0.0005

        fuel_message("Combustível: {:.2f} %".format(self.fuel), (255, 255, 255))
