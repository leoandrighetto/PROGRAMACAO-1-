def linha():
    print()
    print(15* '--')
    print()

'''
# RESUMO DE FUNÇÕES:

# PARA DECLARAR UMA FUNÇÃO:

# def "função(Parâmetros)"   # def = definir
#     Comandos
#     retorno
'''

linha()

'''
# PARA EXECUTAR UMA FUNÇÃO:

# função(parâmetros)
# função() Sem parâmetros
'''

linha()


#FUNÇÃO COM PARÂMETROS:

def multiplicação(a,b,c):

    """
    Multiplica 3 números e estes devem sempre receber um valor inteiro:
    
    :para a: Número inteiro
    :para b: Número inteiro
    :para c: Número inteiro
    :m: Variável de atribuição
    """

    m = a * b * c

    print(f' O resultado da multiplicação entre os números é {m}!')


multiplicação(2,2,2)      #EXECUTA A FUNÇÃO

#SAÍDA

# O resultado da multiplicação entre os números é 6.


linha()


#PARÂMETROS OPCIONAIS:

def soma(a,b,c=0):

    """
    Soma 3 valores, sendo o último opcional.
    """

    s=a+b+c
    print(f'A soma é {s}.')

soma(4,2)   #Não foi digitado um valor para C, mas ele já possui o valor de 0 atribuídoà ele.

# Saída:

# A soma é 6.

linha()

'''
#ESCOPO DE --VARIÁVEIS--

#ESCOPO DE VARIÁVEIS REPRESENTA O LOCAL ONDE UMA VARIÁVEl PODE SER ACESSADA:

#------------------------------------
def função():
    a = 1                           # VARIÁVEL  a  ESTÁ EM UM ESCOPO "LOCAL". 
    print(f'a local vale {a}')

#------------------------------------
#programa principal

função()    #EXECUTA A FUNÇÃO/   SAÍDA: 1

#--------
a = 2                                               #VARIÁVEL a ESTÁ EM UM ESCOPO GLOBAL, DENTRO DO PROGRAMA PRINCIPAL
print(f'a global vale {a}')    #SAÍDA: 2
#--------                                   

linha()

# PARA USAR UMA VARIÁVEL GLOBAL COMO LOCAL:
'''


def somaDeB(b):# --------- B VALE 2, POIS O COMANDO GLOBAL SÓ FUNCIONA APÓS SER CHAMADO. NO SEU PRINT CORRESPONDENTE ELE (a) SERÁ SOMADO COM 4. SAÍDA = 6
    global a
    a=8                          # USANDO O COMANDO GLOBAL SOBRE a, NO PRINT CORRESPONDENTE,
    b+=4
    c=3
    print(f' a local vale {a}')
    print(f' b local vale {b}')
    print(f' c local vale {c}')


a = 2 
somaDeB(a)      #A  VALE  2
print(f'a global vale {a}')

#USANDO O COMANDO GLOBAL SOBRE UMA VARIÁVEL, DENTRO DE UM LOCAL, A VARIÁVEL GLOBAL PASSA A VALER O VALOR DA VARIÁVEL LOCAL. 

#EXEMPLO SEM O COMANDO GLOBAL
linha()

def somadeC (c):

    a=8
    c+=4
    d=3
    print(f'a local é {a}')
    print(f'c local é {c}')
    print(f'd local é {d}')

a = 2
somadeC (a)
print(f'a global é {a}')

linha()


'''
 IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE IMPORTANTE

 
FUNÇÃO RETURN:

SÃO ÚTEIS PARA A PERSONALIZAÇÃO DOS RESULTADOS:

'''
#EXEMPLOS:

def exemplo(a,b):
    soma=a+b
    mul=a*b
    div=a/b
    return soma,mul,div

r1=exemplo(10,2)
r2=exemplo(9,8)
r3=exemplo(5,4)

print(f'A soma, multiplicação e divisão usando os números 10 e 2 são {r1}')
print()
print(f'A soma, multiplicação e divisão usando os números 9 e 8 são {r2}')
print()
print(f'A soma, multiplicação e divisão usando os números 5 e 4 são {r3}')

'''
#SAÍDA:

A soma, multiplicação e divisão usando os números 10 e 2 são (12, 20, 5.0)

A soma, multiplicação e divisão usando os números 9 e 8 são (17, 72, 1.125)

A soma, multiplicação e divisão usando os números 5 e 4 são (9, 20, 1.25)

'''

linha()

# 3 - FAÇA UM PROGRAMA QUE RECEBA UMA FUNÇÃO CHAMADA FICHA(),
# QUE RECEBA DOIS PARÂMETROS OPCIONAIS. O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU

# O PROGRAMA DEVE MOSTRAR A FICHA DO JOGADOR MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.

def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# AS DUAS VARIÁVEIS ESTÃO COMO STRINGS, PARA SÓ DEPOIS VERIFICAR SE GOLS POSSUI VALOR NUMÉRICO.
n=str(input('Nome do jogador: '))
g=str(input('Quantidade de gols: '))


if g.isnumeric():   #VERIFICA SE O VALOR DE g É NUMÉRICO.
        g = int(g)  #SE SIM, g RECEBE O MESMO VALOR DIGITADO E PASSA A SER UM INT.
else:
    g = 0           #SENÃO, PASSA A SER 0


# NOVIDADE:
# É POSSÍVEL SELECIONAR QUANDO A FUNÇÃO SERÁ EXECUTADA:

if n.strip() == '':     #SE O VALOR DE N ESTIVER VAZIO (MESMO ESTANDO COM ESPAÇOS - .STRIP()) 
     ficha(gols=g)      #APENAS O PARÂMETRO GOLS MOSTRARÁ SEU VALOR.
else:
     ficha(n, g)        #SENÃO, É MOSTRADO OS DOIS VALORES COMO FORAM ATRIBUÍDOS.
