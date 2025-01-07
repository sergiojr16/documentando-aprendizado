# Automação para leitura e análise da planilha "loot_rares"

## 1. Programa principal
- Abre a planilha para realizar as análises;
- O loop principal faz o menu inicial aparecer até o que o usuário decida sair do programa;
- É possível escolher: "analisar o histórico", "análises mensais" ou finalizar o sistema;
- Escolhendo "analisar o histórico", a função "analisa_historico_valores_mensais" é chamada
e ao final, é dada a possibilidade de salvar um novo arquivo com as análises através da função
"criar_novo_arquivo";
- Escolhendo "análises mensais", será solicitado o período de análise e dadas as opções de 
chamar as funções "analisa_valores_mensais", "analisa_origem_valores" e "analisa_quantidade_items";
- A opção "finalizar o sistema" encerra a aplicação.

## 2. Analisar histórico dos valores mensais
- Esta função itera todas as linhas da planilha armazenando os períodos de referência e os valores
correspondentes;
- Para cada período ela retorna a soma destes valores em forma de dicionário {período:soma_valor};
- Com a função "criar_novo_arquivo", uma nova planilha é gerada com os períodos de referência,
a soma dos valores correspondentes ao período e um gráfico resumo de todo o histórico.


## 3. Analisar mensalmente os valores, a origem dos valores e quantidade de itens

### 3.1 Filtro

- É necessário selecionar um período (mês) de referência;

### 3.2 Analise de valores

- Dado o período de referência, são feitas iterações neste período, retornando a soma total dos
valores correspondentes a ele.

### 3.3 Analise da origem dos valores

- Dado o período de referência, são feitas iterações neste período, que agora somará os valores 
para cada origem diferente, retornando as origens dos valores com suas respectivas somas;
- É gerado um gráfico de setores com as informações geradas para melhor visualização.

### 3.4 Analise da quantidade de itens

- Dado o período de referência, são feitas iterações neste período, contando a quantidade de vezes
que cada um dos itens se repete tendo como retorno cada item e a quantidade de repetições;
- É gerado um gráfico de setores com as informações geradas para melhor visualização.
