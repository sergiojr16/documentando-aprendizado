import os


def menu_inicial():
    print("\n"+"-"*40)
    print("==== Controle de Estoque ====")
    print("-" * 40)
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
                print("Já existe um produto com este ID, tente novamente utilizando um ID diferente.\n")
                listar_produtos(estoque)
                return
        nome = input("Digite o nome do produto: ").capitalize()
        quantidade = int(input("Digite a quantidade deste produto no estoque: "))
        preco = float(input("Digite o preço da unidade deste produto: "))
    except ValueError:
        print("Você digitou um valor inválido. Por favor, tente novamente.")
        return
    novo_produto = {"ID": id_produto, "nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(novo_produto)
    print(f"\n O produto {nome} foi adicionado ao estoque.")


def listar_produtos(estoque):
    if not estoque:
        print("\nNão há produtos no estoque.")
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
                    print("\nOpções:")
                    print("[1] - Nome.")
                    print("[2] - Quantidade.")
                    print("[3] - Preço.")
                    print("[4] - Retornar ao menu principal ")
                    opcao_atualizar = input("\nSelecione a opção a ser atualizada: ")
                    if opcao_atualizar == "1":
                        novo_nome = input("Digite o novo nome: ")
                        produto['nome'] = novo_nome
                        print(f"O nome atualizado do produto de ID {id_produto_atualizado} é: {produto['nome']}")
                    elif opcao_atualizar == "2":
                        nova_quantidade = int(input("Digite a quantidade atualizada: "))
                        produto['quantidade'] = nova_quantidade
                        print(f"A nova quantidade do produto de ID {id_produto_atualizado} é: {produto['quantidade']}")
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
        except ValueError:
            print("Você digitou um valor inválido. Por favor, tente novamente.")
            return
        print(f"Não foi encontrado nenhum produto com o ID {id_produto_atualizado}.")


def remover_produto(estoque):
    listar_produtos(estoque)
    if not estoque:
        print("Não há produtos no estoque. ")
    else:
        try:
            id_removido = int(input("\nDigite o ID do produto que deseja remover: "))
        except ValueError:
            print("Você digitou um valor inválido. Por favor, tente novamente.")
            return
        for produto in estoque:
            if id_removido == produto['ID']:
                confirmacao = input(f"\nO produto {produto['nome']} de ID {produto['ID']} será removido "
                                    f"permanentemente, você confirma a ação? [S]/[N]: ").upper()
                if confirmacao not in ["S", "N"]:
                    print("\nOpção inválida, tente novamente.")
                elif confirmacao == "N":
                    print("\nNenhum produto foi removido.")
                else:
                    estoque.remove(produto)
                    print(f"\nO produto com ID {produto['ID']} foi removido. ")
                return
        print(f"Não foi encontrado nenhum produto com o ID {id_removido}.")


def salvar_estoque(estoque):
    with open("dados_estoque.txt", "w") as dados:
        for produto in estoque:
            linha = f"{produto['ID']}, {produto['nome']}, " \
                    f"{produto['quantidade']}, {produto['preco']}"
            dados.write(linha)
    print("\nOs dados do estoque foram salvos com sucesso.")


def abrir_estoque(estoque):
    if os.path.exists("dados_estoque.txt"):
        with open("dados_estoque.txt", "r") as dados:
            for linha in dados:
                id_produto = int(linha.strip().split(",")[0])
                nome = linha.strip().split(",")[1]
                quantidade = linha.strip().split(",")[2]
                preco = linha.strip().split(",")[3]
                estoque.append({"ID": id_produto, "nome": nome, "quantidade": quantidade, "preco": preco})
            print("\nOs dados do estoque foram carregados. ")
    else:
        print("\nNão foram encontrados dados no estoque, criando novo estoque...")


def controle_de_estoque():
    estoque = []
    abrir_estoque(estoque)
    while True:
        menu_inicial()
        opcao = input("Selecione uma opção: ")
        os.system('cls')
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            atualizar_produto(estoque)
        elif opcao == "4":
            remover_produto(estoque)
        elif opcao == "5":
            salvar_estoque(estoque)
        elif opcao == "6":
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida, tente novamente.")
        input("\n\n\n\nAperte Enter para continuar...")
        os.system('cls')


if __name__ == "__main__":
    controle_de_estoque()
