# Menu Principal
def menu_inicial():
    print("-"*40)
    print("==== Gerenciador de Atividadess ====")
    print("[1] - Adicionar Atividade")
    print("[2] - Listar Atividades")
    print("[3] - Marcar Atividade como concluída")
    print("[4] - Remover Atividade")
    print("[5] - Finalizar Programa")
    print("-"*40)

# Adicionar nova atividade
def adicionar_atividade(atividades):
    nova_atividade = input("Digite uma atividade a ser adicionada no gerenciador: ")
    atividades.append({"Atividade": nova_atividade, "Finalizada": False})
    print("Uma nova atividade foi adicionada.")


# Listar todas as atividades
def listar_atividade(atividades):
    if not atividades:
        print("Não há nenhuma atividade cadastrada. ")
    else:
        print("Lista de Atividades: ")
        indice = 1
        for a in atividades:
            if a["Finalizada"]:
                situacao_atividade = "Atividade Concluída"
            else:
                situacao_atividade = "Atividade Pendente"
            print(f"{indice}. {a['Atividade']} - {situacao_atividade}")
            indice += 1

# Marcar uma atividade como concluída
def concluir_atividade(atividades):
    listar_atividade(atividades)
    if not atividades:
        print("Ao menos uma atividade deve ser adicionada para executar esta função.")
    else:
        try:
            num_atividade = int(input("Digite o número da atividade a ser concluída: ")) -1
            if 0 <= num_atividade < len(atividades):
                 atividades[num_atividade]["Finalizada"] = True
                 print(f"A atividade {atividades[num_atividade]['Atividade']} foi marcada como 'Atividade Concluída' ")
            else:
                print("Digite um número válido.")
        except ValueError:
            print("Você digitou um valor inválido. Por favor, digite um número.")

# Remover uma atividade existente
def remover_atividade(atividades):
    listar_atividade(atividades)
    if not atividades:
        print("Ao menos uma atividade deve ser adicionada para executar esta função.")
    else:
        try:
            num_atividade = int(input("Digite o número da atividade a ser removida: ")) -1
            if 0 <= num_atividade < len(atividades):
                atividade_removida = atividades.pop(num_atividade)
                print(f"A atividade {atividade_removida['Atividade']} foi removida.")
            else:
                print("Digite um número válido.")
        except ValueError:
            print("Você digitou um valor inválido. Por favor, digite um número.")


# Programa principal
def gerenciador_de_atividades():
    atividades = []
    while True:
        menu_inicial()
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            adicionar_atividade(atividades)
        elif opcao == "2":
            listar_atividade(atividades)
        elif opcao == "3":
            concluir_atividade(atividades)
        elif opcao == "4":
            remover_atividade(atividades)
        elif opcao == "5":
            print("Finalizando Programa...")
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida: ")


# Inicio do Programa

if __name__ == "__main__":
    gerenciador_de_atividades()








