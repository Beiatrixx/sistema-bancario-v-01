menu = """
Bem Vindo ao Banco Pixy, como podemos te ajudar?
             
Escolha a operação desejada:

[1] Depósito
[2] Saque
[3] Extrato
[0] SAIR
             
"""

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
            
        else:
            print("Valor informado é inválido, sua operação falhou!")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = quantidade_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print(f"Operação falhou! Valor do saque excede o limite de R$ {limite}.")

        elif excedeu_saques:
            print("Operação falhou! Limite de 3 saques diários atingido. Volte amanhã!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            quantidade_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Valor informado é inválido, sua operação falhou!")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * 29)
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida! Digite novamente a operação desejada.")