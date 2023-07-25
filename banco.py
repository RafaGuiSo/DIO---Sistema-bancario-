menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        deposito = float(input("Informe o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print("Deposito feito com sucesso")
            
            
        else:
            print("Operação invalida")
            
        
    elif opcao == "s":
        saque = int(input("Informe o valor do saque: "))
        
        excedeu_saldo = saque > saldo
        
        excedeu_limite = saque > limite
        
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação invalida, Saldo insuficiente")
            
        elif excedeu_limite:
            print("Operação invalida, Limite de saque excedido")
            
        elif excedeu_saque:
            print("Operação invalida, Numero de saques diarios excedido")
            
        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            print(f"Saque: R${saque:.2f}")
            extrato += f'Saque: R${saque:.2f}\n'
            
        else:    
            print("Vc não possui saldo suficiente ")
        
        
    elif opcao == "e":
        print("Não forma realizados movimentações" if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione a operação desejada.")
    