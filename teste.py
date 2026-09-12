
print("****************************************")  

print("        SISTEMA PARA BIBLIOTECA")
print("****************************************")
print("1 - Cadastrar Livros")
print("2 - Cadastrar Alunos")
print("3 - Realizar Empréstimo")
print("4 - Sair")
print("****************************************")

opcao = input("Escolha uma opção: ")

if opcao == "1":

        quantidade_livros = int(input("Quantos livros deseja cadastrar? "))

        for livro in range(quantidade_livros):

            print("----- LIVRO", livro + 1, "-----")

            codigo = input("Código do livro: ")

            if codigo == "":
                print("Código do livro não informado.")

            else:
                titulo = input("Título do livro: ")

                if titulo == "":
                    print("O título do livro não pode ficar vazio.")

                else:
                    autor = input("Nome do autor: ")

                    if autor == "":
                        print("O nome do autor não pode ficar vazio.")

                    else:
                        ano = int(input("Ano de publicação: "))

                        if ano <= 0:
                            print("Ano de publicação inválido.")

                        else:
                            quantidade = int(input("Quantidade disponível: "))

                            if quantidade <= 0:
                                print("A quantidade disponível deve ser maior que zero.")

                            else:
                                print("Livro cadastrado com sucesso!")
elif opcao == "2":

        quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))

        for aluno in range(quantidade_alunos):

            print("----- ALUNO", aluno + 1, "-----")

            matricula = input("Matrícula: ")

            if matricula == "":
                print("Matrícula não informada.")

            else:
                nome = input("Nome do aluno: ")

                if nome == "":
                    print("O nome do aluno não pode ficar vazio.")

                else:
                    turma = input("Turma: ")

                    if turma == "":
                        print("A turma não pode ficar vazia.")

                    else:
                        print("Aluno cadastrado com sucesso!")

elif opcao == "3":

        print("----- EMPRÉSTIMO -----")

        codigo_livro = input("Código do livro: ")

        if codigo_livro == "":
            print("Código do livro não informado.")

        else:
            matricula_aluno = input("Matrícula do aluno: ")

            if matricula_aluno == "":
                print("Matrícula do aluno não informada.")

            else:
                quantidade_disponivel = int(
                    input("Quantidade disponível: ")
                )

                if quantidade_disponivel > 0:
                    print("Empréstimo realizado com sucesso!")

                else:
                    print("Não é possível realizar o empréstimo.")
elif opcao == "4":

        print("----- DESLIGANDO SISTEMA -----")
