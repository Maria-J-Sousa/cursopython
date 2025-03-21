#Entrada dos dados
while True:
    nota1      =float(input("Digite sua nota do 1º Bimestre: "))
    if (nota1<=10) and (nota1>=0):
        break
while True:
    nota2      =float(input("Digite sua nota do 2º Bimestre: "))
    if(nota2<=10)  and (nota2>=0):
        break
while True:
    nota3      =float(input("Digite sua nota do 3º Bimestre: "))
    if(nota3<=10)  and (nota3>=0):
        break
while True:
    nota4      =float(input("Digite sua nota do 4º Bimestre: "))
    if(nota4<=10) and (nota4>=0):
        break
#Processamento
media          =(nota1+nota2+nota3+nota4)/4
#Saída de dados
print("Média Final é: ",media)
print(f"Sua média é {media:,.2f}")
if(media  >=5):
    print("Aluno APROVADO!!!")
elif(media>=3):
    print("Aluno em RECUPERAÇÃO")
else:
    print("Aluno REPROVADO!!!")
print("FIM DO ANO LETIVO!!!")