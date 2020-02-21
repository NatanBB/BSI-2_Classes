from macaco import *

alimentos = ["Banana", "Sopa de Macaco", "Empadão"]

def exibeMenu(macacos):
    menu = True
    print("1 - Criar macaco")
    print("2 - Ver macacos")
    print("3 - Sair ")
    selec = input("Selecione = ")
    print()

    if selec == "1":
        nome = input("Escolha um nome para o macaco: ")
        novo_macaco = Macaco(nome)
        macacos.append(novo_macaco)

    elif selec == "2":
        macacos = menuMacacos(macacos)

    elif selec == "3":
        menu = False
    else:
        print("Selecione uma opção válida\n")

    return menu, macacos

def menuMacacos(macacos):

    for i in range(len(macacos)):
        print("{} - {}".format(i+1, macacos[i].nome))

    selec = input("Selecione um macaco ou pressione Enter para sair =")
    if selec.isdigit():
        selec = int(selec)
        selec = selec -1
    else:
        return macacos

    while True:
        print("\n"*50)

        print("\nMACACO: {}".format(macacos[selec].nome))
        print("1 - Comer")
        print("2 - Ver bucho")
        print("3 - Digerir")
        print("4 - Sair")
        op = input("Selecione = ")
        print()

        if op == "1":
            exibeAlimentos()
            n = int(input("Selecione a comida: "))
            n = n - 1
            macacos[selec].comer(alimentos[n])

        elif op == "2":
            macacos[selec].verBucho()
            c = input("Pressione qualquer tecla para continuar...")

        elif op == "3":
            macacos[selec].digerir()
            c = input("Pressione qualquer tecla para continuar...")

        elif op == "4":
            break

    return macacos

def exibeAlimentos():
    print()
    for i in range(len(alimentos)):
        print("{} - {}".format(i+1, alimentos[i]))