from macaco import *
from menu import *

macacos = []
menu = True

while menu:
    print("\n"*50)
    menu, macacos = exibeMenu(macacos)

print("Finalizando...")