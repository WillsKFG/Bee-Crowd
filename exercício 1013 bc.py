entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorAB = (a+b+abs(a-b))//2
maiorC = (maiorAB + c + abs(maiorAB - c))//2
print(f"{maiorC} eh o maior")