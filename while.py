# estrutura básica do while

contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1

# while com entrada do usuário

senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
print ("Acesso permitido!")

#5 while para repetir determinadas vezes
print("_______cadastro de alunos_______")
quantidade = int(input("Quantos alunos? "))
contador = 1

while contador <= quantidade:
    nome = input("digite o nome do aluno: ")
    print("aluno cadastrado :" , nome)
    contador = contador + 1
print("cadastrado com sucesso! ")

#6 while com menu

opcao = 0
while opcao != 3:
    print("1 - cadastrar aluno")
    print("2 - lista de aluno")
    print("3 - sair")
    opcao = int(input("escolha uma opção: "))
    if opcao == 1:
        print("cadastro de aluno")
    elif opcao == 2:
        print("lista de alunos")
    elif opcao == 3:
        print("____saindo____")
    else:
        print("Opção inválida!")

#7 um ex. proximo da nossa atividade: cadastro de livros  


quantidade = int(input("quantos livros deseja cadastrar? "))
contador = 1
while contador <= quantidade:
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor: ")
    print("Livro:" , titulo)
    print("Autor:" , autor)
    contador = contador + 1
print("Cadastro finalizado!")

#8 while + if : repetição com decisão


contador = 1

while contador <=5: 
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")    
    contador = contador + 1
print("Cadastro finalizado!")


#9 while para validar dados

nota = float (input("Digite uma nota de 0 a10:"))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Digite uma nota de 0 or 10: "))
print("Nota registrada:" , nota)

