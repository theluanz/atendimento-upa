"""import time
import random
#import imp
#pessoa = imp.load_source('pessoa', 'cd ../estruturas/Pessoa.py')
#pessoa.testar()

#idp = 1

space = ("-"*32)
febre = 0
nomecompleto = 0
cpf = 00000000000
rg = 0000000
datanascimento = 0 
"""(Acima de 60 anos prioridade)
idPessoa (deve ser único)"""
cartaosus = 0
idp = 0
idm = 0
"""idPai // caso não tenha, ID=0, isso é necessário no segundo projeto
idMãe // caso não tenha, ID=0, isso é necessário no segundo projeto"""
sintoma = 0
idade = 0

print ("\n\n" + space)
time.sleep(0.8)
print ("| Bem Vindo Ao Atendimento Upa |")
time.sleep(0.5)
print (space + "\n")

time.sleep(0.5)
print ("Para começar, preciso que voce \nresponda três perguntas iniciais.\n")

nomecompleto = str(input("Qual seu nome: "))
febre = int(input("Você está com febre? \n[1]Sim\n[2]Nao\n"))
idade = 


if febre == 1:
    print("Prioridade maxima\n")
    time.sleep(0.5)
    print("Voce esta na fila de prioridade maxima.\nEnquanto isso iremos realizar seu cadastro: ")
    cpf = int(input("CPF: "))
    rg = int(input("RG: "))
    datanascimento = int(input("Data De nascimento: "))
    cartaosus = int(input("Cartao SUS: "))
    sintoma = str(input("Quais sao seus sintomas?: "))
    print (space +"\nCADASTRO EFETUADO COM SUCESSO!!!\n" + space)

if idade > 59:
    print("Prioridade maxima\n")
    time.sleep(0.5)
    print("Voce esta na fila de prioridade maxima.\nEnquanto isso iremos realizar seu cadastro: ")
    cpf = int(input("CPF: "))
    rg = int(input("RG: "))
    datanascimento = int(input("Data De nascimento: "))
    cartaosus = int(input("Cartao SUS: "))
    sintoma = str(input("Quais sao seus sintomas?: "))
    print (space +"\nCADASTRO EFETUADO COM SUCESSO!!!\n" + space)


if febre == 2:
    time.sleep(0.5)
    print("Baixa Prioridade")

#idp = random.sample(range(0,100), 4)
#print ("Seu Id é: ")
#print (ipd)"""
import random
import math

print(math.ceil(100000000000 * random.random()))