# 1. Faça um programa que peça a idade do usuário e imprima se ele é maior ou menor que 18 anos.

idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("É de maior!")
else:
    print("É de menor!")

# 2. Faça um programa que peça um número e mostre se ele é positivo ou negativo.

número = int(input("Digite um número inteiro:"))

if número >= 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")

# 3. Faça um programa que, dado um número digitado, mostre se ele é par ou impar.
número = int(input("Digite um número inteiro:"))
if número % 2 == 0:
 print("O número é par. ")
else:
 print("O número é impar. ")

# 4. Faça um programa que peça dois números e mostre o maior deles.

n1 = int(input("Digite um inteiro: "))
n2 = int(input("Digite outro inteiro:"))

if n1 > n2:
 print(n1)
else:
 print(n2)

# 5. Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, f ou outro;

idade = int(input("Digite a idade maior que 0 menor 150: "))
if idade > 0 and idade < 150:
 print("idade válida")
else:
 print("idade inválida")

Salário = int(input("Digite o salário: R$ "))
if Salário > 0:
 print(f"O salário é R$ {Salário}")
else:
 print("Salário inválido")

sexo = input("Digite o sexo [M, F, outro]: ")
if sexo.upper == "M":
 print("Sexo masculino")
elif sexo.upper == "F":
 print("Sexo feminino.")
elif sexo.lower == "outro":
 print("Sexo outro")
else:
 print("Sexo inválido")