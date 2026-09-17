nome = input("digite seu nome: ")
nota1 = float(input("digite a 1 nota: "))
nota2 = float(input("digite a 2 nota: "))
nota3 = float(input("digite a 3 nota: "))
nota4 = float(input("digite a 4 nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 :
    print ("Aprovado")

elif media >=6:
    print ("recuperação")    
else:
    print ("reprovado") 