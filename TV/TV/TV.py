class televisor:
    def __init__(self, canal="1", volume="35"):
        self.canal = canal
        self.volume = volume

    def canal(self):
        return self.__canal

    def canal(self, numero):
        if numero.isdigit():
            num = int(numero)
            if num > 0 and num <= 50:
                self.__canal = num
            else:
                print("Canal Inválido")

        else:
            print("O canal deve ser apenas números!")

    def volume(self):
        return self.__volume

    def volume(self, numero):
        if numero.isdigit():
            num = int(numero)
            self.__volume = num
            if num >= 0 and num <= 100:
                self.__volume = num
        else:
            print("O volume deve ser apenas números!")


    def mudaCanal(self):
        print('Canal atual: {}'.format(self.canal))
        num = input("Mudar para o canal: ")
        self.canal = num

    def mudaVolume(self):
        print('Volume {}'.format(self.volume))
        num = input("Mudar para o volume: ")
        self.volume = num

    def __str__(self):
        return "Canal atual: {} \nVolume: {}\n ".format(self.canal, self.volume)

def exibeMenu():
    tv01 = televisor()

    while True:
        print("\n"*40)
        print(tv01)
        print("Selecione uma opção:")
        print("1 - Mudar de canal")
        print("2 - Mudar o volume")
        print("3 - Desligar a TV\n")
        selec = input("Selecionar:")

        if selec == "1":
            tv01.mudaCanal()

        elif selec == "2":
            tv01.mudaVolume()

        elif selec == "3":
            print("Desligando")
            break

        else:
            print("Selecione uma opção válida!")

exibeMenu()