import os
comand = "mkdir teste"
pasta = os.popen(comand)
linha = os.getcwd()
print(linha)

cont = 0
while pasta != linha:
    dirc = os.listdir()
    print(dirc)
    cont += 1
    if cont == 100:
        break