class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, objeto):
        self.bucho.append(objeto)

    def verBucho(self):
        print("Coisas no Bucho: ")
        for i in self.bucho:
            print(i)
        print("...")

    def digerir(self):
        print("Digerindo...")
        self.verBucho()
        self.bucho = []