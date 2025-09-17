# README - Projeto "Passa a Bola"

## 📝 Descrição

"Passa a Bola" é um script de console simples em Python que simula uma pequena rede social. Ele permite que os usuários se cadastrem, verifiquem suas senhas, visualizem seus perfis, criem e listem posts. O projeto foi desenvolvido para demonstrar conceitos básicos de Python, como funções, laços de repetição, condicionais, manipulação de strings e listas, além do uso de funções `lambda`.

## ✨ Funcionalidades Principais

  * **Cadastro de Usuário**: Coleta nome completo, e-mail e senha.
  * **Verificação de Senha**: Sistema de confirmação de senha com um limite de três tentativas para garantir a segurança.
  * **Boas-vindas Personalizada**: Saúda o usuário pelo primeiro nome após o login bem-sucedido.
  * **Criação de Posts**: Permite ao usuário criar posts com título e corpo, que são armazenados em uma lista.
  * **Listagem de Posts**: Exibe todos os posts criados pelo usuário, numerados e formatados.
  * **Visualização de Perfil**: Mostra os detalhes do usuário cadastrado (nome, e-mail e senha).
  * **Menu Interativo**: Um menu de fácil navegação permite ao usuário escolher a ação que deseja realizar.
  * **Reinicialização Automática**: Em caso de falha na verificação da senha, o script é reiniciado automaticamente.

## 🚀 Como Executar

Para executar este projeto, você precisa ter o Python instalado em seu sistema.

1.  **Clone o repositório ou baixe o arquivo** `entrada-user.py`.
2.  **Abra o seu terminal** ou prompt de comando.
3.  **Navegue até o diretório** onde o arquivo foi salvo.
4.  **Execute o seguinte comando**:
    ```bash
    python entrada-user.py
    ```
5.  **Siga as instruções** apresentadas no console para interagir com o programa.

## 🛠️ Estrutura do Código

O script é dividido em seções principais para organização e clareza.

### Funções Auxiliares e Lambdas

  * `restart()`: Utiliza o módulo `os` e `sys` para limpar o console e reiniciar o script. É multiplataforma, funcionando tanto em Windows (`cls`) quanto em sistemas baseados em Unix (`clear`).
  * `primeiro_nome = lambda name: ...`: Uma função `lambda` que recebe um nome completo e retorna apenas o primeiro nome.
  * `mostra_perfil = lambda name, mail, password: ...`: Uma função `lambda` que formata e exibe os detalhes do perfil do usuário.
  * `mostra_opcoes = lambda: ...`: Uma função `lambda` que simplesmente imprime o menu de opções disponíveis para o usuário.

### Funções Principais

  * `cria_post()`: Solicita ao usuário um título e um corpo para um novo post. Cria um dicionário contendo essas informações, juntamente com o nome do autor, e o adiciona à lista global `posts`.
  * `listar_posts(postagens:list)`: Verifica se a lista de posts não está vazia. Se houver posts, itera sobre a lista e exibe cada um de forma formatada. Caso contrário, informa ao usuário que nenhum post foi criado ainda.

### Coleta de Dados e Verificação

Esta seção é responsável por toda a interação inicial com o usuário:

1.  Solicita o nome completo, e-mail e uma senha para o cadastro.
2.  Inicia um laço `while` para a verificação da senha, dando ao usuário três tentativas.
3.  Se a senha for confirmada, o acesso é liberado. Caso contrário, após três falhas, a função `restart()` é chamada.
4.  Após o login, uma mensagem de boas-vindas é exibida.
5.  Inclui um laço de repetição bem-humorado que "força" o usuário a se tornar um "membro fiel".

### Execução Principal

O coração do programa, onde o menu interativo é gerenciado:

1.  Inicializa uma lista vazia `posts` e um `contador`.
2.  Exibe as opções do menu pela primeira vez.
3.  Entra em um laço `while True` que continuamente solicita ao usuário uma opção.
4.  A cada três interações, o menu de opções é exibido novamente para conveniência do usuário.
5.  Utiliza uma estrutura `if/elif/else` para chamar a função correspondente à escolha do usuário (`1` para perfil, `2` para criar post, `3` para listar posts).
6.  A opção `4` encerra o programa com uma mensagem de despedida.
7.  Qualquer outra entrada é tratada como inválida.