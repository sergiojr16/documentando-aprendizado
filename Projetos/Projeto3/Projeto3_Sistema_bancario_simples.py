import os

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"Cliente {self.nome}"


class Conta:
    def __init__(self, pessoa, num_conta):
        self.pessoa = pessoa
        self.num_conta = num_conta
        self.__saldo = 0.0
        self.historico = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if isinstance(novo_saldo, float):
            self.__saldo = novo_saldo
        else:
            raise ValueError("\nO novo saldo deve ser um número.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("\nNão há saldo suficiente para realizar esta transação. ")
        else:
            self.__saldo -= valor
            print(f"Foi realizado um saque no valor de R$ {valor:.2f}. \n"
                  f"Seu novo saldo é: R$ {self.__saldo:.2f}")
            self.registrar_historico(f"Saque de R$ {valor:.2f}")


    def depositar(self, valor):
        if valor < 0:
            print("\nValor inválido para depósito. ")
        else:
            self.__saldo += valor
            print(f"\nDeposito no valor de R$ {valor:.2f} realizado com sucesso. \n"
                  f"Seu novo saldo é: R$ {self.__saldo:.2f}")
            self.registrar_historico(f"Depósito de R$ {valor:.2f}")

    def transferir(self, valor, conta_destino):
        if valor > self.__saldo:
            print("\nNão há saldo suficiente para realizar esta transação. ")
        else:
            self.__saldo -= valor
            conta_destino.__saldo += valor
            print(f"Foi transferido R$ {valor:.2f} da conta {self.num_conta} para a conta {conta_destino}. ")
            print(f"O novo saldo da conta {self.num_conta} é: R$ {self.__saldo}. ")
            print(f"O novo saldo da conta {conta_destino.num_conta} é: R$ {conta_destino.__saldo}. ")
            self.registrar_historico(f"Transferência feita para {conta_destino} no valor de R$ {valor:.2f}")
            conta_destino.registrar_historico(f"Transferência recebida de {self.num_conta} no valor de R$ {valor:.2f}")


    def consultar_saldo(self):
        print(f"O saldo da conta {self.num_conta} é: R$ {self.__saldo}")

    def registrar_historico(self, registro):
        self.historico.append(registro)

    def consultar_historico(self):
        for historico in self.historico:
            print(f" - {historico}")

    def __str__(self):
        return f"Conta {self.num_conta} | {self.pessoa}"


class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        self.contas[conta.num_conta] = conta
        print(f"\nA conta {conta.num_conta} foi adicionada. ")

    def encontrar_conta(self, num_conta):
        return self.contas.get(num_conta)

    def listar_contas(self):
        if not self.contas:
            print("\nNão há contas cadastradas. ")
        else:
            print("\nLista de Contas Cadastradas: ")
            for conta in self.contas.values():
                print(conta)


def menu_inicial():
    print("\n"+"-"*40)
    print("==== BEM VINDO AO BANCO EASY MONEY ====")
    print("-" * 40)
    print("[1] - Cadastrar novo cliente ")
    print("[2] - Já sou cliente ")
    print("[3] - Consultar lista de clientes cadastrados ")
    print("[4] - Sair do banco ")
    print("-" * 40)


def cadastrar_cliente(banco):
    nome = input("Digite o nome do Cliente: ")
    try:
        idade = int(input("Digite a idade do cliente: "))
        cpf = int(input("Digite o cpf do cliente: "))
    except ValueError:
        print("\nNão foi digitado um valor válido, tente novamente. ")
        return

    cliente = Pessoa(nome, idade, cpf)
    try:
        num_conta = int(input("Digite o número da conta: "))
    except ValueError:
        print("\nNão foi digitado um valor válido, tente novamente. ")
        return
    valida_cadastro(cliente, num_conta, banco)


def valida_cadastro(cliente, num_conta, banco):
    if num_conta in banco.contas.keys():
        print(f"\nJá existe uma conta {num_conta} cadastrada no sistema. ")
    else:
        conta = Conta(cliente, num_conta)
        banco.adicionar_conta(conta)


def menu_cliente():
    print("\n"+"-" * 40)
    print("[1] - Sacar um valor ")
    print("[2] - Depositar um valor ")
    print("[3] - Tranferir um valor ")
    print("[4] - Consultar saldo da conta ")
    print("[5] - Consultar histórico de transações ")
    print("[6] - Voltar ao menu inicial ")
    print("-"*40)


def sistema_bancario():
    banco = Banco()
    while True:
        menu_inicial()
        opcao = input("Selecione uma das opções: ")
        os.system('cls')
        if opcao == "1":
            cadastrar_cliente(banco)
        elif opcao == "2":
            if not banco.contas.keys():
                print("\nNão há nenhuma conta cadastrada. ")
                continue
            while True:
                try:
                    num_conta = int(input("Digite o número da conta: "))
                    if num_conta not in banco.contas.keys():
                        print("\nEsta conta não existe em nosso sistema, tente novamente. ")
                    else:
                        conta_logada = banco.encontrar_conta(num_conta)
                        break
                except ValueError:
                    print("\nNão foi digitado um número válido, tente novamente. ")
            while True:
                menu_cliente()
                opcao_cliente = input("Selecione uma das opções: ")
                os.system('cls')
                if opcao_cliente == "1":
                    try:
                        valor = float(input("Qual valor deseja sacar de sua conta? "))
                        conta_logada.sacar(valor)
                    except ValueError:
                        print("\nNão foi digitado um número válido, tente novamente. ")
                elif opcao_cliente == "2":
                    try:
                        valor = float(input("Qual valor deseja depositar em sua conta? "))
                        conta_logada.depositar(valor)
                    except ValueError:
                        print("\nNão foi digitado um número válido, tente novamente. ")
                elif opcao_cliente == "3":
                    try:
                        valor = float(input("Qual valor deseja transferir de sua conta? "))
                        banco.listar_contas()
                        num_conta_destino = int(input("\nPara qual conta deseja fazer a transferência? "))
                        conta_destino = banco.encontrar_conta(num_conta_destino)
                        if conta_destino:
                            conta_logada.transferir(valor, conta_destino)
                        else:
                            print(f"\nA conta não foi encontrada. ")
                    except ValueError:
                        print("\nNão foi digitado um número válido, tente novamente. ")
                elif opcao_cliente == "4":
                    conta_logada.consultar_saldo()
                elif opcao_cliente == "5":
                    conta_logada.consultar_historico()
                elif opcao_cliente == "6":
                    break
                else:
                    print("\nOpção inválida, tente novamente.")
        elif opcao == "3":
            banco.listar_contas()
        elif opcao == "4":
            print("\nSaindo do banco...")
            break
        else:
            print("\nOpção inválida, tente novamente.")


if __name__ == "__main__":
    sistema_bancario()
