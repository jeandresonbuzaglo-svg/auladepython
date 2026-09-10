nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
cadastro = input("Possui cadastro ativo? (sim/não): ").lower()

if cadastro == "não":
    situacao = "Acesso negado"
elif idade < 14:
    situacao = "Acesso permitido somente com acompanhamento"
else:
    situacao = "Acesso permitido"

print("Aluno:", nome)
print("Situação de acesso:", situacao)
