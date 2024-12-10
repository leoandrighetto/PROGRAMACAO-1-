# 1 Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
l=[]
for i in range(5):
    l.append(int(input()))
print(l)

#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

l=[]
for i in range(10):
    l.append(int(input()))
print(l[::-1])

#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

l=[]
for i in range(4):
    l.append(int(input()))
print(l)
print((sum(l))/(len(l)))

#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

v=[]
con=[]
vogais="aeiouAEIOU"
for i in range(10):
    c=input()
    if c in vogais:
        v.append(c)
    else:
        con.append(c)
print()
print(con)
print(len(con))

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

l=[]
par=[]
impar=[]
for i in range(20):
    a=int(input())
    l.append(a)
    if a%2==0:
        par.append(a)
    else:
        if a%2!=0:
            impar.append(a)
print(l)
print(par)
print(impar)

#
