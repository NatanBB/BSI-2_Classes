from clientes import Cliente
from contas import Conta
natan = Cliente("Natan Borba Boos", "99259-4069")
marcos = Cliente("Marcos Andrei Rocha", "99272-4402")
conta1 = Conta([natan], 1, 5000)
conta2 = Conta([marcos], 2, 3000)
conta1.saque(100)
conta2.deposito(300)
conta1.saque(90)
conta2.deposito(90.25)
conta2.saque(250)
conta1.extrato()
conta2.extrato()