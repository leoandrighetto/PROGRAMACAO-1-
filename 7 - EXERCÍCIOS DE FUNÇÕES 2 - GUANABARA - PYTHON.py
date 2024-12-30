print('EXERCÍCIO 1')


def linha():
  print()
  print(15* '-=')
  print()


# 1 - CRIE UM PROGRAMA QUE RECEBA UMA FUNÇÃO CHAMADA VOTO().
#QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA
# E IRÁ RETORNAR, BASEADO NO ANO, SE ESTA PESSOA É OBRIGADA A VOTAR, OU NÃO, OU SE 
#O VOTO É OPCIONAL.


def voto(ano):
    from datetime import date


    idade = (date.today().year) - ano
    print()
    if idade >= 70 or idade>=16 and idade < 18:
        return f'COM {idade} ANOS O VOTO É OPCIONAL!'

    elif idade >= 18 and idade < 70:
        return f'COM {idade} ANOS O VOTO É OBRIGATÓRIO!'
    else:
        return f'COM {idade} ANOS NÃO VOTA!'

    print()


print(voto(1998))
print(voto(1948))
print(voto(2008))
print(voto(2010))


linha()


print('EXERCÍCIO 2')
print()
# 2 - CRIE UM PROGRAMA COM UMA FUNÇÃO CHAMADA FATORIAL() QUE RECEBA DOIS PARÂMETROS:
# O PRIMEIRO PARÂMETRP É UM NÚMERO INTEIRO, DO QUAL O USUÁRIO QUER CALCULAR O FATORIAL
# E O SEGUNDO É CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO, OPCIONAL, QUE IRÁ MOSTRAR OU NÃO
# O CALCULO DO FATORIAL NA TELA.

def fatorial(n=1,show=False):
    '''
    Calcula o fatorial de um número.
    :para n: número cujo fatorial será mostrado
    :para show: (opcional) Se for True: mostra o cálculo do fatorial. Se for False: somente o fatorial.
    '''


    if show:
        c=n
        while c!=1:
            print(f'{c} X', end=' ')
            c-=1
        print('1 = ', end= ' ')


    fatorial=1
    for i in range(1,n+1,1):
            fatorial *= i
    return fatorial



print(fatorial(5, True))


linha()

#3 - CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA LEIAINT() 
# QUE VAI FUNCIONAR DE FORMA SEMELHANTE AO INPUT() 
#PORÉM APENAS QUANDO LER UM NÚMERO INTEIRO.

def leiaInt(valor):
    while True:
        if valor.isnumeric():
            return valor
        else:
            while True:
                print('ERRO! DIGITE UM NÚMERO INTEIRO!')
                False
                break
        valor = input('Digite um número: ')


n = leiaInt (input('Digite um número: '))
print(f'Você digitou {n}')

