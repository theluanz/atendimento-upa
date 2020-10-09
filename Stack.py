class Stack:
    def __init__(self, link):
        self.vetor = []
    def inserir(self, link):    
        self.vetor.append(link)
    def excluir(self):
        print(self.vetor[-1])
        del self.vetor[-1]
