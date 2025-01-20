 # CLASES# CLASES# CLASES# CLASES# CLASES# CLASES# CLASES# CLASES# CLASES

#  EXER 1
class Ingresso():
    def __init__(self,nome_do_evento,valor_ingresso):
        self.nome_do_evento = nome_do_evento 
        self.valor_ingresso = valor_ingresso

    def exibirValor(self):
        return f"Valor do Ingresso: {self.valor_ingresso}"
    
    def __str__(self):

        return f'Evento: {self.nome_do_evento} | Valor do Ingresso: {self.valor_ingresso}'
    
# EXER 2.

class Retangulo():

    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    
    def calcularPerimetro(self):
        perimetro = (self.largura*2) + (self.altura*2) 
        return f'O perímetro do retêngulo de {self.largura}m por {self.altura}m é {perimetro}m'

    def calcularArea(self):
        area = self.altura * self.largura
        return f'A área do retângulo é {area} m².'

# EXER 3.

class Ponto():

    def __init__(self,nome,x,y):
        self.nome = str(nome)
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'{self.nome}: ({self.x}, {self.y})'


 # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO

from exercicios import Ingresso,Retangulo,Ponto

# #EXERCÍCIO 1
# Crie uma classe chamada Ingresso, que possua o nome do
# evento e o valor do ingresso. Crie o método exibirValor(),
# que apenas retorne o valor do ingresso. Crie o método __str__
# que retorne o nome do evento seguido do valor do ingresso.
# Crie um programa para testar sua classe.

evento = Ingresso('Show dos Beatles', "500.00")

print (evento)
print(Ingresso.exibirValor(evento))


# #EXERCÍCIO 2
# 2. Crie uma classe chamada Retangulo, a qual possua os atributos 
#largura e altura, e os métodos calcularPerimetro() e
# calcularArea(). No código de teste, crie um objeto e calcule,
# respectivamente, o perímetro e a área desse retângulo.

medida = Retangulo(45,10)

print(Retangulo.calcularArea(medida))

print(Retangulo.calcularPerimetro(medida))


# #EXERCÍCIO 3

# 3. Crie uma classe Ponto, conforme a figura a seguir. 
# O método __str__ deve retornar os atributos do objeto no formato
# “nome: (x, y)”. Crie em outro arquivo os testes para a classe
# Ponto, lendo diversos pontos e criando um objeto ponto para
# cada entrada lida. Coloque cada objeto da classe Ponto em
# uma lista e, ao final, imprima cada elemento dessa lista.

pontos = [Ponto("Coordenadas_1", 15, 44),
          Ponto("Coordenadas_2", 35, 13),
          Ponto("Coordenadas_3", 55, 69),
          Ponto("Coordenadas_4", 10, 64)]

print(pontos[0])
print(pontos[1])
print(pontos[2])
print(pontos[3])

