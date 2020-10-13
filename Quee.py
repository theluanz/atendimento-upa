from pessoa import Pessoa
from BinaryTree import Tree

space = ("-"*32)

class Quee:
    def __init__(self):
        self.vetor = []
    def inserir(self, TreePessoa):    
        self.vetor.append(TreePessoa)
    def inserirPrioritario(self, TreePessoa):
        isFebre= True if 'febre' in TreePessoa.pessoa.sintomas else False
        if isFebre:
            tmp=0
            for x in self.vetor:
                tem_febre = True if 'febre' in x.pessoa.sintomas else False
                if not(tem_febre): 
                    print(x.pessoa.sintomas)
                    self.vetor.insert(tmp,TreePessoa)
                    break
                tmp+=1
            if tmp == len(self.vetor):
                self.vetor.append(TreePessoa)
        else:
            self.vetor.append(TreePessoa)
            
    
    def atender(self, quee):
        if quee.vetor:
            print("Atendimento Prioritário")
            print("Atendimento de agora: " + quee.vetor[0].pessoa.nome)
            del quee.vetor[0]
        elif self.vetor:
            print("Atendimento Normal")
            print("Atendimento de agora: " + self.vetor[0].pessoa.nome)
            del self.vetor[0]    
        else:
            print(space + "\n|    Nenhum usuario na fila    |\n" + space)
    
    
    def printarTodos(self):
        for x in self.vetor:
            print("="*50)
            print("Nome: {}".format(x.pessoa.nome))
            print("CPF: {}".format(x.pessoa.cpf))
            print("Data Nascimento: {}/{}/{}".format(x.pessoa.dia,x.pessoa.mes, x.pessoa.ano ))
            print("Sintomas: {}".format(x.pessoa.sintomas))
            print("="*50)

    def searchByIndex(self):
        tmp=0
        for x in self.vetor:
            print("="*50)
            print("Indice: {}".format(tmp))
            print("Nome: {}".format(x.pessoa.nome))
            print("CPF: {}".format(x.pessoa.cpf))
            tmp+=1
            print("")
        return self.vetor[int(input("Digite o index correspondente: "))]









































'''
pessoa = Pessoa("eu", "sexo",1, 1, 12, 32, 121, "ctsus", "zap" )
pai = Pessoa("pai", "sexo",12, 12, 12, 32, 121, "ctsus", "a" )
mae = Pessoa("mae", "sexo",123, 123, 12, 32, 121, "ctsus", "febre" )
pai= Tree(pai)
mae= Tree(mae)
root = Tree(pessoa)
root.addPais(pai, mae)

#AQUI COMEÇA A LISTA:

#Para criar uma varia do tipo Quee basta importar a Quee e colocar o seguinte:
# nomeVar = Quee() // assim ele vai criar uma variavel do tipo lista
#Detalhe, crie filas diferentes para prioritario e nao prioritario
filadePessoas = Quee()
filadePessoasPrioritaria = Quee()

#para adicionar algum elemento basta fazer o seguinte:
#Como parametro deve passar uma variavel do TIPO ARVORE!!! isso é importante
#filadePessoas.inserir(root)

#Para a fila prioritaria use o seguinte metodo, isso somente na prioritaria
#filadePessoasPrioritaria.inserirPrioritario(pai)

#função para atender as pessoas
filadePessoas.atender(filadePessoasPrioritaria)
#Função pra listar todos os usuarios da fila
##filadePessoas.printarTodos()

#Exemplo de função pra retornar as gerações que eu fiz na Arvore
##filadePessoas.searchByIndex().mostrarTodaGeracao()
'''