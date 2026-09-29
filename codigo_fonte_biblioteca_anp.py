livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])

            else:
                print("Livro não encontrado!")    

    

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")
        encontrado = False

        for contador in livros:
            if contador[0] == pesquisa:
                livros.remove(contador)
                encontrado = True
                print("Livro excluído!")
                break

            if not encontrado:
                print("Livro não pode ser excluído, pois não foi encontrado.")

    elif opcao == "5":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")


elif opcao == "6":
quantidade = len(livros)
print(f"Existem {quantidade} livro(s) cadastrado(s).")