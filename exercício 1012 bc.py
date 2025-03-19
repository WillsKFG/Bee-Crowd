#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

entrada =  input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

area_triangulo = A * C/2
area_circulo = 3.14159 * C**2
area_trapezio = (A+B)*C/2
area_quadrado = B*B
area_retangulo = A*B

print(f'''TRIANGULO: {area_triangulo:.3f}
CIRCULO: {area_circulo:.3f}
TRAPEZIO: {area_trapezio:.3f}
QUADRADO: {area_quadrado:.3f}
RETANGULO: {area_retangulo:.3f}''')