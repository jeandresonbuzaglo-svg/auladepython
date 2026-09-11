nome = input("Digite o nome do cliente: ")
velocidade = int(input("velocidade contratada de internet: "))

if velocidade < 50:
    plano = " Plano basico"
elif velocidade <= 200:
    plano = "Plano Intermediário"
elif velocidade <= 500:
    plano = "Plano avançado"
else:
    plano = "Plano Ultra"

print("--- Velocidade Contratada do Cliente ---")
print("nome do Cliente:", nome)
print("Velocidade Contratada:", velocidade, "Mbps")
print("Tipos de planos:", plano)

