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

# Função que cria um post e adiciona na lista de posts
def cria_post()-> list:
    try:
        h1 = input("Insira o título do post: ").capitalize().strip() 
        main = input("Insira o corpo do post: ").capitalize().strip() 

        post = {
            "titulo": h1,
            "corpo": main,
            "autor": f"Autor: {primeiro_nome(nome)}"
        }

        posts.append(post)

    except Exception as e:
        return "Algo inesperado ocorreu na execução do projeto"

    return "\n✅ Post criado com sucesso!\n"

# Função lambda que mostra as opções do site
mostra_opcoes = lambda: print('\nFunções do site:\n1-) Ver o meu perfil\n2-) Criar Posts\n3-) Listar posts existentes\n\033[91m4-) Sair\033[0m\n')

# Função que lista os posts criados
def listar_posts(postagens: list) -> list:
    if postagens:
        for i, post in enumerate(postagens, start=1):
            print(f"\nPost n{i}:\n{post['titulo']}\n{post['corpo']}\n{post['autor']}\n")
    else:
        print(f"\033[93mAinda não há nenhum post\033[0m\n")

#Regex pra verificar a veracidade do e-mail inserido pelo user
def email_valido(email: str) -> bool:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

#-Coleta-de-Dados----------------------------------------------------------------------------------------------------------
print("LOGIN - PASSA A BOLA \n")

# Cadastro do usuário:
try: 
    nome = input("Digite o seu nome completo: ").capitalize().strip()
    email = input("Digite o seu email principal: ").strip()

    while not email_valido(email):
        if email_valido(email): break

        else:
            print("\033[93mInsira um email válido\033[0m")
            email = input("Digite o seu email principal: ").strip()
    
    senha = input("Crie uma senha para usar no APP: ").strip()

except Exception as e:
    print(f"\nErro inesperado: {e}")

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

# Pergunta se o usuário quer ser membro fiel
while True:
    membro = input("Deseja ser membro(a) fiel do PASSA A BOLA? (Você não tem escolha) ").upper().strip()

    if membro not in ["SIM","S","SIP","SIK","SIN"]:
        membro = input("Não não é resposta, diz que sim, vai (eu avisei) ").upper().strip()

        if membro in ["SIM","S","SIP","SIK","SIN"]:
            print("\033[32mObrigado por fazer parte da nossa comunidade!\033[0m\n")
            break

    else:
        print("\033[32mObrigado por fazer parte da nossa comunidade!\033[0m\n")
        break


#-Execuçao-Principal-------------------------------------------------------------------------------------------------------

contador = 0
posts = []

mostra_opcoes()

while True:
    opcao = input("O quê você gostaria de fazer? (Digite o número): ").upper().strip()
    contador += 1

    if contador >= 3:
        mostra_opcoes()
    if opcao == "1":
        mostra_perfil(nome,email,senha)
    elif opcao == "2":
        cria_post()
    elif opcao == "3":
        listar_posts(posts)
    elif opcao == "4":
        print("\nVocê acaba de sair do nosso site, agradecemos sua atenção!"),time.sleep(1)
        print("\033[32mxd\033[0m")
        break

    else:
        print("\n\033[93mDigite um índice válido!\033[0m\n")
