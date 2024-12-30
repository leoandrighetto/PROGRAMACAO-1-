'''
1 Um usuário do departamento de vendas de uma empresa necessita de um relatório que apresente seus clientes potenciais.
Para isso, é necessário que o relatório seja ordenado do cliente
que mais comprou para o que menos comprou. Os dados de
entrada são razão social e valor total de compras. Considere a
razão social como sendo a chave identificadora do cliente.
'''
-----------------------------

from operator import itemgetter

Vendas = {}
Vendas ["Coca-cola"]=80
Vendas ["Multisom"]=6
Vendas ["Lacoste"]=555
Vendas ["A.G.N.C. Guarda Negra"]=10
print("Empresas:")
print()
for i in Vendas:
    print(i)
print()
print("Vendas em ordem decrescente:")
print()
cont=1
for i, a in sorted(Vendas.items(), key=itemgetter(1),reverse=True):
    print(f'{cont}ª = {i} - {a}')
    cont+=1

------------------------------

'''
2. Construa um programa no qual o usuário informe o nome, a
estatura e o peso de vários alunos de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno
ordenados pelo nome do aluno.
'''

------------

alunos={}

while True:
    aluno=[]
    nome = input('Nome do aluno: ')
    aluno.append(float(input('Peso do aluno: ')))
    aluno.append(float(input('Altura do aluno: ')))

    alunos.update({nome: aluno})

    add=input("Adicionar mais alunos (S/N)?   ")
    if add == "N" or add=="n":
        break
'''
OS DICIONÁRIOS ARMAZENAM SEUS DADOS EM {CHAVE: VALOR}. USANDO DUAS VARIAVEIS DENTRO DE UM FOR, E ACESSANDO TODOS OS
ITENS DO DICIONÁRIO, AO ACESSAR A PRIMEIRE VARIÁVEL, ESTAMOS ACESSANDO AS CHAVES, SE ACESSARMOS SEGUNDA VARIÁVEL, OS VALORES.
'''

print(20 * "-")

for i, a in alunos.items():
    print(f'O IMC do(A) aluno(A) {i} é: {(a[0]/a[1]**2):.2f}')
    
-------------

'''
3. Construa um programa que cadastre diversos voos aéreos,
bem como sua origem e seu destino. Considere o número do
voo como sendo a chave. Com base no que foi armazenado
no dicionário, o programa deve informar a quantidade de voos
cuja origem é Natal. 
'''

voos = {}
cont=0
while True:
    n=int(input('Número de voo: '))
    o=input('Origem: ')
    if o=="Natal" or o=="natal":
        cont+=1
    d=input('Destino: ')
    voos.update({n:[o,d]})
    add=input('Deseja registrar outro voo (S/N)?   ')
    if add=="n" or add=="N":
        break

print(f'{cont} voos tem como origem Natal')

--------------

'''
4. Com base no dicionário da questão anterior, construa um
programa para remover os voos cujo destino é Recife. Em seguida, imprima a nova listagem de voos.
'''

voo={}

while True:
    p = []
    n=int(input('n: '))
    p.append(input('o: '))
    p.append(input('d: '))
    voo.update({n: p})
    add= input('Add mais um voo (S/N):  ')
    if add.lower() == 'n':
        break
        
remover=[]
for i,a in voo.items():
    if a[1].lower() == 'recife':
        remover.append(i)
        
for i in remover:
    voo.pop(i)
    
print(voo)


-------------

'''
5. Ainda com base no dicionário da questão 3, construa um programa em que, após os voos terem sido cadastrados, o usuário
possa modificar a origem e/ou o destino de um determinado
voo. Ao fim, o programa deve imprimir a nova listagem de voos.
'''

voos={}

while True:
    n=input('Número do voo: ')
    l=[]
    l.append(input('Origem: '))
    l.append(input('Destino: '))
    voos.update({n: l})

    print()
    print(20 * '-')
    per=input('Deseja adicionar mais voos (S/N)?   ')
    print()
    print(20 * '-')

    if per.lower() =='n':
        print('Obrigado por experimentar meu programa! S2')
        break

print()
print(20 * '-')
print()

for i, a in voos.items(): 
    print(f'O voo n° {i} tem como origem {a[0]} e destino {a[1]}')

print()
op= input('Deseja alterar a origem ou destino de algum voo (S/N)?  ')
print()

