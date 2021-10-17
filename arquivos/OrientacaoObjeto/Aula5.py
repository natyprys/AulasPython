class Poligono:
    def __init__(self, numero_de_lados):
        self.n = numero_de_lados
        self.lados = [0 for i in range (numero_de_lados)]

    def le_lados(self):
        self.lados = [float(input("Digite tamanho do lado" + str(i+1)))]    

    def mostra_lados(self):
        for i in range(self.n):
            print("Lado", i+1, "tem comprimento", self.lados[i])

class Triangulo(Poligono):
    def __init__(self):
        Poligono.__init__(self,3)

    def area(self):
        a,b,c = self.lados
        #calcula o semi-perimetro
        s= (a+b+c)/2
        area = (s*(s-1)*(s-b)*(s-c)) ** 0.5
        print("A área do triângulo é %0.2f" %area) 



