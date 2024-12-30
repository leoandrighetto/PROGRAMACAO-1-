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

linha()

# 4 - CRIE UM PROGRAMA QUE RECEBA UMA FUNÇÃO CHAMADA FICHA QUE RECEBA DOIS PARÂMETROS OPCIONAIS:
# O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU
# O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE AS INFORMAÇÕES NÃO
# TENHAM SIDO ESCREITAS CORRETAMENTE.

def ficha(nome='<desconhecido>', gols=0):
    print (f'O jogador {nome} fez {gols} gol(s).')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g=int(g)
else:
    g=0

if n.strip()=='':

    ficha(gols=g)
else:

    ficha(n,g)

linha()

# 5- FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS()
# QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS
# E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:

# -QUANTIDADE DE NOTAS
# -A MAIOR NOTA
# -A MENOR NOTA
# -A MÉDIA DA TURMA
# -A SITUAÇÃO (OPCIONAL)

 # ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO.

def notas(* notas, situação = False):

    qua=len(notas)
    maior = max(notas)
    menor = min(notas)
    media = round(sum(notas)/len(notas), 2)
    
    dic = {'Quantidade de notas': qua,
         'Maior Nota': maior,
         'Menor nota': menor,
         'Média da turma': media}
    
    if situação:

        if media > 7:
            dic.update ({'Situação': 'Boa'})
            return dic
        elif media >= 5 and media < 7:
            dic.update ({'Situação': 'regular'})
            return dic
        else:
            dic.update ({'Situação': 'Péssima'})
            return dic
    else:
        return dic


print(notas(5.5, 9.5, 18, 6.5))
print()
print(notas(5.5, 9.5, 18, 6.5, situação = True))



