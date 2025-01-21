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

linha()


# # EXERC 4:

# # Crie uma classe Lista¹ que receba um atributo do tipo list
# # e que tenha um método o qual retorne os elementos da lista
# # sem repetição. Crie o programa de teste.

class Lista():

    def __init__(self):
        self.itens = []

    def ele_sem_duplicatas(self,itens):
        self.itens = itens
        return list(set(self.itens))
    

#3 EXER 5:

# 5. Implemente uma calculadora que receba dois operadores
# utilizando os conceitos de orientação a objetos aprendidos. Os
# atributos op1 e op2 (operadores) são iniciados no construtor e os
# métodos somar(), subtrair(), multiplicar(), dividir()
# e calcularPotencia() realizam as respectivas ações nesses
# atributos. Crie o programa de teste para a classe Calculadora.

class Calculadora():
    def __init__(self,op1,op2):
        self.op1 = op1
        self.op2 = op2

    def somar(self):
        soma = self.op1 + self.op2
        return soma
    
    def subtrair(self):
        sub = self.op1 - self.op2
        return sub

    def multiplicar(self):
        mul = self.op1 * self.op2
        return mul
    
    def dividir(self):
        div = self.op1 / self.op2
        return div


    def calcularPotencia(self):
        pot = self.op1**(self.op2)
        return pot


# # EXER 6:
# 6. Crie a classe Funcionario com os atributos nome e
# salario, recebidos pelo método construtor, e o método
# aumentarSalario(porcentagem) cujo parâmetro é a porcentagem de aumento. 
# Implemente um programa de teste
# para a classe, criando dois funcionários e simulando o aumento de 
# salário de 20% para um e 50% para o outro.

class Funcionario():
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self,porcentagem):
        self.porcentagem = porcentagem
        reajuste = (self.salario*self.porcentagem)/100
        total = self.salario + reajuste
        return total
    
# 7. Implemente uma classe Carro, que tenha as propriedades
# consumo e combustível refletindo o consumo do carro em
# km/l e o combustível no tanque, respectivamente. O consumo
# é atribuído no método construtor, enquanto o combustível
# inicia com 0. Crie o método andar() para simular o ato de
# dirigir o veículo por uma certa distância (isso vai reduzir a
# quantidade de combustível no tanque). Crie um método
# exibirCombustivel(), que mostrará o nível atual em
# que o carro se encontra e o método abastecer(litros)
# para aumentar o nível de combustível do carro. Agora, crie o
# programa de teste e simule o passeio de um veículo.

class Carro():

    def __init__(self,consumo):

        self.consumo = consumo
        self.combustivel = 0
        self.distancia = 0
 
    def andar(self,distancia):
        self.distancia = distancia
        return distancia
    
    def abastecer(self,litros):
        self.litros = litros

        self.combustivel += litros

        return litros

    def exibirCombustivel(self):

        nivel = self.litros

        if self.distancia > 0:
            return nivel - (self.distancia / self.consumo)
        elif self.consumo > 0:
            return nivel
        else:
            return nivel
        
# IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO # IMPORTAÇÃO

from p_classes.classes import Ingresso,Retangulo,Ponto,Lista

def linha():
    print('---')
    print('---')
    print('---')

# #EXERCÍCIO 1
# Crie uma classe chamada Ingresso, que possua o nome do
# evento e o valor do ingresso. Crie o método exibirValor(),
# que apenas retorne o valor do ingresso. Crie o método __str__
# que retorne o nome do evento seguido do valor do ingresso.
# Crie um programa para testar sua classe.

evento = Ingresso('Show dos Beatles', "500.00")

print (evento)
print (Ingresso.exibirValor(evento))

linha()

# #EXERCÍCIO 2
# 2. Crie uma classe chamada Retangulo, a qual possua os atributos 
#largura e altura, e os métodos calcularPerimetro() e
# calcularArea(). No código de teste, crie um objeto e calcule,
# respectivamente, o perímetro e a área desse retângulo.

medida = Retangulo(45,10)

print(Retangulo.calcularArea(medida))

print(Retangulo.calcularPerimetro(medida))

linha()

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

linha()

# EXERCICIO 4 (IMPORTANTE DE CONFERIR)
# Crie uma classe Lista¹ que receba um atributo do tipo list
# e que tenha um método o qual retorne os elementos da lista
# sem repetição. Crie o programa de teste.

nova_lista = Lista([12,43,45,45,67,67,11,00,1,34]).El_Ordenados()                                                 

print(nova_lista)

linha()

# #3 EXER 5:

# # 5. Implemente uma calculadora que receba dois operadores
# # utilizando os conceitos de orientação a objetos aprendidos. Os
# # atributos op1 e op2 (operadores) são iniciados no construtor e os
# # métodos somar(), subtrair(), multiplicar(), dividir()
# # e calcularPotencia() realizam as respectivas ações nesses
# # atributos. Crie o programa de teste para a classe Calculadora.

# print(classes.Calculadora(3,3).somar())
# print(classes.Calculadora(3,3).subtrair())
# print(classes.Calculadora(3,3).multiplicar())
# print(classes.Calculadora(3,3).dividir())
# print(classes.Calculadora(3,3).calcularPotencia())

linha()

# # EXER 6:
# 6. Crie a classe Funcionario com os atributos nome e
# salario, recebidos pelo método construtor, e o método
# aumentarSalario(porcentagem) cujo parâmetro é a porcentagem de aumento. 
# Implemente um programa de teste
# para a classe, criando dois funcionários e simulando o aumento de 
# salário de 20% para um e 50% para o outro.


# funcionario1 = classes.Funcionario('Leonardo',1555)
# funcionario2 = classes.Funcionario('Paola',1555)

# print(funcionario1.aumentarSalario(20))
# print(funcionario2.aumentarSalario(50))

# 7. Implemente uma classe Carro, que tenha as propriedades
# consumo e combustível refletindo o consumo do carro em
# km/l e o combustível no tanque, respectivamente. O consumo
# é atribuído no método construtor, enquanto o combustível
# inicia com 0. Crie o método andar() para simular o ato de
# dirigir o veículo por uma certa distância (isso vai reduzir a
# quantidade de combustível no tanque). Crie um método
# exibirCombustivel(), que mostrará o nível atual em
# que o carro se encontra e o método abastecer(litros)
# para aumentar o nível de combustível do carro. Agora, crie o
# programa de teste e simule o passeio de um veículo.

carro1 = classes.Carro(1)
carro1.abastecer(50)
print(f'Abasteci {carro1.exibirCombustivel()} Litros')
print()
print(f'Andei {carro1.andar(15)} Kilometros')
print()
print(f'Fiquei com {carro1.exibirCombustivel()} Litros')
carro1.consumo = 1
print(carro1.exibirCombustivel())

linha()
