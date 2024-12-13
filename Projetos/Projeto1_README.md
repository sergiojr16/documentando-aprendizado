# Gerenciador de Atividades

## 1. Programa principal 
- Armazena uma lista com todas as atividades através da variável 'atividades';
- O loop principal faz o menu inicial aparecer até o que o usuário decida sair.

## 2. Menu Inicial
- Mostra as funcionalidades do programa principal: adicionar, listar, marcar como concluído e remover atividades.

## 3. Adicionar Atividade
- Esta função adiciona uma atividade na lista 'atividades'; 
- A atividade é adicionada em forma de dicionário, no qual o primeiro campo representa a atividade em si e o segundo campo indica se a atividade foi concluída ou não, através de um valor Booleano.

## 4. Listar Atividade
- Esta função lista as atividades cadastradas na lista 'atividades';
- Se nenhuma atividade foi cadastrada, ela indica que a lista está vazia;
- A lista mostra as atividades cadastradas enumeradas e suas situações (se foram concluídas ou não).

## 5. Concluir Atividade
- Esta função permite modificar a situação de uma atividade da lista (modifica de 'pendente' para 'concluída') com base em seu índice;
- Se nenhuma atividade foi cadastrada, ela indica que a lista está vazia e solicita que ao menos uma atividade seja cadastrada.

## 6. Remover Atividade
- Esta função remove uma atividade previamente adicionada na lista com base em seu índice;
- Se nenhuma atividade foi cadastrada, ela indica que a lista está vazia e solicita que ao menos uma atividade seja cadastrada.

