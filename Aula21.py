# aula21.py

# EXERCÍCIOS DE FIXAÇÃO

# 1. adicione o número 50 ao final da lista.
lista_numeros = [10, 20, 30, 40]
lista_numeros.append(50)
print(lista_numeros)


# 2. Adicione "laranja" ao índice 1 da lista.
lista_frutas = ["maça", "banana", "uva"]
lista_frutas.insert(1,"laranja")
print(lista_frutas)

# 3. Remova "cachorro" da lista.
lista_animais = ["cachorro", "gato", "pássaro", "cachorro"]
lista_animais.remove("cachorro")
print(lista_animais)

# 4. Remova o elemento de índice 2 da lista e mostre o elemento removido
lista_nomes = ["Alice", "Bob", "Charlie", "David"]
valor_removido = lista_nomes.pop(2)
print(lista_nomes)
print(valor_removido)

# 5. encontre o índice da primeira ocorrência de 'azul na lista.
lista_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'azul']
índice_azul = lista_cores.index('azul')
print(índice_azul)

# 6. Conte quantas vezes o número 2 aparece na lista.
lista_numeros_repetidos = [1, 2, 3, 2, 4, 2, 5, 2]
quantidade_de_dois = lista_numeros_repetidos.count(2)
print(quantidade_de_dois)

# 7. Ordene a lista em ordem crescente.
lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)