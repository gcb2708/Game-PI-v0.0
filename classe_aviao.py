from auxiliar import tela


class Aviao(object):

    def __init__(self, airX, airY, airW, airH, airImg):
        self.airX = airX
        self.airY = airY
        self.airW = airW
        self.airH = airH
        self.airImg = airImg
        self.airVel = 0
        self.airAX = 0
        self.airAY = 0
        self.airARR = 0

    def draw(self):

        tela.blit(self.airImg, (self.airX, self.airY))
