class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibir_dados(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Disponível:", self.disponivel)

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Empréstimo realizado!")
        else:
            print("Livro já emprestado!")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print("Devolução realizada!")
        else:
            print("O livro já está disponível!")


biblioteca = []


def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")

    novo_livro = Livro(titulo, autor)
    biblioteca.append(novo_livro)

    print("Livro cadastrado!")


def listar_livros():
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for livro in biblioteca:
            livro.exibir_dados()
            print("--------")


def emprestar_livro():
    titulo = input("Título para empréstimo: ")

    for livro in biblioteca:
        if livro.titulo == titulo:
            livro.emprestar()
            return

    print("Livro não encontrado.")


def devolver_livro():
    titulo = input("Título para devolução: ")

    for livro in biblioteca:
        if livro.titulo == titulo:
            livro.devolver()
            return

    print("Livro não encontrado.")


while True:
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        emprestar_livro()

    elif opcao == "4":
        devolver_livro()

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")



       