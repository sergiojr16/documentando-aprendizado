# Controle de Estoque

## 1. Programa principal
- Armazena os itens do estoque na lista 'estoque';
- Utiliza a função "abrir_estoque" para verificar se já existe um estoque salvo;
- O loop principal faz o menu inicial aparecer até o que o usuário decida sair do programa;

## 2. Abrir Estoque
- A função verifica se já existe um arquivo .txt com dados de estoque salvo;
- Caso exista este arquivo, ela carrega os dados para o programa.

## 3. Adicionar Produto
- Esta função adiciona um novo produto ao estoque;
- Ela solicita ao usuário 4 inputs relacionados ao produto: ID, nome, preço e quantidade;
- Os inputs são adicionados em forma de dicionário e o valor do ID deve ser único.

## 4. - Listar Produtos
- Esta função lista os produtos cadastradas na lista 'estoque';
- Se nenhum produto foi cadastrado, ela indica que o estoque está vazio;
- A lista mostra os produtos cadastrados em ordem crescente de ID.

## 5. Atualizar Produto
- Esta função permite atualizar os dados de um produto tendo seu ID como referêcia;
- Caso não haja produtos previamente cadastrados, ela indica que o estoque está vazio.

## 6. Remover Produto
- Esta função permite remover um produto tendo seu ID como referêcia;
- Uma mensagem de segurança é exibida para confirmar se quer que o produto seja removido;
- Caso não haja produtos previamente cadastrados, ela indica que o estoque está vazio.

## 7. Salvar Estoque
- Esta função salva os dados do estoque em um arquivo .txt para que sejam utilizados no proximo uso do programa.

