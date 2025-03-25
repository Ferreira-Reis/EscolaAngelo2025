# O loop for (laço de repetição for)

lista_numeros = [54, 23, 18, 99, 15]

i = 0
while i < len(lista_numeros):
    print(lista_numeros[i], end= " ")
    i += 1

print()
for elemento in lista_numeros:
 print(elemento, end= " ")

print()
i = 0
for el in lista_numeros:
 print(f"Indice = {i}, elemento = {el}")
 i += 1

for elemento in enumerate(lista_numeros):
 print(elemento)

 for indice,  elemento in enumerate(lista_numeros):
    print("Indice:", indice, "Elemento", elemento)

for numero in range(9):
 print(numero)

for numero in range(1, 9):
 print(numero)

print()
for numero in range(1, 9, 2):
 print(numero)

print()
lista_com_range = list(range(1, 11))
print(lista_com_range)