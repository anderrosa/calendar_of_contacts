# Lista para armazenar os contatos
contatos = []

# Função para exibir o menu
def menu():
    print("\n=== AGENDA DE CONTATOS ===")
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Ver Contatos Favoritos")
    print("6. Deletar Contato")
    print("0. Sair")

# Função para adicionar contato
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append({"nome": nome, "telefone": telefone, "email": email, "favorito": False})
    print(f"Contato '{nome}' adicionado com sucesso!")

# Função para visualizar contatos
def visualizar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    print("\nLista de Contatos:")
    for idx, contato in enumerate(contatos):
        favorito = "⭐" if contato['favorito'] else ""
        print(f"{idx + 1}. {contato['nome']} | {contato['telefone']} | {contato['email']} {favorito}")

# Função para editar um contato
def editar_contato():
    visualizar_contatos()
    try:
        idx = int(input("Número do contato a ser editado: ")) - 1
        if 0 <= idx < len(contatos):
            contatos[idx]['nome'] = input(f"Novo nome ({contatos[idx]['nome']}): ") or contatos[idx]['nome']
            contatos[idx]['telefone'] = input(f"Novo telefone ({contatos[idx]['telefone']}): ") or contatos[idx]['telefone']
            contatos[idx]['email'] = input(f"Novo email ({contatos[idx]['email']}): ") or contatos[idx]['email']
            print("Contato atualizado com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Função para marcar/desmarcar como favorito
def marcar_favorito():
    visualizar_contatos()
    try:
        idx = int(input("Número do contato para marcar/desmarcar favorito: ")) - 1
        if 0 <= idx < len(contatos):
            contatos[idx]['favorito'] = not contatos[idx]['favorito']
            status = "favorito" if contatos[idx]['favorito'] else "não favorito"
            print(f"Contato '{contatos[idx]['nome']}' marcado como {status}.")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Função para visualizar contatos favoritos
def visualizar_favoritos():
    favoritos = [c for c in contatos if c['favorito']]
    if not favoritos:
        print("Nenhum contato favorito.")
        return
    print("\nLista de Contatos Favoritos:")
    for idx, contato in enumerate(favoritos):
        print(f"{idx + 1}. {contato['nome']} | {contato['telefone']} | {contato['email']} ⭐")

# Função para deletar contato
def deletar_contato():
    visualizar_contatos()
    try:
        idx = int(input("Número do contato a ser deletado: ")) - 1
        if 0 <= idx < len(contatos):
            contato_removido = contatos.pop(idx)
            print(f"Contato '{contato_removido['nome']}' removido com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida.")

# Loop principal
while True:
    menu()
    escolha = input("\nEscolha uma opção: ")
    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        visualizar_contatos()
    elif escolha == "3":
        editar_contato()
    elif escolha == "4":
        marcar_favorito()
    elif escolha == "5":
        visualizar_favoritos()
    elif escolha == "6":
        deletar_contato()
    elif escolha == "0":
        print("\nSaindo... Até mais!")
        break
    else:
        print("\nOpção inválida, tente novamente.")
