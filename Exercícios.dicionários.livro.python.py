1 Um usuário do departamento de vendas de uma empresa necessita de um relatório que apresente seus clientes potenciais.
Para isso, é necessário que o relatório seja ordenado do cliente
que mais comprou para o que menos comprou. Os dados de
entrada são razão social e valor total de compras. Considere a
razão social como sendo a chave identificadora do cliente.

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

2. Construa um programa no qual o usuário informe o nome, a
estatura e o peso de vários alunos de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno
ordenados pelo nome do aluno.
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

# OS DICIONÁRIOS ARMAZENAM SEUS DADOS EM {CHAVE: VALOR}. USANDO DUAS VARIAVEIS DENTRO DE UM FOR, E ACESSANDO TODOS OS
#ITENS DO DICIONÁRIO, AO ACESSAR A PRIMEIRE VARIÁVEL, ESTAMOS ACESSANDO AS CHAVES, SE ACESSARMOS SEGUNDA VARIÁVEL, OS VALORES.

print(20 * "-")

for i, a in alunos.items():
    print(f'O IMC do(A) aluno(A) {i} é: {(a[0]/a[1]**2):.2f}')
    
-------------

3. Construa um programa que cadastre diversos voos aéreos,
bem como sua origem e seu destino. Considere o número do
voo como sendo a chave. Com base no que foi armazenado
no dicionário, o programa deve informar a quantidade de voos
cuja origem é Natal. 

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

4. Com base no dicionário da questão anterior, construa um
programa para remover os voos cujo destino é Recife. Em seguida, imprima a nova listagem de voos.

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
5. Ainda com base no dicionário da questão 3, construa um programa em que, após os voos terem sido cadastrados, o usuário
possa modificar a origem e/ou o destino de um determinado
voo. Ao fim, o programa deve imprimir a nova listagem de voos.


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
        print('OBRIGADO E FAÇA UMA BOA VIAGEM!')

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
            print('Obrigado por experimentar meu programa! S2')

else:
    print('Boa viagem!')


















