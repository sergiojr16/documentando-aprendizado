import os

caminho_user = os.getenv('USERPROFILE')
caminho_pasta_screenshots = os.path.join(caminho_user, 'AppData', 'Local', 'Tibia', 'packages', 'Tibia', 'screenshots')

def organizar_screenshots():
    contar_prints = 0

    for arquivo in os.listdir(caminho_pasta_screenshots):
        if arquivo.endswith(".png"):
            try:
                data, hora, nome, origem_e_formato = arquivo.split("_")
                origem, formato = origem_e_formato.split(".")
            except:
                print(f"Não foi possível fazer o split do arquivo {arquivo}. ")
                continue

            pasta_nome = os.path.join(caminho_pasta_screenshots, nome)
            if not os.path.exists(pasta_nome):
                os.makedirs(pasta_nome)
                print(f"Pasta {pasta_nome} criada com sucesso. ")

            pasta_origem = os.path.join(pasta_nome, origem)
            if not os.path.exists(pasta_origem):
                os.makedirs(pasta_origem)

            caminho_screenshot_original = os.path.join(caminho_pasta_screenshots, arquivo)
            novo_nome = f"{nome}_{origem}_{data}_{hora}.{formato}"
            novo_caminho = os.path.join(pasta_origem, novo_nome)
            try:
                os.rename(caminho_screenshot_original, novo_caminho)
                contar_prints += 1
            except OSError as erro:
                print(f"Erro ao tentar renomear e mover o arquivo: {erro}")

            print(f"Arquivo {arquivo} movido e renomeado com sucesso. ")

    print(f"\nForam movidas {contar_prints} screenshots. \n")

if __name__ == "__main__":
    print("Iniciando organizador de screenshots...")
    organizar_screenshots()
    print("Todas as screenshots foram movidas com sucesso. Encerrando... ")
    os.system("pause")
