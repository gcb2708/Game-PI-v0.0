from auxiliar import tela, larguraTela


class Soldado(object):

    def __init__(self, x, y, larg, alt, img):
        self.x = x
        self.y = y
        self.larg = larg
        self.alt = alt
        self.img = img
        self.vel = 5
        self.aY = 0

    def draw(self):
        tela.blit(self.img, (self.x, self.y))

    def andaDireita(self):
        self.x += self.vel

        if self.x > larguraTela - self.larg:
            self.x = larguraTela - self.larg

    def andaEsquerda(self):
        self.x -= self.vel

        if self.x < 0:
            self.x = 0