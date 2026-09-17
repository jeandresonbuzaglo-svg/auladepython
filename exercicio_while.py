#1 exercico contagem

contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1


#2 exercicio numeros pares

contador = 2

while contador <= 10:
    print(contador)
    contador = contador + 2

#3 exercicio  -  cadastro


print("_______cadastro de alunos_______")
quantidade = int(input("Quantos serão alunos cadastrado? "))
contador = 1

while contador <= quantidade:
    nome = input("digite o nome do aluno: ")
    print("aluno cadastrado :" , nome)
    contador = contador + 1
print("cadastrado com sucesso! ")


#4 exercicio menu simples

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


#5 exercicio validação


contador = 1

while contador <=5: 
    idade = int(input("Digite a idade: "))
    while nota < 0 or nota > 120:
        print("idade inválida")
  
    contador = contador + 1
print("Cadastro finalizado!")
