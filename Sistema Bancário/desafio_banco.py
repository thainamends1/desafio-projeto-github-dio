menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':

        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"   
        else:
            print("Operação inválida!")

    elif opcao == '2':
        
        if (saldo == 0):
            print("Você não possui saldo suficiente.")
        else:

            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Você não possui saldo suficiente.")

            elif excedeu_limite:
                print("O valor de saque excede o limite.")

            elif excedeu_saques:
                print("Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

    elif opcao == '3':
        print("\n--------EXTRATO--------\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------\n")

    elif opcao == '0':
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
