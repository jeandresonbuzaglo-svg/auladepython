
# Lista que armazenará os livros
livros = []


# Desafio 1
def calcular_total(preco, quantidade):
    return preco * quantidade


# Desafio 2
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    preco = float(input("Digite o preço do livro: "))

    livro = {
        "titulo": titulo,
        "autor": autor,
        "preco": preco
    }

    livros.append(livro)
    print("Livro cadastrado com sucesso!")


# Desafio 3
def listar_livros():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    print("\n--- LIVROS CADASTRADOS ---")

    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Preço: R$ {livro['preco']:.2f}")
        print("------------------------")


# Desafio 4
def buscar_livro():
    titulo = input("Digite o título que deseja buscar: ")

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            print("\nLivro encontrado!")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Preço: R$ {livro['preco']:.2f}")
            return

    print("Livro não encontrado.")


# Desafio 5
def remover_livro():
    titulo = input("Digite o título do livro que deseja remover: ")

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)
            print("Livro removido com sucesso!")
            return

    print("Livro não encontrado.")


# Testando calcular_total()
resultado = calcular_total(20, 4)
print("Total:", resultado)


# Menu principal
while True:
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Remover livro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        buscar_livro()

    elif opcao == "4":
        remover_livro()

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")




