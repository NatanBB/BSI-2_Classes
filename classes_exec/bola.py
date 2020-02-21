# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class Ball:
    def __init__(self, color="unknown", circunf=0, material="unknown"):
        self.color = color
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input("Deseja mudar a cor atual {}? [sim/nao]".format(self.color))

        troca = troca[0].lower()

        if troca == "sim":
            nova_cor = input("\n> Nova Cor: ")
            self.color = nova_cor
        else:
            print("A cor continua ser {}".format(self.color))

    def mostraCor(self):
        print("\nA cor atual é {}".format(self.color))


def main():
    bola01 = Ball("azul", 5, "metal")

    while True:
        bola01.mostraCor()
        bola01.trocaCor()

        continuar = input("Continuar? [sim/nao]")
        continuar = continuar[0].lower()
        if continuar == "nao":
            break

    bola01.mostraCor()


main()