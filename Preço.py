#entrada de dados
while True:
    preco1 = float(input("Digite o 1º preço do produto; "))
    if preco1 <=0:
        break
while True:
    preco2 = float(input("Digite o 2º preço do produto; "))
    if preco1 <=0:
        break
while True:
    preco3 = float(input("Digite o 3º preço do produto; "))
    if preco1 <=0:
        break
#processamento
media = (preco1+preco2+preco3)/3
print("A média do preço deste produto é: media")
