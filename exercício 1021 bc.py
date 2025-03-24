# Ler o valor monetário com duas casas decimais
valor = float(input())

# Converter para centavos para evitar problemas de ponto flutuante
centavos = int(round(valor * 100))

# Listas de notas e moedas disponíveis (em centavos)
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    qtd_notas = centavos // nota
    print(f"{qtd_notas} nota(s) de R$ {nota / 100:.2f}")
    centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = centavos // moeda
    print(f"{qtd_moedas} moeda(s) de R$ {moeda / 100:.2f}")
    centavos %= moeda
