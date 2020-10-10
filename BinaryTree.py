from pessoa import Pessoa

class Tree: 
    #construtor
    def __init__(self, Pessoa, pai=None, mae=None):
        self.pessoa = Pessoa
        self.pai = pai
        self.mae = mae

#adiciona os pais a classe
    def addPais(self, pai=None, mae=None):
        self.pai = pai
        self.mae = mae
      
    #mostra todas as gerações
    def mostrarTodaGeracao(self):
        if self.pai:
            print(self.pai.pessoa.nome)
            self.pai.mostrarTodaGeracao()
        if self.mae:
            print(self.mae.pessoa.nome)
            self.mae.mostrarTodaGeracao()

            

'''
#primeiro deve-se criar uma pessoa, usando o struct do Luan C é isso, veja a sequencia
# dos atributos no código do Luan C
pessoa = Pessoa("eu", "sexo",1, 1, 12, 32, 121, "ctsus", "sintomas" )
pai = Pessoa("pai", "sexo",12, 12, 12, 32, 121, "ctsus", "sintomas" )
mae = Pessoa("mae", "sexo",123, 123, 12, 32, 121, "ctsus", "sintomas" )
nono = Pessoa("nono", "sexo",1234, 1234, 12, 32, 121, "ctsus", "sintomas" )
nona = Pessoa("nona", "sexo",12345, 12345, 12, 32, 121, "ctsus", "sintomas" )
pessoa5 = Pessoa("nonamae", "sexo",123456, 123456, 12, 32, 121, "ctsus", "sintomas" )

# Após criar as pessoas, deve-se criar um nó, pode fazer da seguinte forma:
pai= Tree(pai)
mae= Tree(mae)
nono= Tree(nono)
nona= Tree(nona)
pessoa5= Tree(pessoa5)

# nesse caso, root é a RAIZ, o ponto inicial, o primeiro nó B)
root = Tree(pessoa)

# agora o método de adicionar pai e mae para a raiz
root.addPais(pai, mae)
#aqui esta adiconando o pai e mae do PAI
root.pai.addPais(nono,nona)
#aqui o pai da mae
root.mae.addPais(pessoa5)
## Aqui chama toda a geração do root, a variavel q chama, é a q vai ser usada nesse exemplo é o ROOT
root.mostrarTodaGeracao()

'''


    