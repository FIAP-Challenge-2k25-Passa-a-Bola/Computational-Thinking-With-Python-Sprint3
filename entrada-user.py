import os, sys, time, re

def restart(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    python = sys.executable
    os.execl(python, python, *sys.argv)

primeiro_nome = lambda name: name.split(' ')[0]

mostra_perfil = lambda name, mail, password: print(f'\nPerfil de {name}:\nNome: {name}\nE-mail: {mail}\nSenha: {password}\n')

def cria_post()-> list:
    try:
        h1 = input("\nInsira o título do post: ").title().strip() 
        main = input("Insira o corpo do post: ").capitalize().strip() 

        post = {
            "titulo": h1,
            "corpo": main,
            "autor": f"Autor: {primeiro_nome(nome)}"
        }

        posts.append(post)

        with open("dados.txt","a", encoding="utf-8") as arquivo:
            arquivo.write(f"{post['titulo']}\n")
            arquivo.write(f"{post['corpo']}\n")
            arquivo.write(f"{post['autor']}\n\n")
            arquivo.write('-' * 30 + "\n\n")

    except Exception as e:
        return "Algo inesperado ocorreu na execução do projeto"

    return "\n✅ Post criado com sucesso!\n"

mostra_opcoes = lambda: print('Funções do site:\n1-) Ver o meu perfil\n2-) Criar posts\n3-) Listar posts existentes\n4-) Alterar posts\n5-) Excluir posts\n\033[91m6-) Sair\033[0m')

def lista_posts() -> list:
    with open("dados.txt","r",encoding="utf-8") as arquivo:
        conteudo = arquivo.read().strip()
        
        if conteudo != "":
            print("\n",conteudo)
        else:
            print(f"\033[93mAinda não há nenhum post\033[0m\n")

def email_valido(email: str) -> bool:
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

adm = False

print("LOGIN - PASSA A BOLA \n")

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

tentativas = 3

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

if email_normalizado == "adm@gmail.com" and senha == "adm":
    adm = True

print(f"\nSeja bem vindo(a) a nossa comunidade exclusiva, \033[32m{primeiro_nome(nome)}\033[0m")

if not adm:
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

contador = 0
posts = []

mostra_opcoes()

while True:
    opcao = input("\nO quê você gostaria de fazer? (Digite o número): ").upper().strip()
    contador += 1

    if contador >= 3:
        mostra_opcoes()

    if opcao == "1":
        mostra_perfil(nome,email,senha)
    elif opcao == "2":
        cria_post()
    elif opcao == "3":
        lista_posts()
    elif opcao == "4":
        if adm:
            print("\033[32mAcesso liberado para alterar posts (admin).\033[0m")
        else:
            print("\033[91mAcesso negado. Apenas administradores podem alterar posts.\033[0m")

    elif opcao == "5":
        if adm:
            print("\033[32mAcesso liberado para excluir posts (admin).\033[0m")
        else:
            print("\033[91mAcesso negado. Apenas administradores podem excluir posts.\033[0m")

    elif opcao == "6":
        print("\nVocê acaba de sair do nosso site, agradecemos sua atenção!"),time.sleep(1)
        print("\033[32mxd\033[0m")
        break
    else:
        print("\n\033[93mDigite um índice válido!\033[0m\n")
