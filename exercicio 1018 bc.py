#ler um valor e imprimir a quantidade de notas necessárias para pagar esse valor, considerando notas de 100, 50, 20, 10, 5, 2 e 1.
N = int(input())
cedula=[100,50,20,10,5,2,1]
print(N)
for cedulas in cedula:
    quantidade = N//cedulas
    N%=cedulas
    print(f"{quantidade} nota(s) de R$ {cedulas},00")