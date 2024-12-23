import os

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"Cliente {self.nome} | Idade: {self.idade} anos | CPF: {self.cpf}"


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
            raise ValueError("O novo saldo deve ser um número.")

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

    def transferir(self, valor, conta_destino):
        pass

    def consultar_saldo(self):
        pass

    def registrar_historico(self):
        pass

    def consultar_historico(self):
        pass

    def __str__(self):
        return f"Conta {self.num_conta} | {self.pessoa}"


class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar_conta(self, conta):
        self.contas[conta.num_conta] = conta
        print(f"A conta {conta.num_conta} foi adicionada. ")

    def encontrar_conta(self, num_conta):
        return self.contas.get(num_conta)

    def listar_contas(self):
        if not self.contas:
            print("Não há contas cadastradas. ")
        else:
            for conta in self.contas.values():
                print(conta)


def menu_inicial():
    print("\n"+"-"*40)
    print("==== BEM VINDO AO BANCO EASY MONEY ====")
    print("-" * 40)
    print("[1] - Cadastrar novo cliente ")
    print("[2] - Já sou cliente ")
    print("[3] - Sair do banco ")
    print("-" * 40)


def cadastrar_cliente(banco):
    nome = input("Digite o nome do Cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    cpf = input("Digite o cpf do cliente: ")

    cliente = Pessoa(nome, idade, cpf)
    while True:
        try:
            num_conta = input("Digite o número da conta (4 dígitos): ")
            if len(num_conta) > 4:
                print("O número da conta possui mais de 4 dígitos. ")
            else:
                break
        except ValueError:
            print("Não foi digitado um valor válido, tente novamente. ")
    valida_cadastro(cliente, num_conta, banco)


def valida_cadastro(cliente, num_conta, banco):
    if num_conta in banco.contas.keys():
        print(f"Já existe uma conta {num_conta} cadastrada no sistema. ")
    else:
        conta = Conta(cliente, num_conta)
        banco.adicionar_conta(conta)


def menu_cliente():
    print("-" * 40)
    print("[1] - Sacar um valor ")
    print("[2] - Depositar um valor ")
    print("[3] - Tranferir um valor ")
    print("[4] - Consultar saldo da conta ")
    print("[5] - Consultar histórico de transações ")
    print("[6] - Voltar ao menu inicial ")
    print("[7] - Sair do banco ")
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
            while True:
                num_conta = int(input("Digite o número da conta: "))
                if num_conta not in banco.contas.keys:
                    print("Esta conta não existe em nosso sistema, tente novamente. ")
                else:
                    conta_logada = banco.encontrar_conta(num_conta)
                    break
            menu_cliente()
            opcao_cliente = input("Selecione uma das opções: ")
            if opcao_cliente == "1":
                conta_logada.sacar()
            elif opcao_cliente == "2":
                conta_logada.depositar()
            elif opcao_cliente == "3":
                conta_logada.transferir()
            elif opcao_cliente == "4":
                conta_logada.consultar_saldo()
            elif opcao_cliente == "5":
                conta_logada.consultar_historico()
            elif opcao_cliente == "6":
                continue
            elif opcao_cliente == "7":
                print("Saindo do banco...")
                break
        elif opcao == "3":
            print("Saindo do banco...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    sistema_bancario()
