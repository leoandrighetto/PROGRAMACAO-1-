Um usuário do departamento de vendas de uma empresa necessita de um relatório que apresente seus clientes potenciais.
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
























