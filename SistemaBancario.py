from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    entrada = input("Escolha qual operação deseja realizar: ")

    if(entrada == "d"):
        valor_deposito = float(input("Quanto deseja depositar? :"))

        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato += f"""
                Extrato\n
                Data: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n
                Valor depositado: + R${valor_deposito:.2f}\n
                Saldo: R${saldo:.2f}\n
            """
        else:
            print("Digite um valor válido")
    
    elif(entrada == "s"):
        saque = float(input("Informe o valor do saque: "))

        if(saque > limite):
            print("Limite excedido!")

        elif(saque > saldo):
            print("Saldo insuficiente!")
        
        elif(numero_saques > LIMITE_SAQUES):
            print("Número de saques excedido!")
        
        elif(saque > 0):
            saldo -= saque
            extrato += f"""
                Extrato\n
                Data: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n
                Saque: - R${saque:.2f}\n
                Saldo Restante: R${saldo:.2f}\n
            """

            numero_saques += 1
        
        else:
            print("Valor de saque inválido!")



    elif(entrada == "e"):
        print(extrato)

    elif(entrada == "q"):
        break

    else:
        print("Operação inválida, selecione as opções recomendadas!")
        