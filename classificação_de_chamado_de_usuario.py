nome = input("Digite o nome do usuario: ")
tipo_problema = int(input("Digite a prioridade do usuario: "))

print ("1 - indisponivel")
print ("2 - lentidão")
print ("3 - não impede de trabalhar")
print ("4 - outros problemas")

if tipo_problema == 1:
    situacao = ("critica")
elif tipo_problema == 2:
    situacao = ("Alta")
elif tipo_problema == 3:
    situacao = ("Média")
elif tipo_problema == 4:
    situacao = ("Baixa")
else:
    situacao = (" Opção Inválida! Preste atenção..")

print("\n--- Chamado de suporte técnico ao usuario ---")
print("nome do usuario:", nome)
print("Prioridade do Problema:", tipo_problema)
print("Situação:", situacao)