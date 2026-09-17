notas = []

for i in range(5):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

print("\nNotas cadastradas:")
for nota in notas:
    print(nota)

print(f"\nQuantidade de notas armazenadas: {len(notas)}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")