if op.lower() == "s":

    for i, a in voos.items():
        print(f"{i} --- {a}")
    print()
    op1=(input('Digite o número de voo que você gostaria de alterar ou digite "N" para sair: '))
    

    if op1.lower() == "n":
        print()
        print('Obrigado por experimentar meu programa! S2')

    else:
        print()
        op2=input('Você gostaria de alterar a ORIGEM, DESTINO ou sair do programa ("N")?  ')
        if op2.lower() == "origem":
            print()
            op3=input('Qual a nova origem? ')

            voos [op1][0] = op3

            for i, a in voos.items():
                print(f'Voo: {i}, tem origem: {a[0]} e Destino: {a[1]}')
                print()
            print()
            print('Alterado!! Boa viagem')

        elif op2.lower()=="destino:":
            op4=input('Qual o novo destino? ')
            voos [op1][1] = op4
            for i, a in voos.items():
                    print(f'Voo: {i}, tem origem: {a[0]} e Destino: {a[1]}')
                print()
            print()
            print('Alterado!!Boa viagem')
        else:
            while True:
                print('Por favor, digite uma opção Válida:')
                op2=input('Você gostaria de alterar a ORIGEM, DESTINO ou sair do programa ("N")?  ')
                if op2.lower() in ['s', 'n']:
                    break
            
else:
    print('Obrigado por experimentar meu programa! S2')

'''
6. Crie um programa para uma nova plataforma de vídeo sob
demanda o qual deve armazenar o título da série e o nome
dos 2 principais atores. Ao final, o programa deve exibir uma
listagem contendo, de forma ordenada, o nome da série e os
nomes dos atores.
'''
ssvid = {}

nome=input('Nome da Série: ')
p1=input('Ator principal: ')
p2=input('Ator secundário: ')
ssvid.update({nome: [p1,p2]})

while True:
    print()
    per = input('Deseja adicionar mais dados (S/N)? ')

    if per.lower()=='s':
        print()
        nome = input('Nome da Série: ')
        p1 = input('Ator principal: ')
        p2 = input('Ator secundário: ')
        ssvid.update({nome: [p1, p2]})

    elif per.lower()=='n':
        print()
        print('Obrigado por usar este programa!')
        break

    else:
        print()
        print('Digite uma opção válida!')

for i, a in sorted(ssvid.items()):
    print(10*"~")
    print(f'Série: {i}')
    print(f'Ator principal: {a[0]}')
    print(f'Ator Coadjuvante: {a[1]}')
    print(10*"~")

'''
7. Modifique o programa anterior de modo que o usuário informe o nome de uma série e o novo programa indique os nomes
dos atores principais. Caso a série não esteja cadastrada, o programa deve informar isso ao usuário.
'''

series= {}

#NOSSO DICIONÁRIO POSSUI APENAS UMA SÉRIE CADASTRADA NESTE EXEMPLO:
series.update({'dois homens e meio': ['Charlie Sheen', 'Jon Cryer']})

while True:

    n = input('Digite o nome da série em letras minúsculas: ')

    if n.isupper():
        print('Você digitou o nome da série com letras maiúsculas')
        continue

    if n in series:
        print(f'Atores principais: {series[n]}')
        break

    else:
        print('não há séries com este nome')
        break

'''
8. Construa um programa que utilize um dicionário para representar a tabela abaixo.

Código              Nome                    Valor (R$)
1                   Monitor LED 24”         599,99
2                   Teclado wireless        59,26
3                   Mouse wireless          19,90
4                   Cartucho colorido       54,00

O programa deve aplicar um desconto de 10% sobre os produtos com o valor acima de R$ 50,00 e acrescentar à descrição a
string (em promoção).
'''

produtos = {}

produtos.update({'1': ['Monitor LED 24', 599.99]})
produtos.update({'2': ['Teclado Wireless', 59.26]})
produtos.update({'3': ['Mouse Wireless', 19.90]})
produtos.update({'4': ['Cartucho Colorido', 54.00]})

for i,a in produtos.items():
    if a[1] >50:
        a[0]+=" (em promoção)"

for i in produtos.items():
    print(i)

'''
9. Crie um dicionário para armazenar os dados da tabela anterior (de funcionarios). 
Em seguida, o programa deve imprimir uma listagem de
mulheres do setor de TI que recebem acima de R$ 3.000,00.
'''

funcionarios = {'1': ['Ana', 'f', 'ti',7,3200],
'2': ['Beatriz', 'f','ti',4, 3720],
'3': ['Carla','f','ti',2, 3920],
'4': ['Daniela','f','rh',2, 2100],
'5': ['Emilio', 'm','rh',7, 4235.12],
'6': ['Fernando', 'm','marketing',7, 1200],
'7': ['Gabriela', 'f','marketing',8,7234.89],
'8': ['Hernandes', 'm','ti','marketing',6,4234.12],
'9': ['Ítalo', 'm','rh',13,13934.23],
'10': ['Janaína', 'f','rh',7,9341.89]}


for i,a in funcionarios.items():
    if a[1] == "f" and a[2]=='ti' and a[4] > 3000:
        print(i, a)
'''
10. Modifique a questão anterior para listar os homens que
não são do setor de TI.
'''

for i,a in funcionarios.items():
    if a[1] == "m" and a[2]!='ti':
        print(i, a)












