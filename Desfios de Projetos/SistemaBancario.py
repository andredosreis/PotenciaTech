
# instruções para o código
# Operações de depostito:"""
# o deposito só pode ser feito com valores positivos e so ter um usuário
# Saque:
# Permitido 3 saques diários com o limite maximo de R$ 500,00 por saque
# o Usuario tem que ter saldo positivo para realizar o saque, informar quando o cliente não tiver saldo
# todos os saques devem ser aramazenados em uma variavel e exibidos na iperação de extrato
# extrato:
# deve listar todos os depositos e saques realizados,
# no fim da listagem deve exibir o saldo atual do usuário ex: 1500,45 = R$ 1500,45"

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
limite_saque = 3

while True:
    print(menu)
    opcao = input("Digite a opção desejada: ")

    #deposito
    if opcao == "d":
        deposito = int(input("Digite o valor do deposito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito de R${deposito:.2f} realizado com sucesso!\n"
        
        else:
            print('numero invalido')
            
            
      

    #saque
    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))

        if saque > saldo:
            print("Saldo insuficiente!")
            
        elif saque > limite:
            print("Limite de saque diario excedido!")
        elif num_saques >= limite_saque:
            print("Limite de saque diario excedido!")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque de R${saque:.2f} realizado com sucesso!\n"
            num_saques += 1
    
            

        else:
            print("Opção inválida! o valor informado é invalido")

    #extrato
    elif opcao == "e":
        print("\n ================= Extrato =================\n")
        print(' Não foram realizados movimentações.' if not extrato else extrato)
        
             

        print(f"Saldo atual: R${saldo:.2f}")

        print("\n ==========================================\n")
        
        
        
        


    #sair do sistema
    elif opcao == "x":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
