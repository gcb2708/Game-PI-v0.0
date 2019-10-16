from auxiliar import tela, larguraTela


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

    def andaEsquerda(self):
        self.perX -= self.perVel

        if self.perX < 0:
            self.perX = 0