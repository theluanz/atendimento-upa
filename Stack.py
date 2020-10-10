import os

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
        os.system("xdg-open {}".format(link))    
'''
#Dessa forma voce cria um variavel da classe Stack
classePilha = Stack()
#Dessa forma voce insere um link
classePilha.inserir("https://www.youtube.com/watch?v=d-GgZpCtBXw")
classePilha.inserir("https://www.youtube.com/watch?v=xL-Mdet-cow")
#Dessa forma voce exclui e faz tocar um valor
classePilha.excluir()
'''