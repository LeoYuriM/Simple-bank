
menu = """
####### Bem-vindo ao banco simples ########

s - Saque
d - depósito
e - Extrato
u - criar usuario
c - criar conta
f - Fechar

###########################################
"""

entrada_incorreta = """

===========================================
entrada incorreta! Digite um número válido!
===========================================

"""

valor_incorreto = """

===================================================
Valor incorreto! Insira um valor maior que 0 (Zero)
===================================================

"""



saldo = 0.0
extrato = ""
numero_de_saques = 0
limite_de_saques = 3
numero_contas = 0
usuarios = []
contas = []

def criar_usuario(usuarios):
    nome = input("Digite o nome: ")
    data_nascimento = input("data de nascimento: ")
    cpf = input("cpf, sem pontos ou traços: ")
    for usuario in usuarios:
        if cpf in usuario:
            print("Usuario ja cadastrado")
            return usuarios
    endereco = input("endereço - formato: logradouro, numero - bairro - cidade/sigla estado: ")
    usuario = [nome, data_nascimento, cpf, endereco]
    usuarios.append(usuario)
    return usuarios

def criar_conta(usuarios, contas, numero_contas):
    agencia = "0001"
    cpf_usuario = input("Digite o cpf do usuario: ")
    for usuario in usuarios:
        if cpf_usuario in usuario:
            numero_contas += 1
            conta = numero_contas
            conta_bancaria = [agencia, conta, cpf_usuario]
            contas.append(conta_bancaria)
            return contas, numero_contas
    print("Usuário não existe!")
    return contas, numero_contas
        

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor > 0:
            if valor <= saldo:
                if valor <= limite:
                    saldo -= valor
                    extrato+=f"Saque: R${valor:.2f}\n"
                    numero_saques+=1
                    print("Saque efetuado!")
                else:
                    print(f"Limite de R${limite} por saque ")
            else:
                print("Valor precisa ser menor ou igual ao saldo")
        else:
            print(valor_incorreto)
    else:
        print("numero de saques maximo atingido")
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Depósito efetuado!")
    else:
        print(valor_incorreto)
    return saldo, extrato

def mostrar_extrato(saldo,/,*,extrato):
    print("==================")
    print("não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo : R${saldo: .2f}")
    return

while True:
    # imprime o menu e recebe a escolha do usuario
    choice = input(menu)

    if choice == 's': # saque
        entrada = input("Digite o valor do saque: ")
        try:
            valor = float(entrada)
        except:
            print(entrada_incorreta)
            continue
        saldo, extrato = saque(saldo=saldo, valor=valor,extrato=extrato,limite=500,numero_saques=numero_de_saques, limite_saques=limite_de_saques)
    elif choice == 'd':
        entrada = input("Qual o valor do depósito? ")
        try:
            valor = float(entrada)
        except:
            print(entrada_incorreta)
            continue
        saldo, extrato = deposito(saldo, valor, extrato)
    elif choice == 'e':
        mostrar_extrato(saldo, extrato=extrato)
    elif choice == 'u':
        criar_usuario(usuarios)
        print(usuarios)
    elif choice == 'c':
        contas, numero_contas = criar_conta(usuarios, contas, numero_contas)
        print(contas)
    elif choice == 'f':
        break
    else:
        print("Opção errada!")


    
