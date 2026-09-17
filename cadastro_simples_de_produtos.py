produtos = []

for i in range(6):
    produto = input(f"Digite o nome do { i + 1}º produto: ")
    produtos.append(produto)

print("Produtos cadastrados:")
for i in range(len(produtos)):
    print(f"{i + 1}. {produtos[i]}")

pesquisa = input(" Digite o nome do produto que deseja pesquisar: ")

if pesquisa in produtos:
    print("Produto encontrado!")
else:
    print("Produto não encontrado.")

print("Quantidade de produtos cadastrados: {(len(produtos)}")

remover = input("\nDigite o nome do produto que deseja remover: ")

if remover in produtos:
    produtos.remove(remover)
    print("Produto removido com sucesso!")
else:
    print("Produto não encontrado para remoção.")

