print("\nBem vindo a Lista de Contatos do Gustavo Ferreira\n")

# Lista de dicionarios e o id global que coloquei meu RU
lista_contatos = []
id_global = 5360106

#Funções do PROGRAMA

def cadastrar_contato(id):# Função para cadastrar contato
    print(12 * "-", "MENU CADASTRAR CONTATO", 12 * "-")
    print("Id do Contato: ", id)
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o Telefone do contato: ")
    print(45 * "-")

    contato = { # Dicionario para armazenar os dados do contato
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    lista_contatos.append(contato.copy()) # Adiciona o contato na lista de contatos

    print("\nContato cadastrado com sucesso!\n")

def consultar_contatos():# Função para consultar contatos
    while True:
        print(12 * "-", "MENU CONSULTAR CONTATOS", 11 * "-")
        opc = input("\n1. Consultar todos\n2. Consultar por ID\n3. Consultar por Atividade\n4. Retornar ao menu\nEscolha uma opção: ")
    
        if opc == "1":#Para mostrar todos os contatos
            print(15 * "-")
            for c in lista_contatos:
                print(f"id: {c['id']}\nNome: {c['nome']}\nAtividade: {c['atividade']}\nTelefone: {c['telefone']}\n", 15 * "-")

        elif opc == "2":#Para consultar por ID
            id_busca = input("Informe o ID do contato: ")
            encontrados = False
            for c in lista_contatos:
                if str(c["id"]) == id_busca:
                    print(f"\nContato encontrado: {c['id']}\nNome: {c['nome']}\nAtividade: {c['atividade']}\nTelefone: {c['telefone']}")
                    encontrados = True
                    break
            if not encontrados:
                print("ID não encontrado.")
                
        elif opc == "3":#Para consultar por atividade
            atividade_busca = input("Informe a atividade: ")
            encontrados = [c for c in lista_contatos if c["atividade"].lower() == atividade_busca.lower()]
            if encontrados:
                print("\n--- CONTATOS ENCONTRADOS ---")
                for c in encontrados:
                    print(f"{c['id']}\nNome: {c['nome']}\nAtividade: {c['atividade']}\nTelefone: {c['telefone']}")

            else:
                print("Nenhum contato exerce essa atividade.")
        
        elif opc == "4":#Voltar
            return
        
        else:
            print("Opção inválida.Tente novamente.")

def remover_contato():#Função para remover contatos
    id_remove = input("Informe o id do contato que deseja remover: ")
    encontrado = False

    for c in lista_contatos:
        if str(c["id"]) == id_remove:
            lista_contatos.remove(c)
            print("\nContato removido com sucesso!\n")
            encotrado = True
            return
    if not encontrado:
        print("Id inválido!Tente novamente.")

while True:
    print(45 * "-")
    print(15 * "-", "MENU PRINCIPAL", 15 * "-")
    opcao = input("Escolha a opção desejada:\n1 - Cadastrar Contato\n2 - Consultar Contato(s)\n3 - Remover Contato\n4 - Sair\n")
#opções iniciais do programa
    if opcao == "1":
        cadastrar_contato(id_global)
        id_global += 1
    
    elif opcao == "2":
        consultar_contatos()

    elif opcao == "3":
        remover_contato()

    elif opcao == "4":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")