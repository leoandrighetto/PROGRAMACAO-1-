# PARA CRIAR UM PACOTE OU UTILIZAR MÓDULOS EM PYTHON NO VS CODE:

# CRIE UM DIRETÓRIO NESTE MODELO:

# PASTA_MODULARIZACAO/
# │
# ├── PASTA_PACOTES/

#   │   ├── __init__.py                # Arquivo vazio para indicar que a pasta contém módulos personalizados.

#   │   ├── PASTA_MODULO_1/            # Primeira pasta de módulo

# │   │   ├── __init__.py            # Arquivo vazio para marcar este diretório como um módulo.
# │   │   ├── mat.py                 # Arquivo Python com as funções matemáticas (exemplo: soma, subtração, etc.).
# │   │   └── funcoes.py             # Outro arquivo Python com funções auxiliares (opcional).

#   │   ├── PASTA_MODULO_2/            # Segunda pasta de módulo

# │   │   ├── __init__.py            # Arquivo vazio para marcar este diretório como um módulo.
# │   │   └── funcoes.py             # Arquivo Python com funções auxiliares (exemplo: operações com strings).

#   │   ├── PASTA_MODULO_3/            # Terceira pasta de módulo

# │   │   ├── __init__.py            # Arquivo vazio para marcar este diretório como um módulo.
# │   │   └── outras_funcoes.py      # Arquivo Python com outras funções (exemplo: manipulação de listas).

#   │   └── PASTA_MODULO_4/            # Quarta pasta de módulo

# │       ├── __init__.py            # Arquivo vazio para marcar este diretório como um módulo.
# │       └── utilitarios.py         # Arquivo Python com funções utilitárias (exemplo: funções de entrada e saída).
# │
# └── arquivo_onde_eu_importo.py     # Arquivo onde as importações dos módulos são feitas.



#EXEMPLO:

# PASTA_PACOTES\PASTA_MÓDULO_1\mat.py <-um arquivo que criei para implementar minhas funções matemáticas.

# O ARQUIVO -> mat.py:

def soma (a,b):
  c = a + b
  print (f" A soma entre {a} + {b} é {c}.")




#COMO IMPORTAR DE DENTRO DO ARQUIVO ONDE ESTOU IMPLEMENTANDO MEU PROJETO->  arquivo_onde_eu_importo:



from PASTA_PACOTES._PASTA_MÓDULO_1 import mat
#IMPORTAÇÃO PRECISA.


mat.soma(4,5)
#FORMA SIMPLES DE UTILIZAR A FUNÇÃO

#SAÍDA:
    # A soma entre 4 + 5 é 9.





#RESUMO:

# para criar um diretório válido, a pasta com os arquivos python usados para a importação devem conter um arquivo vazio chamado __init__.py .

# pode-se importar dados de qualquer diretório, desde que o arquivo do projeto em si esteja dentro da pasta alfa.

# para importar um arquivo de um módulo espcífico deve-se seguir estas regras: (OS PONTOS SÃO JUNTO AOS COMANDOS)


# 1 - IMPORTANDO O ARQUIVO DA BIBLIOTECA DE FORMA ESPECÍFICA:
  
        # from pasta_pacote . pasta_modulo     import    arquivo_com_as_funcoes

                    #UTILIZANDO A FUNÇÃO DE DENTRO DO ARQUIVO:
                    arquivo_com_as_funcoes . funcao()



# 2 - IMPORTANTO APENAS A BIBLIOTECA INTEIRA:

        #import pasta_pacote . pasta_modulo . arquivo . arquivo_com_as_funcoes

                     #UTILIZANDO A FUNÇÃO DE DENTRO DO ARQUIVO, QUE ESTÁ DENTRO DA PASTA_MODULO, QUE ETC...:
                    pasta_pacote . pasta_modulo . arquivo . arquivo_com_as_funcoes . funcao()



# A IMPORTAÇÃO ESPECÍFICA É MAIS PRÁTICA E ÚTIL NA HORA DA IMPLEMENTAÇÃO.






