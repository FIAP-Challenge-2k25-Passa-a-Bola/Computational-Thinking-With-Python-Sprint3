import os, sys, time, re

# Função pra reinicializar o sistema e o terminal
def restart(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Função lambda que retorna o primeiro nome
primeiro_nome = lambda name: name.split(' ')[0]

# Função lambda que mostra o perfil do usuário
mostra_perfil = lambda name, mail, password: print(f'\nPerfil de {name}:\nNome: {name}\nE-mail: {mail}\nSenha: {password}\n')

# Salva os dados do usuário no arquivo  
def salvar_usuario(nome, email, senha, arquivo="usuario.txt"):
    with open(arquivo, "w") as f:
        f.write(f"{nome}\n")
        f.write(f"{email}\n")
        f.write(f"{senha}\n")

# Carrega os dados do usuário do arquivo user.txt
def carregar_usuario(arquivo="usuario.txt"):
    if not os.path.exists(arquivo):
        return None, None, None
    with open(arquivo, "r") as f:
        linhas = [linha.strip() for linha in f.readlines()]
    return linhas[0], linhas[1], linhas[2]

# Função que cria um post e adiciona no arquivo
def cria_post()-> str:
    try:
        h1 = input("\nInsira o título do post: ").title().strip() 
        main = input("Insira o corpo do post: ").capitalize().strip() 
        post = {
            "titulo": h1,
            "corpo": main,
            "autor": f"Autor: {primeiro_nome(nome)}"
        }

        with open("dados.txt","a", encoding="utf-8") as arquivo:
            arquivo.write(f"{post['titulo']}\n")
            arquivo.write(f"{post['corpo']}\n")
            arquivo.write(f"{post['autor']}\n")

    except Exception:
        return "Algo inesperado ocorreu na execução do projeto"

    return "\n✅ Post criado com sucesso!"

# Função que mostra as opções
mostra_opcoes = lambda: print('Funções do site:\n1-) Ver o meu perfil\n2-) Criar posts\n3-) Listar posts \n4-) Alterar senha\n5-) Excluir perfil\n\033[91m6-) Sair\033[0m')

# Função que lista os posts criados (lê direto do arquivo)
def lista_posts() -> None:
    if not os.path.exists("dados.txt"):
        print(f"\033[93mAinda não há nenhum post\033[0m\n")
        return

    with open("dados.txt","r",encoding="utf-8") as arquivo:
        conteudo = arquivo.read().strip()
        
        if conteudo != "":
            print("\n",conteudo)
        else:
            print(f"\033[93mAinda não há nenhum post\033[0m\n")

# Altera somente a senha do usuário
def altera_senha():
    global senha
    nova = input("Digite a nova senha: ").strip()

    if nova == "":
        print("\033[91mA nova senha não pode ser vazia.\033[0m")
        return
    
    senha = nova
    salvar_usuario(nome, email, senha)
    print("\033[32mSenha alterada com sucesso.\033[0m")

# Exclui o perfil (apaga o arquivo e sai)
def exclui_perfil():
    if os.path.exists("usuario.txt"):
        os.remove("usuario.txt")

    print("\033[32mPerfil excluído com sucesso.\033[0m")
    print("Encerrando o sistema...")
    time.sleep(1)
    sys.exit(0)

# Regex pra verificar a veracidade do e-mail do user
def email_valido(email: str) -> bool:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

print("LOGIN - PASSA A BOLA \n")

# Coleta de dados do usuário:
try: 
    nome = input("Digite o seu nome completo: ").strip()
    email = input("Digite o seu email principal: ").strip()
    email_normalizado = email.lower()

    while not email_valido(email):
        print("\033[93mInsira um email válido\033[0m")
        email = input("Digite o seu email principal: ").strip()
        email_normalizado = email.lower()
    
    senha = input("Crie uma senha para usar no APP: ").strip()

except Exception as e:
    print(f"\nErro inesperado: {e}")

# salva logo após o cadastro
salvar_usuario(nome, email, senha)

tentativas = 3

# Verificação da senha:
while True:
    try:    
        verificacao = input(f"Confirme sua senha \033[93m({tentativas} tentativa(s) restantes):\033[0m ").strip()

        if verificacao == "":
            print("\033[91mA senha não pode ser vazia!\033[0m")

        if verificacao == senha:
            print("✅ Senha correta, acesso liberado!")
            break

        tentativas -= 1
        if tentativas == 0:
            print("❌ \033[91mVocê errou 3 vezes.\033[0m")
            print("Reinicializando...")
            time.sleep(3)
            restart()
            
    except Exception as e:
        print(f"Erro durante a execução: {e}")

print(f"\nSeja bem vindo(a) a nossa comunidade exclusiva, \033[32m{primeiro_nome(nome)}\033[0m")

contador = 0

mostra_opcoes()

while True:
    opcao = input("\nO quê você gostaria de fazer? (Digite o número): ").upper().strip()
    contador += 1

    if contador >= 3:
        mostra_opcoes()

    if opcao == "1":
        mostra_perfil(nome, email, senha)

    elif opcao == "2":
        msg = cria_post()
        print(msg)

    elif opcao == "3":
        lista_posts()

    elif opcao == "4":
        altera_senha()

    elif opcao == "5":
        exclui_perfil()

    elif opcao == "6":
        print("\nVocê acaba de sair do nosso site, agradecemos sua atenção!"),time.sleep(1)
        print("\033[32mxd\033[0m")
        break

    else:
        print("\n\033[93mDigite um índice válido!\033[0m\n")
