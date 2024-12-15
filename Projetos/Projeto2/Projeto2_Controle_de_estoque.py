import os
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
    try:
        id_produto = int(input("Digite o ID do produto: "))
        for produto in estoque:
            if id_produto == produto['ID']:
                print("Já existe um produto com este ID, tente novamente utilizando um ID diferente.")
                return
        nome = input("Digite o nome do produto: ").capitalize()
        quantidade = int(input("Digite a quantidade deste produto no estoque: "))
        preco = float(input("Digite o preço da unidade deste produto: "))

        novo_produto = {"ID": id_produto, "nome": nome, "quantidade": quantidade, "preco": preco}
        estoque.append(novo_produto)
        print(f"\n O produto {nome} foi adicionado ao estoque.")
    except ValueError:
        print("Você digitou um valor inválido. Por favor, tente novamente.")

def listar_produtos(estoque):
    if not estoque:
        print("Não há produtos no estoque.")
    else:
        print("Produtos no estoque: \n")
        estoque.sort(key=lambda x: x['ID'])
        for produto in estoque:
            print(f"ID: {produto['ID']}, Nome: {produto['nome']}, "
                  f"Quantidade: {produto['quantidade']}, Preço: {produto['preco']}")

def atualizar_produto(estoque):
    listar_produtos(estoque)
    if not estoque:
        print("Não há produtos no estoque.")
    else:
        try:
            id_produto_atualizado = int(input("\nDigite o ID do produto a ser atualizado: "))
            for produto in estoque:
                if id_produto_atualizado == produto['ID']:
                    print("[1] - Nome.")
                    print("[2] - Quantidade.")
                    print("[3] - Valor.")
                    print("[4] - Retornar ao menu principal ")
                    opcao_atualizar = input("\nSelecione a opção a ser atualizada: ")
                    if opcao_atualizar == "1":
                        novo_nome = input("Digite o novo nome: ")
                        produto['nome'] = novo_nome
                        print(f"O nome atualizado do produto de ID {id_produto_atualizado} é: {produto['nome']}")
                    elif opcao_atualizar == "2":
                        nova_quantidade = input("Digite a quantidade atualizada: ")
                        produto['quantidade'] = nova_quantidade
                        print(f"A quantidade atualizada do produto de ID {id_produto_atualizado} é: {produto['quantidade']}")
                    elif opcao_atualizar == "3":
                        novo_preco = float(input("Digite o preço atualizado: "))
                        produto['preco'] = novo_preco
                        print(f"O preço atualizado do produto de ID {id_produto_atualizado} é: {produto['preco']}")
                    elif opcao_atualizar == "4":
                        print("Voltando ao menu principal...")
                        return
                    else:
                        print("Opção inválida, nenhum produto foi atualizado")
                    return
            print(f"Não foi encontrado nenhum produto com o ID {id_produto_atualizado}.")
        except ValueError:
            print("Você digitou um valor inválido. Por favor, tente novamente.")

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
        os.system("cls")
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            atualizar_produto(estoque)
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