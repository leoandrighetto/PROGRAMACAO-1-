#111111111111111111111111111111111

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

#222222222222222222222222222222222

