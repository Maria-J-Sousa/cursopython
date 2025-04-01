'''Montar um programa, utilizando o while, que monte a tabuada do 2'''

n = 2
while n <=10:
    print("Tabuada do número: ", n)
    x = 1
    while x <=10:
        print(n,"*", x, "=", x*n)
        x=x+1
    n=n+1

