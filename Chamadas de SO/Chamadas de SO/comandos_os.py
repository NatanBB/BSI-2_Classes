import os
command = " "
while (command != "sair"):
    command = input("Digite o comando ou precione 1 para sair: ")
    if command == "1":
        break
    else:
        handle = os.popen(command)
        line = " "
        while line:
            line = handle.read()
            print(line)
        handle.close()
print('Tchau')