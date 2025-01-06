import openpyxl

# Abrir arquivo excel e selecionar planilha ativa
arquivo = "loot_rares.xlsx"
workbook = openpyxl.load_workbook(arquivo)
sheet = workbook.active

# Ler cabeçalhos das colunas e identificar o índice delas
header = [celula.value for celula in next(sheet.iter_rows(max_row=1))]
col_index_ref = header.index("Referência")
col_index_item = header.index("Item")
col_index_onde = header.index("Onde")
col_index_valor = header.index("Valor")

# Processar os dados para agrupar os valores mensalmente
valor_mensal = {}

for linha in sheet.iter_rows(min_row=2, values_only=True):
    ref = linha[col_index_ref]
    valor = linha[col_index_valor]
    if isinstance(valor, (int, float)):
        if ref not in valor_mensal:
            valor_mensal[ref] = 0
        valor_mensal[ref] += valor

print(valor_mensal)




