menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Criar novo usuário
[nc] Criar nova conta
[q] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

def deposito(saldo,valor,extrato,/):
    
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
        print(f"\nDeposito de R${valor} feito com sucesso")
           
    else:
        print("Operação invalida")
    
    return saldo,extrato     

def saque(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
        
    excedeu_limite = valor > limite
        
    excedeu_saque = numero_saques >= LIMITE_SAQUES
        
    if excedeu_saldo:
        print("Operação invalida, Saldo insuficiente")
            
    elif excedeu_limite:
        print("Operação invalida, Limite de saque excedido")
            
    elif excedeu_saque:
        print("Operação invalida, Numero de saques diarios excedido")
            
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        print(f"Saque: R${valor:.2f}")
        extrato += f'Saque: R${valor:.2f}\n'
            
    else:    
            print("Saldo suficiente ")
            
    return saldo, extrato    
 
def criar_usuario(usuarios):
    
    cpf = input("cpf: ").strip(".-")  #tentei passar um filtro para retirar .-, mas parece que não funcionou
    usuario = filtra_usuario(cpf,usuarios)

    if usuario:
        print("CPF já cadastrado")
        return
    
    nome = input("Nome Completo: ")
    data_de_nascimento = input("Data de nascimento(dd-mm-aaaa): ")
    endereco = input("Endereco(logradouro-nro-bairro-cidade/sigla): ")
    
    usuarios.append({"nome":nome,"data_nascimento":data_de_nascimento,"cpf":cpf,"endereco":endereco})
    
    print("Usuario criado com sucesso")

def filtra_usuario(cpf,usuarios):   #filtro criado igual do professor
    filtrar = [usuarios for usuarios in usuarios if usuarios["cpf"] == cpf]
    return filtrar[0] if filtrar else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("CPF: ")
    usuario = filtra_usuario(cpf,usuarios)
    
    if usuario:
        print("Conta criado")
        return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("Usuario não encontrado")
    
while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito:R$ "))
        saldo,extrato = deposito(saldo,valor,extrato)
                
    elif opcao == "s":
        valor = int(input("Informe o valor do saque: "))
        saldo,extrato = saque(saldo = saldo ,valor = valor,extrato = extrato,limite = limite,numero_saques = numero_saques,LIMITE_SAQUES = LIMITE_SAQUES)
             
    elif opcao == "e":
                             
        print("\nNão forma realizados movimentações" if not extrato else extrato)
        print(f"\nSaldo atual: R${saldo:.2f}\n")
    
    elif opcao == "nu":
        criar_usuario(usuarios)
    
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA,numero_conta,usuarios)
        
        if conta:
            contas.append(conta)
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione a operação desejada.")
    