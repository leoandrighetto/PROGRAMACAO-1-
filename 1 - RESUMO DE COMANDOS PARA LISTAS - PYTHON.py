#SUBSTITUIR:
notas=['Dó','Ré','Mi','Fá',]

notas[3]='Mib'
print(f'{notas}notas[3]="Mib" SUBSTITUIR "Fá" POR "Mib"')
print()

#   .APPEND para adicionar ao FINAL da lista:
notas=['Dó','Ré','Mi','Fá',]

notas.append('Sol')
notas.append('Lá')

print(f'{notas}-notas.append("Sol") adicionar ao final "Sol" E "Lá"')
print()

#    .INSERT

notas=['Dó','Ré','Mi','Fá',]

notas.insert(2,'Lá')

print(f'{notas}-notas.insert(2,"Lá") "Lá" NO ÍNDICE 2')
print()

#.DEL deletar da lista:

notas=['Dó','Ré','Mi','Fá',]

del notas[0]

print(f'{notas} del / notas [0]--deletar nota "Dó"')
print()

#POP para deletar da lista (geralmente para eleminar o último elemento):

notas=['Dó','Ré','Mi','Fá',]

notas.pop(0)
print(f'notas=["Dó","Ré","Mi","Fá",]')
print(f'{notas}--notas.POP (0) para eliminar "Dó"')
print()

#REMOVE para remover da lista:

notas=['Dó','Ré','Mi','Fá',]

notas.remove('Ré')
print(f'notas=["Dó","Ré","Mi","Fá",]')
print(f'{notas} notas.remove ("Ré") para remover Ré')
print()

#USANDO UM RANGE em uma lista:

ranges=list(range(4,11))
print(f'{ranges}ranges=list(range(4,11))')
print()

#SORT para colocar a lista em ordem:

print()
print("antes: [9,5,7,3,2,6]")
print()
lista=[9,5,7,3,2,6]
print()

lista.sort()
print(f'Depois: {lista}' )
print()

#SORT REVERSE para colocar a lista em ordem INVERSA:

print()
print("antes: [9,5,7,3,2,6]")
lista=[9,5,7,3,2,6]
print()
lista.sort(reverse=True)
print(f'Depois: {lista}' )
print()

#LEN para saber quantos elementos existem na lista:

lista=[9,5,7,3,2,6]

print(f'{len(lista)} ---- len(lista) mostra nº elementos')
print()

#PARA DEIXAR A LISTA BONITA, EXEMPLO 1:

valores=[]
valores.append(0)
valores.append(1)
valores.append(2)
valores.append(3)

for v in valores:
    print(f'{v}...',end='')
print()
print()
#EXEMPLO 2:

valores=[]
valores.append(1)
valores.append(2)
valores.append(3)
valores.append(4)
print(f'valores= 0,1,2,3')
print()
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print()

#PARA ADICIONAR UMA LISTA COM INT:
'''
valores=list()
for cont in range(0,4):
    valores.append(int(input()))

print(f'cont= 4 Posições: 0,1,2,3 (4). E os valores são {valores}')
print()

valores=[]
for cont in range(0,4):
    valores.append(int(input()))
    
for c, v in enumerate(valores):
    print(f'{c} = {v}')
print(f'Usamos o "enumerate" para enumerar as posições')
print()
'''
#PARA ENCONTAR O INDICE DE UM ELEMENTO EM UMA LISTA:

notas=[1,2,3,4,5,6,7]
print(f'índice do número 4 da lista "notas": {notas.index(4)}')

#FUNÇÕES RANDOM

#RANDOM RANDINT
#CRIANDO UMALISTA ALEATORIA COM UM LAÇO
import random #IMPORTAR O RANDOM PARA CRIAR ALEATORIEDADE
l=[]
#n=int(input())
for a in range(10):   #QUANTIDADE DE ELEMENTO DENTRO DA LISTA
    ran=random.randint(1,10)   #VARIAVEL QUE RECEBERÁ UM NÚMERO ALEATÓRIO
    l.append(ran)               #ATRAVÉS DO COMANDO random.radint(entre pri. n e o últ. n)
print(l)

#MATRIZES

#NP.RANDOM.RAND PARA CRIAR UMA MATRIZ ALEATÓRIA COM NÚMEROS ENTRE 0 E 1 
#ONDE VOCÊ DETERMINA O NÚMERO DAS DIMENSÕES

#PARA LISTAS COM ELEMENTOS DUPKLICADOS:
'''
l=[]
n=1
while n!=0:
    n=int(input())
    if n not in l:
        l.append(n)
        
print(l)
'''
