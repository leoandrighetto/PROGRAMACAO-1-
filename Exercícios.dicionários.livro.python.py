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
    nome= input('Nome do aluno: ')
    peso = float(input('Peso do aluno: '))
    altura=float(input('Altura do aluno: '))
    aluno=[]
    aluno.append(peso)
    aluno.append(altura)
    alunos.update({nome: aluno})
    a=input("Adicionar mais alunos (S/N)?   ")
    if a == "N" or a=="n":
        break

print(alunos)
print()
for i, a in alunos.items():
    print(a)
print()

# OS DICIONÁRIOS ARMAZENAM SEUS DADOS EM {CHAVE: VALOR}. USANDO DUAS VARIAVEIS DENTRO DE UM FOR, E ACESSANDO TODOS OS
#ITENS DO DICIONÁRIO, AO ACESSAR A PRIMEIRE VARIÁVEL, ESTAMOS ACESSANDO AS CHAVES, SE ACESSARMOS SEGUNDA VARIÁVEL, OS VALORES.

print(20 * "-")

for i, a in alunos.items():
    print(f'O IMC DO(A) ALUNO(A) {i} É: {(a[0]/a[1]**2):.2f}')
-------------

3. Construa um programa que cadastre diversos voos aéreos,
bem como sua origem e seu destino. Considere o número do
voo como sendo a chave. Com base no que foi armazenado
no dicionário, o programa deve informar a quantidade de voos
cuja origem é Natal. 




























