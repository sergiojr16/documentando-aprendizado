# Sistema Bancário Simples (POO)

## 1. Classe Pessoa
Registra os dados dos clientes.
### 1.1 Atributos
- Nome; 
- Idade; 
- CPF.
### 1.2 Métodos
- Método "str" que retorna em forma de string o atributo "nome".

## 2. Classe Conta
Vincula uma pessoa à uma conta.
### 2.1 Atributos
- Pessoa;
- Número da conta;
- Saldo (privado);
- Histórico (lista com todas as operações realizadas).
### 2.2 Métodos
- @property e @saldo.setter para acessar e modificar, respectivamente, o atributo privado "saldo";
- Sacar: solicita um valor, verifica se o saldo na conta é maior ou igual a esse valor, caso seja,
subtrai o valor do saldo. No fim, registra a operação do histórico;
- Depositar: solicita um valor maior que 0 e adiciona esse valor ao saldo, registrando no histórico;
- Transferir: solicita um valor e uma conta destino. Verifica se o saldo na conta origem é maior ou 
igual a esse valor, caso seja, subtrai o valor do saldo da conta origem e deposita o mesmo valor no
saldo da conta destino. Registra a operação no histórico da conta origem e da conta destino;
- Consultar_saldo: mostra o saldo da conta selecionada;
- Registrar_histórico: registra a operação feita no histórico do objeto;
- Consultar_histórico: mostra todas as operações feitas envolvendo o saldo do objeto selecionado;
- Método "str" que retorna em forma de string os atributos "pessoa" e "número da conta".

## 3. Classe Banco
Guarda as informações das contas em um dicionário.
### 3.1 Atributos
- Contas (dicionário que irá guardar {número da conta : objeto}).
### 3.2 Métodos
- Adicionar_conta: adiciona um novo par "número_da_conta - objeto(conta)" no dicionário;
- Encontrar_conta: dado um número da conta, retorna o objeto(conta) correspondente;
- Listar_contas: verifica se o dicionário está vazio, se não estiver, lista todas as contas do dicionário.

## 4. Programa Principal:
- Inicia uma instância da classe Banco;
- O menu inicial irá aparecer em forma de loop até o que o usuário escolha uma opção disponível: "criar conta",
"já sou cliente" (usado para acessar uma conta já cadastrada), "listar contas cadastradas" ou "sair do programa";
- Ao escolher "criar conta", o método cadastrar_cliente solicitará inputs de "nome", "idade" e "cpf" para 
criar um objeto da classe Pessoa. Depois será solicitado um input de "número da conta", validado pelo método 
valida_cadastro para a criação de um objeto da classe Conta, que será adicionado ao Banco;
- Ao escolher "já sou cliente", será verificado se já existe uma conta cadastrada. Caso uma ou mais contas já
tenham sido cadastradas, será solicitado o número da conta. Uma vez informado um número de conta válido, o
menu do cliente irá aparecer em forma de loop até que o usuário escolha uma opção disponível: sacar, depositar,
transferir, consultar saldo, consultar histórico de transações ou voltar ao menu anterior. Cada uma das opções
retorna um método da classe Conta e "voltar ao menu anterior" retorna ao menu inicial;
- Ao escolher "listar contas cadastradas", a função listar_contas() é chamada;
- Ao escolher "sair do banco", a aplicação é encerrada.