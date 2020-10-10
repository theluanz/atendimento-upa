class Stack:
    def __init__(self):
        self.vetor = []
    def inserir(self, link):    
        self.vetor.append(link)
    def excluir(self):
        if self.vetor:    
            self.tocar(self.vetor[-1])
            del self.vetor[-1]
        else:
            print("Pilha Vazia, não é possivel tocar")
    def tocar(self, link):
        print(link)
    
'''
#Dessa forma voce cria um variavel da classe Stack
classePilha = Stack()
#Dessa forma voce insere um link
classePilha.inserir("linkkkkkkkkkkkkkk")
classePilha.inserir("linkkkkkkkkkkkkkk2")
#Dessa forma voce exclui e faz tocar um valor
classePilha.excluir()
classePilha.excluir()
'''
