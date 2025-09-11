import os, sys, time

def restart(): #Função pra reinicializar o sistema e o terminal

    os.system('cls' if os.name == 'nt' else 'clear')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def primeiro_nome(name:str):
    name = name.split(' ')
    for i in name:
        primeiro_nome = name[0]
    return primeiro_nome

print("LOGIN - PASSA A BOLA \n")

# Cadastro do usuário: 
nome = input("Digite o seu nome completo: ").capitalize()
email = input("Digite o seu email principal: ").strip()
senha = input("Crie uma senha para usar no APP: ").strip()

tentativas = 3

while True:
    verificacao = input(f"Confirme sua senha: \033[93m({tentativas} tentativa(s) restante(s))\033[0m ").strip()

    if verificacao == senha:
        print("✅ Senha correta, acesso liberado!")
        break

    tentativas -= 1
    if tentativas == 0:
        print("❌ \033[91mVocê errou 3 vezes.\033[0m")
        print("Reinicializando...")
        time.sleep(3)

        restart()
    else:
        print("\033[91mSenha incorreta. Tente novamente.\033[0m")

print(f"\nSeja bem vindo(a) a nossa comunidade exclusiva, \033[32m{primeiro_nome(nome)}\033[0m")

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

#-----------------------------------------------------------------------------------------------------------

print("Funções do site:\n1-) Ver o meu perfil\n2-) Criar Posts\n3-) Listar posts existentes\n4-) Sair")

while True:
    posts = []
    opcao = input("O quê você gostaria de fazer? (Digite o número): ").upper().strip()

    if opcao == "1":
        print(f"\nPerfil de {primeiro_nome(nome)}:\nNome: {nome}\nE-mail: {email}\nSenha: {senha}")

    elif opcao == "2":
        h1 = input("Insira o título do post: ").strip(), posts.append(h1)
        main = input("Insira o corpo do post: ").strip(), posts.append(main)
        footer = input("Insira o footer do post: ").strip(), posts.append(footer)

        post = {
            "titulo": h1,
            "corpo": main,
            "footer": footer
        }

        posts.append(post)

        print("\n✅ Post criado com sucesso!\n")








    



    


    

