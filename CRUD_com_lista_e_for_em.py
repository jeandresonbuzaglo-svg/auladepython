
biblioteca = []

while True:
    print("===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Pesquisar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

# CREATE - CADASTRO DE LIVRO

    if opcao == "1":
        codigo = int(input("Código: "))
        titulo = input("titulo: ")
        autor = input("autor: ")
        ano = int(input("ano: "))

        livro = [codigo, titulo, autor, ano]

        biblioteca.append(livro)

        print("Livro cadastrado!")
        print("biblioteca")


# READ - LISTA E PESQUISAR

    for livro in biblioteca:
        print("Código:" , livro[0])
        print("Título:" , livro[1])
        print("Autor:" , livro[2])
        print("Ano:" , livro[3])
        print("__________")
    codigo_busca = int(input("Digite o código: "))

    for livro in biblioteca:
        if livro[0] == codigo_busca:
            print("Livro encontrado!")
            print("Título:, livro[1]")
            print("Autor:, livro[2]")
            print("Ano:, livro[1]")











               
