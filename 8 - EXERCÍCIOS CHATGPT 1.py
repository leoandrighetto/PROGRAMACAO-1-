# 1 - Soma dos N primeiros números inteiros: 
# Crie um programa que receba um número n e calcule a soma dos 
# n primeiros números inteiros. 
# Exemplo: se n = 5, a saída deve ser 15 (1 + 2 + 3 + 4 + 5).




# n = int(input('DIGITE UM NÚMERO: '))
# soma = 0

# for i in range(0, n+1):
#     soma += i

# print(f'A soma final é {soma}!')





# 2 - Fatorial de um número: 
# Escreva uma função que calcule o fatorial de um número inteiro não-negativo. 
# Lembre-se de que o fatorial de n é n! = n * (n-1) * ... * 1.

# n = int(input('DIGITE UM NÚMERO: '))
# m = 1
# for i in range(1,n+1):
#     m *= i

# print(f'O fatorial de {n} é {m}!')





# 3 - Palíndromo: 
# Crie uma função que verifique se uma palavra
# ou frase é um palíndromo 
# (uma palavra ou frase que lê da mesma forma de trás para frente,
#  desconsiderando espaços e pontuações).

# def palindromo(n):

#     frase = n.lower()
#     frase = ''.join(i for i in frase if i.isalnum())

#     teste = frase[::-1]

#     if teste == frase:
#         return 'sim'
#     else:
#         return 'não'

# print(palindromo('roma e amor'))

# # saída = 'sim'






# 4 - Números Primos: Crie uma função que determine se um número é primo.
# Um número é primo se ele for maior que 1 e não tiver divisores além de 1 e ele mesmo.


# def primo(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c+=1
#     if c==2:
#         return 'é primo'
#     else:
#         return 'não é primo'

# n = int(input('DIGITE UM NÚMERO PARA VERIFIRA SE É PRIMO: '))    
# print(primo(n))



# 5 - Tabuada: Escreva um programa que mostre a tabuada de um 
# número fornecido pelo usuário. A tabuada deve ir de 1 a 10.

# def tabuada(n):

#     for i in range(1,11):

#         print(f'{i} X {n} = {i*n}')

# n = int(input('DIGITE O NÚMERO DA TABUADA DESEJADA: '))
# tabuada(n)


# 6 - Contagem de vogais: Crie uma função que receba uma string e retorne o 
# número de vogais (tanto maiúsculas quanto minúsculas) presentes nela.

# def contagemVogais(s):
#     v='aeiouáàéíóú'
#     c=0

#     for i in s.lower():
#         if i in v:
#             c+=1
#     return c


# s = 'bapibaquígrafo'

# print(contagemVogais(s))


# 7 - Contagem de números pares e ímpares: Dado um número n, 
# crie um programa que conte quantos números pares e quantos números ímpares 
# existem entre 1 e n.

# def contagemPI(n):

#     p = 0
#     i = 0
#     for a in range(1,n+1):
#         if a%2==0:
#             p+=1
#         else:
#             i+=1
#     return f'Quantidade de pares: {p}, quantidade de ímpares: {i}'

# n = int(input('DIGITE UM NÚMERO: '))
# print(contagemPI(n))



# 8 - Fibonacci: Escreva um programa que calcule o enésimo número da sequência de Fibonacci.
# A sequência de Fibonacci é a sequência onde cada número é a soma dos dois anteriores 
# (1, 1, 2, 3, 5, 8, 13...).

# def Nfibonacci(n):

#     l=[0,1]
#     if n>=2:
#         for i in range(n-2):

#             fibo = l[-1]+l[-2]
#             l.append(fibo)
#         print(l)
#         return f'O número {n} da posição em fibonacci é {l[-1]}'
    
#     else:
#         if n<2:
#             return f'O número da posição {n} em fibonacci é {l[n]}'
        
# while True:
#     n = int(input('DIGITE UM NÚMERO DA PODIÇÃO DE FIBONACCI: '))

#     print(Nfibonacci(n))

        


# 9 - Média e Desvio Padrão: 
# Crie um programa que calcule a média e o desvio padrão
# de uma lista de números fornecida pelo usuário.

# def mediaDesvio(*n):

#     media = sum(n)/len(n)
#     soma = 0

#     for i in n:
#         quadrado = (i-media)**2
#         soma+=quadrado

#     desvio = (soma/len(n))**(1/2)
#     return f'{desvio:.2f}'

#print(mediaDesvio(10,29,3,45,66,2,34,50))
#SAÍDA = 21.94



# 10 - Ordenação de Lista: 
# Dada uma lista de números inteiros, 
# escreva um programa que ordene a lista em ordem crescente sem usar o método sort().

# def crescente():
#     l = []

#     n = int(input('DIGITE A QUANTIDADE DE NÚMEROS DE SUA LISTA: '))
#     for i in range(n):
#         e = int(input('DIGITE UM NÚMERO PARA A SUA LISTA: '))
#         l.append(e)

#     ln = []
#     for a in range(len(l)):
#         for i in l:
#             ln.append(min(l))
#             del l[l.index(min(l))]
#     print(f'SUA LISTA EM ORDEM CRESCENTE: {ln}') 

# crescente()

# print(l[i])

# # 11 Cédulas de Saque (Caixa Eletrônico)
# Um caixa eletrônico precisa entregar o menor número possível de cédulas para um saque. 
# Escreva um programa que leia o valor a ser sacado (valor inteiro) e informe quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5 e R$2. Não há necessidade de tratar valores que não podem ser sacados.
    
# 12. Média Ponderada de Notas
# Em uma prova com três questões, o candidato pode obter diferentes pesos para cada questão. 
# Escreva um programa que leia as três notas do aluno e os respectivos pesos, e calcule a média ponderada.

# 3. Soma dos Divisores
# Dado um número inteiro positivo, escreva um programa que calcule a soma de todos os seus divisores, incluindo ele mesmo.
