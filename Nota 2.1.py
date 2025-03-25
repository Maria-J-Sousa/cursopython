#Entrada dos dados
def PedirNota(frase):
    while True:
        nota = float(input(frase))
        if nota >=0 and nota<=10:
            break
    return nota


nota1      = PedirNota("Digite sua nota do 1º Bimestre: ")
nota2      = PedirNota("Digite sua nota do 2º Bimestre: ")
nota3      = PedirNota("Digite sua nota do 3º Bimestre: ")
nota4      = PedirNota("Digite sua nota do 4º Bimestre: ")

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