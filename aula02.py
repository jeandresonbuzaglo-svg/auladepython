nome = input ("digite seu nome: ")
idade = int(input ("digite sua idade: "))
altura = float(input("digite seu altura: "))

print ("O nome informado foi:", nome)
print ("A idade informada foi:", idade)
print ("A altura informada foi:", altura)

if idade >= 18:
    print ("voto obrigatorio")
elif idade >=16:
    print ("voto não obrigatório")
else: 
    print (" não pode votar")  