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

# l = [5,8,2,4,3,7,9,9]
# l1 = []

# for i in l:
#     if i<=l[-1]:
#         l1.insert(0,i)
    
# print(l1)



l = [71,15,72,17,18,18]

lnova = []

for i in range(len(l)):
    print(l[0])


# l.insert(0,4)

# print(l[i])
