def menu_inicial():
    print("-"*40)
    print("[1] - Adicionar produto ")
    print("[2] - Listar produtos ")
    print("[3] - Atualizar produto ")
    print("[4] - Remover produto ")
    print("[5] - Salvar dados ")
    print("[6] - Finalizar programa ")
    print("-"*40)

def adicionar_produto(estoque):
    id_produto = input("Digite o ID do produto: ")
    nome = input("Digite o nome do produto: ").capitalize()
    quantidade = int(input("Digite a quantidade deste produto no estoque: "))
    preco = float(input("Digite o preço da unidade deste produto: "))

    novo_produto = {"ID": id_produto, "nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(novo_produto)
    print(f"{nome} foi adicionado ao estoque.")

def listar_produtos(estoque):
    pass

def atualizar_produto():
    pass

def remover_produto():
    pass

def salvar_estoque():
    pass

def abrir_estoque():
    pass

def controle_de_estoque():
    estoque =[]
    while True:
        menu_inicial()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    controle_de_estoque()