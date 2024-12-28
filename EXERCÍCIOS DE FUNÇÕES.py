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

3 - faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo e realize a contagem.
seu programa deve realizar três contagens:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2.
c) uma contagem personalizada

def contador(inicio,fim,passo):
    

    if passo==0:
        print(15 * '-=-')
        print(f'Contagem de {inicio} até {fim} de 1 em 1:')
        for i in range(inicio,fim+1,1):
            print(i, end= ' ')
    
    elif fim > inicio and passo!=0:
        print(15 * '-=-')
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        fim+=1
        for i in range(inicio,fim,passo):
            print(i, end= ' ')
    
    elif inicio > fim and passo>=0 :
        print(15 * '-=-')
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        fim-=1
        passo = passo - (passo*2)
        for i in range(inicio,fim,passo):
            print(i, end= ' ')

    else:
        if inicio > fim and passo<0:
            print(15 * '-=-')
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
            fim -= 1
            for i in range(inicio,fim,passo):
                print(i, end= ' ')

    

    print('FIM')
    print(15 * '-=-')

contador(1, 10, 1)
contador(10,0,2)
inicio= int(input('início: '))
fim=int(input('Fim: '))
passo=int(input("Passo: "))
contador(inicio,fim,passo)
