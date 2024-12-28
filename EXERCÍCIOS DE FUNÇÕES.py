# 1 - Desenvolva uma função que peça dois valores, sendo estes, a largura e o comprimento de um terreno, 
# e depois mostre para o usuário a área total deste terreno.
def linha():
  print()
  print(50 * '-')
  print()  

def titulo(nome):
    print()
    print(10*'--')
    print(nome)
    print(10*'--')
    print()

def calculoArea(lar,com):
    a = lar * com
    print(f'A área desde terreno de {lar}m x {com}m é de {a}m²')


titulo('  ÁREA DO TERRENO   ')

lar= float(input('Largura (m): '))
com= float(input('Comprimento (m): '))

calculoArea(lar,com)

linha()

# 2 - faça uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
# adaptável.

def escreva(texto):
    print(f'~{len(texto) * "~"}~')
    print(f' {texto} ')
    print(f'~{len(texto) * "~"}~')



# texto = str(input('Escreva seu texto: '))
escreva('texto')

linha()

# 3 - faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo e realize a contagem.
# seu programa deve realizar três contagens:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2.
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    
    if fim >= inicio:
        print(15 * '-=-')
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for i in range(inicio,fim+1,passo):
            print(i, end= ' ', flush=True)
            sleep(0.3)
        print('FIM')


        if passo==0:
            print(15 * '-=-')
            print(f'Contagem de {inicio} até {fim} de 1 em 1:')
            for i in range(inicio,fim+1,1):
                print(i, end= ' ', flush=True)
                sleep(0.3)
            print('FIM')

    
    else:
        if passo>0:
            print(15 * '-=-')
            #Se o passo for um número positivo:

            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')

            #Convertemos o passo para m número negativo:

            passo = passo - (passo*2)

            for i in range(inicio,fim-1,passo):
                print(i, end= ' ', flush=True)
                sleep(0.3)
            print('FIM')
        
        
        elif passo<0:
                positivo = passo - (passo*2)
                print(15 * '-=-')
                print(f'Contagem de {inicio} até {fim} de {positivo} em {positivo}:')
                for i in range(inicio,fim-1,passo):
                    print(i, end= ' ', flush=True)
                    sleep(0.3)
                print('FIM')
        
        else:
            if passo==0:
                print(15 * '-=-')
            print(f'Contagem de {inicio} até {fim} de 1 em 1:')
            for i in range(inicio,fim-1,-1):
                print(i, end= ' ', flush=True)
                sleep(0.3)
            print('FIM')


contador(1, 10, 1)
contador(10,0,2)
contador(10,0,0)
contador(5,-5,0)
contador(10,0,-1)
inicio= int(input('início: '))
fim=int(input('Fim: '))
passo=int(input("Passo: "))
contador(inicio,fim,passo)


#3 - crie uma função chamada maior(), que receba vários parâmetros com valores inteiros. seu programa deve analisar todos os parâmetros
#e dizer qual é o maior.

def maior (*n):
    for i in n:
        print (i, end= ' ')
    print()
    print (f'Foram informados {len(n)} números.')
    print (f'E o maior valor informado foi {max(n)}')

maior (1,2,10,4,5)

#4- faça um programa que tenha uma lista chamada numeros e duas funções  chamadas sorteia() e somaPar().
# a primeira função vai sortear 5 números e coloca-los dentro da lista e a segunda vai mostrar a soma dos numeros pares dentro desta.

from random import randrange

lista=[]

def sorteia():

    for i in range(6):
        lista.append(randrange(0,20))

    print ('Sorteando 5 valores da lista : ', end= '')
    for i in lista:
        print (i, end= ' ')
    print ()

def somaPar():
    cont=0
    for i in lista:
        if i %2==0:
            cont+=i
    print (f'Somando os valores pares de {lista} temos {cont}')

sorteia()
somaPar()
