# EXERCÍCIOS FOR

#  1.Faça um programa que imprima cada elemento da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando o for.
lista = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
for elemento in lista:
    print(elemento)

#  2. Faça um programa que imprima cada elemento da lista [3, 8, 30, 8, 19, -12, -2, -1, -7, -48] usando o for com range.
lista = [3, 8, 30, 8, 19, -12, -2, -1, -7, -48]
for i in range(len(lista)):
    print(lista[i])

#  3. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for
numeros = [10, 25, 3, 42, 17, 8, 30, 12, 5, 20]
for numero in numeros:
    print(numero)

#  4. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for com range
numeros = [10, 25, 42, 17, 8, 30, 12, 5, 20]
for i in range(len(numeros)):
    print(numeros[i])

# 5. Faça um programa que imprima todos os itens da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando while e compare-o com o exercício 1.
lista = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
i = 0 
while i < len(lista):
    print(lista[i])
    i += 1

#  6. Faça um programa que imprima todos os números de 5 a 0 usando o for.
for numero in range(5, -1, -1):
    print(numero)

#  7. Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1
n = int(input("Digite um numero inteiro n: "))

lista = []
for i in range(n):
    lista.append(i)

    print(lista)

# 8. Faça um programa que imprima o maior número da lista [-8, -6, 3, -1, 7], sem usar o método max().
lista = [ -8, -6, 3, -1, 7]

maior_numero = lista[0]  # Inicializa o primeiro elemento da lista

for numero in lista:
    if numero > maior_numero:
        maior_numero = numero

    print("O maior numero da lista é:", maior_numero)

# 9. Agora, usando o método max(), faça um programa que imprima os três maiores números da lista [2, 9, -5, 2, -8, 4, -9, -5, 4, 1].
lista = [2, 9, -5, 2, -8, 4, -9, -5, 4, 1]

# Ordena a lista em ordem decrescente
lista_ordenada = sorted(lista, reverse=True)

# Imprima os três primeiros elementos da lista ordenada
print("Os três maiores numeros da lista são:", lista_ordenada[:3])
