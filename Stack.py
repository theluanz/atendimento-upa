import os
space = ("-"*36)

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
            print(space + "\n| Pilha Vazia não é possivel tocar |\n" + space + "\n")
            time.sleep(0.5)
    def tocar(self, link):
        os.system("xdg-open {}".format(link)) 
        os.system("start {}".format(link))      
































'''
#Dessa forma voce cria um variavel da classe Stack
classePilha = Stack()
#Dessa forma voce insere um link
classePilha.inserir("https://www.youtube.com/watch?v=xL-Mdet-cow)
classePilha.inserir(" https://www.youtube.com/watch?v=xL-Mdet-cow")
#Dessa forma voce exclui e faz tocar um valor
classePilha.excluir()
'''