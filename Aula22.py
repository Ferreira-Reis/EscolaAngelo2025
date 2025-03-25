# EXERCÍCIOS WHILE

#  1. Adivinhação de números:
#  • Criem uma lista com 10 números.
#  • Peçam ao usuário para adivinhar um número da lista.
#  • Usem um loop while para continuar pedindo adivinhações até que o usuário acerte.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
acertou = False
while not acertou:
    palpite = int(input("Adivinhe um número da lista: "))
    if palpite in numeros:
        print("Parabéns! Você acertou o número.")
        acertou = True
    else:
        print("Não foi dessa vez. Tente novamente!")

#  2. Contagem regressiva:
#  • Criem uma lista de contagem regressiva de 10 a 1.
#  • Usem um loop while para imprimir cada número da lista
contagem_regressiva = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
i = 0 
while i < len(contagem_regressiva):
    print(contagem_regressiva[i])
    i += 1  

# 3. Adição de números:
#  • Criem uma lista vazia para armazenar números.
#  • Peçam ao usuário para fornecer números e os adicionem à lista.
#  • Continuem pedindo números até que o usuário decida parar.
numeros = []
while True:
    entrada = input("Digite um número para adicionar à lista ou 'parar' para encerrar: ")
    if entrada.lower() == 'parar':
        break
    try:
        numero = float(entrada) 
        numeros.append(numero) 
    except ValueError:
        print("Por favor, digite um número válido ou 'parar' para encerrar.")
print("Os números adicionados foram:", numeros)

#  4.Média de notas:
#  • Criem uma lista vazia para armazenar notas.
#  • Peçam ao usuário para fornecer notas e as adicionem à lista.
#  • Calculem e imprimam a média das notas quando o usuário decidir parar
notas = []
while True:
    entrada = input("Digite uma nota ou 'parar' para encerrar: ")
    if entrada.lower() == 'parar':
        break
    if entrada.isdigit():  
        nota = int(entrada) 
        notas.append(nota)  
    else:
        print("Por favor, digite uma nota válida ou 'parar' para encerrar.")
if len(notas) > 0:
    media = sum(notas) / len(notas)  
    print(f"A média das notas é: {media:.2f}") 
    print("Nenhuma nota foi fornecida.")

# 5.Busca em lista:
#  • Criem uma lista de cinco nomes.
#  • Peçam ao usuário para digitar um nome.
#  • Usem um loop while para verificar se o nome está na 
# lista e informar o resultado.
nomes = ["Ana", "Carlos", "João", "Maria", "Pedro"]
while True:
    nome_usuario = input("Digite um nome para procurar na lista: ")
    if nome_usuario.lower() in [nome.lower() for nome in nomes]:
        print(f"O nome {nome_usuario} está na lista!")
        break
    else:
        print(f"O nome {nome_usuario} não está na lista. Tente novamente.")

#  6. Contador de números:
#  • Solicitem ao usuário um número inicial.
#  • Usem um loop while para imprimir os números de 1 até o 
# número fornecido pelo usuário.
#  • Exibam uma mensagem indicando que o loop terminou
# Solicitar um número inicial ao usuário
numero_final = int(input("Digite um número para contar até ele: "))
contador = 1
while contador <= numero_final:
    print(contador)
    contador += 1 
print("Número encontrado!")