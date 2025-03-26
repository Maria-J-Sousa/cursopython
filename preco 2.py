def PedirPreco (frase):
    while true:
        preco = float(input(frase))
        if preco >=0:
            break
    return preco
preco1 = PedirPreco("Digite o 1º preço do produto: ")
preco2 = PedirPreco("Digite o 2º preço do produto: ")
preco3 = PedirPreco("Digite o 3º preço do produto: ")

#processamento
media = (preco1+preco2+preco3)/3
print(f"A média do preço deste produto é: R$ {media:,.2f}")

