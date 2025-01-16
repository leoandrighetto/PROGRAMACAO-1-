class Alunos(): # DEFINE A CLASSE

    def __init__(self, nome, idade, matricula, curso):       # __INIT__ -- INICIALIZA A CLASSE. 
                                                             # SELF = Faz referência à classe criada; (Características). 
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.curso = curso
        
    def Situacao(self, mediasemestre): #MÉTODOS/FUNÇÕES QUE O OBJETO FAZ (verbos)

        if mediasemestre >= 7:
            print('Passou de semestre')
        else:
            print('Não passou de semestre')
    
    def Apresentar(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Cursando: {self.curso}'
    


aluno1 = Alunos('Leonardo','26','2024016743','ADS') #DECLARA UM OBJETO (NESTE CASO UM ALUNO)

# PRINTS

aluno1.Situacao(7)  
print()
print(aluno1.Apresentar())
