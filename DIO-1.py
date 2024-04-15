
menu = """
####### Bem-vindo ao banco simples ########

s - Saque
d - depósito
e - Extrato
f - Fechar

###########################################
"""

entrada_incorreta = """

=====================
entrada incorreta!
=====================

"""

valor_incorreto_deposito = """

===================================================
Valor incorreto! Insira um valor maior que 0 (Zero)
===================================================

"""

valor_incorreto_saque = """

===================================================
Valor incorreto! Insira um valor maior que 0 (Zero),
menor ou igual ao saldo, e menor ou igual a R$500,00
===================================================

"""

saldo = 0.0
extrato = ""
numero_de_saques = 3

while True:
    # imprime o menu e recebe a escolha do usuario
    choice = input(menu)

    if choice == 's': # saque
        if numero_de_saques > 0:
            print(f"Saques:{numero_de_saques}")
            entrada = input("Qual o valor do saque? ")
        else:
            print("numero de saques maximo atingido")
            continue
        try:
            valor = float(entrada)
        except:
            print(entrada_incorreta)
            continue
        if valor > 0 and valor <= saldo and valor <= 500.0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            print("saque efetuado!")
            numero_de_saques -= 1
        else:
            print(valor_incorreto_saque)
    elif choice == 'd':
        entrada = input("Qual o valor do depósito? ")
        try:
            valor = float(entrada)
        except:
            print(entrada_incorreta)
            continue
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor: .2f}\n"
            print("depósito efetuado!")
        else:
            print(valor_incorreto_deposito)
    elif choice == 'e':
        print("==================")
        print("não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo : R${saldo: .2f}")
    elif choice == 'f':
        break
    else:
        print("Opção errada!")