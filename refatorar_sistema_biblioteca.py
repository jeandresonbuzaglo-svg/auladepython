

biblioteca = []

while True:
    print("===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Alterar livro")
    print("5 - Excluir livro")
    print("6 - Sair do sistema")

    opcao = input("Escolha uma opção: ")

    # CREATE - Cadastrar
    if opcao == "1":
        codigo = int(input("Código: "))

        # Verificar se o código já existe
        existe = False

        for livro in biblioteca:
            if livro[0] == codigo:
                existe = True

        if existe:
            print("Erro: esse código já está cadastrado!")
        else:
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))

            livro = [codigo, titulo, autor, ano]
            biblioteca.append(livro)

            print("Livro cadastrado com sucesso!")

    # READ - Listar
    elif opcao == "2":
        if len(biblioteca) == 0:
            print("Nenhum livro cadastrado.")
        else:
            print("\n===== LIVROS CADASTRADOS =====")

            for livro in biblioteca:
                print("Código:", livro[0])
                print("Título:", livro[1])
                print("Autor:", livro[2])
                print("Ano:", livro[3])
                print("-------------------------")

    # READ - Pesquisar
    elif opcao == "3":
        codigo_busca = int(input("Digite o código do livro: "))

        encontrado = False

        for livro in biblioteca:
            if livro[0] == codigo_busca:
                print("\nLivro encontrado!")
                print("Código:", livro[0])
                print("Título:", livro[1])
                print("Autor:", livro[2])
                print("Ano:", livro[3])

                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    # UPDATE - Alterar
    elif opcao == "4":
        codigo_busca = int(input("Digite o código do livro: "))

        encontrado = False

        for livro in biblioteca:
            if livro[0] == codigo_busca:
                print("\nLivro encontrado!")

                livro[1] = input("Novo título: ")
                livro[2] = input("Novo autor: ")
                livro[3] = int(input("Novo ano: "))

                print("Livro atualizado com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    # DELETE - Excluir
    elif opcao == "5":
        codigo_busca = int(input("Digite o código do livro: "))

        encontrado = False

        for livro in biblioteca:
            if livro[0] == codigo_busca:
                biblioteca.remove(livro)

                print("Livro excluído com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("Livro não encontrado.")

    # SAIR
    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
