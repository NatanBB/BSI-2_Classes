# Fazer um programa, usando funções, que possua as seguintes funções:
# - Opção 1: coleta de informações do sistema, executa o comando uname -a e retorna as informações ao usuário
# - Opção 2: uso do disco, executa comando df -h e retorna as informações ao usuário
# - Opção 3: ping, pede o host e executa um ping host retornando as informações ao usuário
# - Opção 4: sair do sistema

import os

def exibeMenu(comando):
    menu = True
    while menu:
        print("1 - Coletar informações")
        print("2 - Uso do disco")
        print("3 - Ping")
        print("4 - Sair ")
        selec = input("Selecione uma opção = ")
        print()

        if selec == "1":
            comando = 'uname -a'
            exe = os.system(comando)
            print(exe)

        elif selec == "2":
            comando = 'df -h'
            exe = os.system(comando)
            print(exe)

        elif selec == "3":
            host = input('Digite seu ip:')
            comando = 'ping {}'.format(host)
            exe = os.system(comando)

        elif selec == "4":
            menu = False

        else:
            print('Erro! Opção inválida')

exibeMenu(True)