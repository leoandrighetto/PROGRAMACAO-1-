#celulas:

#PASSO A PASSO
# PASSO 0 - ENTENDER A EMPRESA E O DESAFIO DA EMPRESA


# PASSO 1 - IMPORTAR A BASE DE DADOS
import pandas as pd

tabela = pd.read_csv("clientes.csv")

display(tabela)



# PASSO 2 - PREPARAR A BASE DE DADOS PARA A IA 
display(tabela.info())

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
cod_comportamento = LabelEncoder()







   
# PASSO 3 - TREINAR A INTELIGENCIA ARTIFICIAL -> CRIAR O MODELO: NOTA DE CRÉDITO: BOA, OK, RUIM



# PASSO 4 - ESCOLHER QUAL MELHOR MODELO



# PASSO 5 - USAR O MELHOR MODELO PARA FAZER AS PREVISÕES DE NOVOS CLIENTES
