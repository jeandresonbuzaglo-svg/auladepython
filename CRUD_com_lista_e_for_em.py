
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

    print("________________________________________")

    # CREATE - CADASTRAR LIVRO

    if opcao == "1":
        codigo = int(input("Código: "))
        titulo = input("titulo: ")
        autor = input("autor: ")
        ano = int(input("ano: "))

        livro = [codigo, titulo, autor, ano]

        biblioteca.append(livro)

        print("Livro cadastrado com sucesso!")
        print("biblioteca Jeandreson buzaglo araujo")
        print("_____________________________________")




    # READ - LISTAR 
    elif opcao == "2":
        if len(biblioteca) == 0:
            print("Nenhum livro cadastrado.")
        else:
            print("___________Livros cadastrados_____________________") 

            for livro in biblioteca:
                print("Código:" , livro[0])
                print("Título:" , livro[1])
                print("Autor:" , livro[2])
                print("Ano:" , livro[3])
                print("Listado com sucesso")
                print("__________")
                
       

               
    # READ - PESQUISAR CÓDIGO  
    elif opcao == "3":
        codigo_busca = int(input("Digite o código do livro: "))
 
        
        for livro in biblioteca:
            if livro[0] == codigo_busca:
                 print("\nLivro encontrado em nossa biblioteca!")
                 print("Código:", livro[0])
                 print("Título:", livro[1])
                 print("Autor:", livro[2])
                 print("Ano:", livro[3])
 
               
 
            else:
             print("Livro não encontrado.")
 
 
 
               

    # UPDATE - ALTERAR
    elif opcao == "4":
        codigo_busca = int(input("Digite o código do livro: "))
        
        for livro in biblioteca:
            if livro[0] == codigo_busca:
                        print("Livro encontrado!")
                        print("Fazer Alteração do livro ")
        
                        livro[1] = input("Novo título: ")
                        livro[2] = input("Novo autor: ")
                        livro[3] = int(input("Novo ano: "))
        
                        print("Livro atualizado com sucesso!")
        
                               
            else:
                        print("Livro não encontrado.")
                        print("Favor verificar o código do livro")


    # DELETE - EXCLUIR
    elif opcao == "5":

        codigo_busca = int(input("Digite o código do livro: "))
                 
        for livro in biblioteca:
            if livro[0] == codigo_busca:
                        biblioteca.remove(livro)
                        print("Livro excluído com sucesso")
                        print("_____________________________")
                        break                
                                  

    # SAIR - ENCERRA O WHILE

    elif opcao == "6":
        print("Programa encerrado.")
    else:
        print("Opção inválida!")
   


