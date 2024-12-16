#FORMAS DE DECLARAR DICIONÁRIOS:
                #111111111

leonardo={
    "Nome": "Leonardo Andrighetto Linhares" ,
    "Telefone": "555-(51) 99387-7613",
    "Endereço": "Acesso Bonar Figueiro 2537 Restinga Porto Alegre"}
print(f'Dicionario1 (Leonardo):{leonardo}')
print('------------')

                #222222222
leonardo2 = {}
leonardo2["Nome"]="Leonardo Andrighetto Linhares"
leonardo2["Telefone"]="993877613"
leonardo2["Endereço"]="Rua Tal"

print(f'Dicionario2 (Leonardo2): {leonardo2}')
print('------------')



#CONSULTAS USANDO " .get()  "

#
print(f'Comando -> "leonardo.get("Nome")" -> : {leonardo.get("Nome")}')
#
print('------------')

#PARA ADICIONAR OU ALTERAR CHAVES USANDO    "  update()  "

#               ---
print(f'Nome antes de Alterar com update: {leonardo2.get("Nome")}')
#    (dicionario.get('chave'))
print('------------')


leonardo.update({"Nome": "Leleo"})

print(f'Depois de mudar Nome usando Update (Leonardo.update) -> : {leonardo.get("Nome")}')
print('------------')
                                #adicionando uma nova chave:
leonardo.update({"Nome da Mãe": 'Ivete Andrighetto'})

print(f'Após nova chave: {leonardo}')
print('------------')


#FUNÇÃO LEN:

print(f'Contando quantas chaves o dicionario possui usando len: --{len(leonardo)}--')
print('------------')

#VERIFICANDO A EXISTÊNCIA DE UMA CHAVE:

if "Nome" in leonardo:
    print(f'VERIFICANDO A EXISTÊNCIA DE UMA CHAVE: {leonardo.get("Nome")}')
    
print('------------')
from operator import itemgetter

#PARA OBTER AS CHAVES DE UM DICIONARIO (EM LISTA):
print('Para obter as CHAVES de um dicionario:')
for a in leonardo.keys():
        print(a)
        
print('------------')


#PARA OBTER TODOS OS VALORES DE UM DICIONARIO (EM LISTA):
print('Para obter os VALORES de um dicionario:')


for a in leonardo.values():
    print(a)

print('------------')



#PARA OBTER TODOS OS ITENS DE UM DICIONARIO (EM LISTA):
print('Para obter TODOS OS ITENS de um dicionario:')

for a in leonardo.items():
    print(a)

print('------------')

#ORDENANDO ELEMENTOS usando SORTED:
print('------------')
print("ORDENANDO ELEMENTOS usando SORTED")
for i in sorted(leonardo):
    print(i)

print('------------')

print("ORDENANDO ELEMENTOS usando SORTED com valores em ordem crescente")
print("---")
compras={}
compras["Cliente 1"]=10
compras["Cliente 2"]=50
compras["Cliente 3"]=30
compras["Cliente 4"]=20

print("for i in sorted(compras.values(), reverse=True)")
print("print(i)")

for i in sorted(compras.values(),reverse=True):
    print(i)
    
print('------------')

print("ORDENANDO ELEMENTOS baseado nos valores: itemgetter()")
print('------------')
print("Compras dos clientes em ordem decrescente:")
for i, a in sorted(compras.items(), key=itemgetter(1), reverse=True):
    print(f'{i}--{a}')


print('------------')

print("ORDENANDO ELEMENTOS usando SORTED 'chave(i)' e valor(a)'")
for i, a in sorted(compras.items()):
    print(f'{i} ---- {a}')

print('------------')

#CLONANDO UM DICIONARIO:

copia= dict(leonardo)
print(f"clonando o dicionario leonardo, atribuindo a variarel copia: print(copia) -> {copia}")

print('------------')


#REMOVENDO ELEMENTOS USANDO POP:
leonardo.pop("Nome")
leonardo.pop("Telefone")
print(f'removendo elementos usando o comando -> leonardo.pop("Nome") e telefone em outra linha.: {leonardo}')

print('------------')
