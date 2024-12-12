#FORMAS DE DECLARAR DICIONÁRIOS:
                #111111111

leonardo={
    "Nome": "Leonardo Andrighetto Linhares" ,
    "Telefone": "555-(51) 99387-7613",
    "Endereço": "Acesso Bonar Figueiro 2537 Restinga Porto Alegre"}
print(f'Dicionario1:{leonardo}')
print()

                #222222222
leonardo2 = {}
leonardo2["Nome"]="Leonardo Andrighetto Linhares"
leonardo2["Telefone"]="993877613"
leonardo2["Endereço"]="Rua Tal"

print(f'Dicionario2: {leonardo2}')
print()



#CONSULTAS USANDO " .get()  "


#               ---
print(f'Nome antes de Alterar com update: {leonardo2.get("Nome")}')
#    (dicionario.get('chave'))
print()




#PARA ADICIONAR OU ALTERAR CHAVES USANDO    "  update()  "

leonardo.update({"Nome": "Leleo"})

print(f'Depois: {leonardo.get("Nome")}')
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
print("ORDENANDO ELEMENTOS usando SORTED")
for i, a in sorted(leonardo.items()):
    print(f'{i} ---- {a}')
