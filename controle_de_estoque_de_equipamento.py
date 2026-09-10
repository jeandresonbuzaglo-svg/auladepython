produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade disponível no estoque: "))

if quantidade == 0:
    situacao = "Produto esgotado"
elif quantidade <= 5:
    situacao = "Estoque crítico"
elif quantidade <= 20:
    situacao = "Estoque baixo"
else:
    situacao = "Estoque normal"

print("\n--- Situação do Estoque ---")
print("Produto:", produto)
print("Quantidade disponível:", quantidade)
print("Situação:", situacao)