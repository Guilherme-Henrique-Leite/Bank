class ContaBancaria():
    def __init__(self):
        self.saldo = 1000
        self.limite_diario = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f'Depósito: R$ {valor: .2f}\n'
            return True
        else: 
            return False
    
    def sacar(self, valor):
        if valor <= 0:
            return False, "Valor inválido"
        elif valor > self.saldo:
            return False, "Saldo insuficiente"
        elif valor > self.limite_diario:
            return False, "Limite diário de saque excedido!"
        elif self.numero_saques >= self.LIMITE_SAQUES:
            return False, "Número máximo de saques excedido"
        
        self.saldo -= valor
        self.extrato += f"Saque: R$ {valor: .2f}\n"
        self.numero_saques += 1
        return True, "Saque efetuado com sucesso."
    
    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
    

def nova_operacao(conta):
    while True:
        opcao = input("Deseja realizar outra operação? [S/N]: ").strip().upper()
        if opcao == "S":
            menu_principal(conta)
            break
        elif opcao == "N":
            print("Obrigado por utilizar nossos serviços!💰💲")
            break
        else:
            print("Opção inválida! Por favor, escolha [S] para Sim ou [N] para Não.")

def menu_principal(conta):
    while True:
        print("""
=====================================💲💲💲💲💲💲💲💲=====================================
                                Bem-vindos ao Central Bank!

[1] Acessar conta
[2] Consultar saldo rápido
[0] Sair

=====================================💲💲💲💲💲💲💲💲=====================================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_conta(conta)
        elif opcao == "2":
            conta.mostrar_extrato()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

    print("Obrigado por utilizar nossos serviços!💰💲")

def menu_conta(conta):
    while True:
        opcao = input("""
=====================================CENTRAL BANK=====================================
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=====================================💲💲💲💲💲💲💲💲=====================================
=> """)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            sucesso = conta.depositar(valor)
            if sucesso:
                print("Depósito realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
            nova_operacao(conta)
            break

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            sucesso, mensagem = conta.sacar(valor)
            print(mensagem)
            if sucesso:
                nova_operacao(conta)
            break

        elif opcao == "3":
            conta.mostrar_extrato()
            nova_operacao(conta)
            break
        elif opcao == "0":
            print('Obrigado por utilizar nossos serviços!💰💲')
            break
        else:
            print("Opção inválida!")

conta = ContaBancaria()
menu_principal(conta)
