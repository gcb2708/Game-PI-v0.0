"""
Arquivo para criação da classe Soldado
"""
from auxiliar import tela, larguraTela, framesEsquerda, framesDireita, framesPulo


class Soldado(object):

    def __init__(self, perX, perY, perW, perH, perImg):
        self.perX = perX
        self.perY = perY
        self.perW = perW
        self.perH = perH
        self.perImg = perImg
        self.perVel = 5
        self.perAY = 0

    def draw(self):
        tela.blit(self.perImg, (self.perX, self.perY))

    def andaDireita(self):
        self.perX += self.perVel

        if self.perX > larguraTela - self.perW:
            self.perX = larguraTela - self.perW

        """
        Insirir o código para animação correndo para direita AQUI !!!!!!!!!!!!!
        """

    def andaEsquerda(self):
        self.perX -= self.perVel

        if self.perX < 0:
            self.perX = 0

        """
        Insirir o código para animação correndo para esquerda AQUI !!!!!!!!!!!!
        """

    def stop(self):
        self.perX = 0

   # def pulo(self):
