import os, sys, time

def restart(): #Função pra reinicializar o sistema e o terminal

    os.system('cls' if os.name == 'nt' else 'clear')
    python = sys.executable
    os.execl(python, python, *sys.argv)

print("LOGIN - PASSA A BOLA \n")

# Cadastro do usuário: 
nome = input("Digite o seu nome completo: ").capitalize().split(" ")
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

for i in nome: # Função pra coletar o primeiro nome do usuário
    primeiro_nome = nome[0]
        
print(f"\nSeja bem vindo(a) a nossa comunidade exclusiva, \033[32m{primeiro_nome}\033[0m")

while True:
    membro = input("Deseja ser membro(a) fiel do PASSA A BOLA? (Você não tem escolha) ").upper().strip()

    if membro not in ["SIM","S","SIP","SIK","SIN"]:
        membro = input("Não não é resposta, diz que sim, vai (eu avisei) ").upper().strip()

    else:
        print("\033[32mObrigado por fazer parte da nossa comunidade!\033[0m\n")
        break


    


    

