from datetime import datetime


def menu():
    menu = """
    [entrar] Entrar no Sistema
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    => """
    return input(menu)

def menu_logado():
    menu_logado = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu_logado)



def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print(f"Data: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@@ Já existe usuário com esse CPF! @@@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("Usuário não encontrado. Criação de conta falhou.")

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}\nNúmero da Conta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}")

# TODO : Fazer função de transferência entre contas
"""
def transferencia(contas,usuarios, valor_transf, conta_transf):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        if(len(contas)>=2):
            for conta in contas:
                if(conta_transf in conta['numero_conta']):

            
    else:
        print("Usuário não encontrado. Criação de conta falhou.")
        

    #for conta in contas:
    #    print(conta)
"""

def acessar_sistema(agencia, contas):
    
    conta_user = int(input("Informe o numero da conta: "))
    
    for ct_user in contas:
        
        if(conta_user == ct_user['numero_conta']):
            print(f"{10*"#"}Seja bem vindo!{10*"#"}")
            print(f"Agencia: {agencia} - Conta: {conta_user}")
            return True
        else:
            print("Conta não encontrada!")
            return False


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    numero_conta = 1
    acesso_valido = False
    while True:
        opcao = menu()


        if opcao == "nc":
            criar_conta(AGENCIA, numero_conta, usuarios, contas)
            numero_conta += 1
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "entrar":
            # TODO: Melhorar esquema de acesso ao sistema
            
            acesso_valido = acessar_sistema(AGENCIA, contas=contas)


            if(acesso_valido):
                while True:
                    opcao_logado = menu_logado()

                    if opcao_logado == "d":
                        valor = float(input("Informe o valor do depósito: "))
                        saldo, extrato = deposito(saldo, valor, extrato)
                    elif opcao_logado == "s":
                        valor = float(input("Informe o valor do saque: "))
                        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
                    elif opcao_logado == "e":
                        exibir_extrato(saldo, extrato=extrato)
                    elif opcao_logado == "q":
                        print("Saindo da conta...")
                        break
                    else:
                        print("Operação inválida! Escolha novamente.")

        elif opcao == "q":
            break
        else:
            print("Operação inválida! Escolha novamente.")

main()