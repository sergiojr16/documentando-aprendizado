class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"Cliente {self.nome} | Idade: {self.idade} anos | CPF: {self.cpf}"


class Conta:
    def __init__(self, pessoa, numero_conta):
        self.numero_conta = numero_conta
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
        return f"Conta {self.numero_conta} | Cliente {self.pesssoa.nome}"


def menu_inicial():
    print("\n"+"-"*40)
    print("==== BEM VINDO AO BANCO EASY MONEY ====")
    print("-" * 40)
    print("[1] - Cadastrar novo cliente ")
    print("[2] - Já sou cliente ")
    print("[3] - Sair do banco ")
    print("-" * 40)


def cadastrar_cliente():
    pass


def menu_cliente():
    print("\n"+"-"*40)
    print(f"==== OLÁ ====")
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
    pass


if __name__ == "__main__":
    sistema_bancario()
