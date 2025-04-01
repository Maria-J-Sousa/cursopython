tabuada = 2
contador = 1

while tabuada <=10:
    print(f'{tabuada} X {contador} = {tabuada*contador}')
    contador = contador + 1
    if contador==11:
        tabuada=tabuada+1
        contador=1
