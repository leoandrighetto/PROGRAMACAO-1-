Uma turma de programação competitiva é composta por somente dezenas de alunos que fizeram uma aposta onde os vencedores de uma prova
serão todos aqueles que tiverem nota final acima da média geral da turma nesta prova. Nem todos os alunos participam da prova. 
Faça um programa para, inicialmente, receber a indicação de quantos alunos (um número inteiro positivo) participam de uma determinada prova, 
registrar cada uma das notas desses alunos participantes, que são valores inteiros não negativos. Por fim, o programa deve verificar e 
mostrar quais dessas notas estão acima da média da turma, conforme os exemplos abaixo.

Entrada: um valor N, inteiro e positivo, que indica quantos alunos participam da prova, seguido de N valores não negativos, que representam as respectivas notas dos alunos.

Saída: uma sequencia de valores inteiros não negativos, um por linha, que representam as notas acima da média entre todas as notas informadas na entrada.

Exemplos de entrada e saída:

Entrada          SAÍDA           Entrada        Saída
4                 4                3              8
2                 5                2              9
3                                  8
4                                  9
5


l=[]
n=int(input('Informe quantos alunos fizeram a prova: '))
for i in range(n):
    l.append(int(input('Informe uma nota: ')))
    
media=sum(l)/len(l)
cont=0
for i in l:
    if i>=media and i!=cont:
        cont+=i
        print(i)


Faça um programa que permita ao usuário informar uma relação de valores. 
O usuário informa uma quantidade indeterminada de valores inteiros positivos 
- até que informe ZERO e com isso encerra a leitura. O ZERO nào faz parte do conjunto. 
Após a constituição da lista, o usuário informa mais um valor inteiro positivo.
O programa verifica quantos dos números da lista são múltiplos desse último valor informado e mostra a quantidade.
Entrada: uma sequência de valores inteiros positivos, até que seja informado ZERO. Mais um valor inteiro e positivo.
Saída: a quantidade existente na lista, de múltiplos do último número lido

l=[]
n=int(input())
while n!=0:
    l.append(n)
    n=int(input())
i=int(input())
cont=0
for p in l:
    if p%i==0:
        cont+=1
print()        
print(cont)

Uma empresa de desenvolvimento de software trabal trabalha somente com uma linguagem de programação criada intemamente. 
O procedimento para selecionar novos desenvolvedores é disponibilizar testes on-line para que 
os candidatos resolvam questões especificamente elaboradas para o processo seletivo. 
O acesso ao sistema de questões fica aberto durante algumas horas. O candidato faz a prova e recebe uma nota. 
Se ele quiser melhorar sua nota, pode realizar novamente a prova quantas vezes desejar. 
No entanto, quando o candidato fizer mais tentativas, a empresa considera como nota final, 
a média entre as notas de todas as tentativas realizadas pelo candidato. 
Desenvolver um programa para calcular e mostrar o resultado do processo seletivo dessa empresa, 
onde o responsável pela seleção digita uma sequencia valores, sendo dois valores por candidato, 
composta pelo número do candidato seguido da respectiva nota alcançada por ele no teste. 
Quando não houver mais notas de candidatos a inserir no sistema, o usuário informa ZERO como o número do candidato, para encerrar a leitura. 
O programa calcula as médias e ao final apresenta a relação dos candidatos com seu respectivo desempenho, conforme os exemplos abaixo:


alunos=[]
notas=[]

aluno=1
while aluno!=0:
    m=[]
    aluno=int(input('aluno: '))
    if aluno==0:
        break
    else:
        if aluno in alunos:
            n=float(input('nota: '))
            notas[alunos.index(aluno)].append(n)
            
        else:    
            alunos.append(aluno)
            n=float(input('nota: '))
            m.append(n)
            notas.append(m)

cont=0
while cont!=len(alunos):
    print(f'{alunos[cont]} {(sum(notas[cont]))/(len(notas[cont])):.1f}')
    cont+=1
