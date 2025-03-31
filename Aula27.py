# Exercícios

#  1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. Concatene-as e imprima o resultado.
string1 = "Olá"
string2 = "Mundo"
resultado = string1 + " " + string2 
print(resultado)

#  2. Dada a string “Python”, imprima o caractere que está no índice 2.
string = "Python"
caractere_indice_2 = string [2]
print(caractere_indice_2)

#  3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.
string_original = "exemplo"
nova_string = string_original[:1] + "y" + string_original[2:]
print(nova_string)

#  4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.
nome = input("Digite seu nome: ")
comprimento_nome = len(nome)
print(f"O comprimento do seu nome é: {comprimento_nome}")

#  5. Crie uma string que represente uma frase. Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)
frase = "O gato preto pulou a cerca."  # Substitua pela sua frase
palavra_procurada = "gato"

if palavra_procurada in frase:
  print(True)
else:
  print(False)

#  6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.
frase = input("Digite uma frase: ")
palavras = frase.split()  # Divide a frase em palavras
numero_palavras = len(palavras)
print(f"O número de palavras na frase é: {numero_palavras}")

#  7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas. Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.

#  8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final. Remova esses espaços e imprima a string resultante.
string_com_espacos = input("Digite uma string com espaços no início e no final: ")
string_sem_espacos = string_com_espacos.strip()
print(f"String sem espaços: '{string_sem_espacos}'")

#  9. Crie uma função que receba um número inteiro e retorne uma string que o represente com separadores de milhares. Por exemplo, para o número 1234567, a função deve retornar “1,234,567”.
