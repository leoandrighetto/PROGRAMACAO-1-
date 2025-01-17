#celulas:

#PASSO A PASSO
# PASSO 0 - ENTENDER A EMPRESA E O DESAFIO DA EMPRESA


# PASSO 1 - IMPORTAR A BASE DE DADOS
import pandas as pd

tabela = pd.read_csv("clientes.csv")

display(tabela)



# PASSO 2 - PREPARAR A BASE DE DADOS PARA A IA 
# display(tabela.info())

# int (inteiros)
# float (decimais)
# object (texto)

# !!IAs NÃO CONSEGUEM APRENDER SOBRE A BASE DE DADOS COM COLUNAS DE TEXTO!!!
# VAMOS INICIAR O PROCESSO DE LABELENCODER (DOCIFICAR OS RÓTULOS): TRANSFORMAR
# AS INFORMAÇÕES DAS COLUNAS DE TEXTO EM NÚMEROS:

# profissao
# mix_credito
# comportamento_pagamento

# LINHA DE CÓDIGO RETIRADA DA BIBLIOTECA SCIKIT-LEARN:

from sklearn.preprocessing import LabelEncoder

# EXECUTANDO O PROCESSO DE LABELENCODER:

cod_profissao = LabelEncoder()
tabela['profissao'] = cod_profissao.fit_transform(tabela['profissao'])
#novovalortabela    = antigovalor    transformado no  codificador



cod_credito = LabelEncoder()
tabela['mix_credito'] = cod_credito.fit_transform(tabela['mix_credito'])

cod_comportamento = LabelEncoder()
tabela['comportamento_pagamento'] = cod_comportamento.fit_transform(tabela['comportamento_pagamento'])

display(tabela.info())


#PASSO 2.1
#  DIVIDIR A DATABASE EM DUAS PARTES. 
# y SENDO A COLUNA QUE QUEREMOS PREVER. (score)
y = tabela['score_credito']


# x SENDO AS COLUNAS DA DATABASE QUE USAREMOS PARA FAZER A PREVISÃO
x = tabela.drop(columns = ['score_credito','id_cliente'])

# DEVEMOS TREINAR NOSSA INTELIGÊNCIA ARTIFICIAL, PORTANTO
# SEPARAMOS NOSSOS DADOS EM DADOS DE TREINO E DADOS DE TESTE:

from sklearn.model_selection import train_test_split
# SEPARA DA BASE OS DADOS DE TREINO E DE TESTE

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

# A ORDEM SERÁ SEMPRE ESTA. ELA FOI DEFINIDA PELOS CRIADORES DA FUNÇÃO


   
# PASSO 3 - TREINAR A INTELIGENCIA ARTIFICIAL -> CRIAR O MODELO: NOTA DE CRÉDITO: BOA, OK, R

# PASSOS PARA CRIAR A IA:

# PASSO 1 - IMPORTAR A IA

# VAMOS IMPORTAR DOIS MODELOS DIFERENTES QUE APRENDEM DE MANEIRAS DIFERENTES E TESTAR CADA UMA DELAS.
# 1º MODELO: ÁRVORE DE DECISÃO (RANDOMFOREST)
# 2º MODELO: VIZINHOS PRÓXIMOS (NEIREST NEIGHBORS)

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier




# PASSO 2 - CRAIR A IA

modelo_arvoradecisao = RandomForestClassifier()
modelo_knn = RandomForestClassifier()




# PASSO 3 - TREINAR A IA


modelo_arvoradecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)



# PASSO 4 - TESTAR OS MODELOS E ESCOLHER QUAL É O MELHOR MODELO

previsao_arvore_decisao = modelo_arvoradecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

# para saber como comparar os modelos, calculamos a acurácia( precisão ) de ambos.

from sklearn.metrics import accuracy_score

display(accuracy_score(y_teste, previsao_arvore_decisao))
display(accuracy_score(y_teste, previsao_knn))



# # PASSO 5 - USAR O MELHOR MODELO PARA FAZER AS PREVISÕES DE NOVOS CLIENTES

# # MELHOR MODELO É O MODELO ARVORE DE DECISAO


# #IMPORTAR OS NOVOS CLIENTES 

# tabela_novosclientes = pd.read_csv('novos_clientes.csv')
