import os
comand = "mkdir teste"
pasta = os.popen(comand)
linha = os.getcwd()
print(linha)

cont = 0
while pasta != linha:
    dirc = os.listdir()
    print(dirc) #Mostra o caminho
    cont += 1
    if cont == 50: #Cont até 55 porque ele demora para criar o diretório
        break