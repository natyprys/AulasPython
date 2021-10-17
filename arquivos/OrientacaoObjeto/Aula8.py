def main():
    carro1 = Carro("Brasília", 1968, "Amarela", 80)
    carro2 = Carro("Fusca", 1981, "preto", 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velocidadeMax):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidadeMin = 0
        self.velocidadeMax = velocidadeMax


    def imprima (self):
        if self.velocidadeMin == 0:
            print("%s %s %d" %(self.modelo, self.cor, self.ano))
        elif self.velocidadeMin < self.velocidadeMax:
            print("%s %s indo a %d Km/h" %(self.modelo,self.cor, self.velocidadeMax))
        else:
            print("%s %s indo muito raaaapido" %(self.modelo, self.cor))


    def acelere (self, velocidade):
        self.velocidadeMin = velocidade
        if self.velocidadeMin > self.velocidadeMax:
            self.velocidadeMin = self.velocidadeMax
        self.imprima()


    def pare (self):
        self.velocidadeMin =0    

        