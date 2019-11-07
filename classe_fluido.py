"""
Arquivo para criação da classe Fluido
"""

import math


class Fluido(object):

    def __init__(self, densidade, area, coefArr, ang, forcaArr):
        self.densidade = densidade
        self.areaSup = area
        self.coefArr = coefArr
        self.angulo = ang
        self.fArrX = forcaArr * math.sin(self.angulo)

    def arrasto(self, relatVel=63.18):
        pass
