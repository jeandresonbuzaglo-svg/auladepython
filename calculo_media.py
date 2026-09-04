nome = input("digite seu nome: ")
nota1 = float(input("digite a 1 nota: "))
nota2 = float(input("digite a 2 nota: "))
media = (nota1 + nota2) / 2

if media >= 7 :
    print ("Aprovado")

elif media >=6:
    print ("recuperação")    
else:
    print ("reprovado") 

