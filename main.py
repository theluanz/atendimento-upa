import time
import os
#import random
#import math


from BinaryTree import Tree
from Quee import Quee
from pessoa import Pessoa
from Stack import Stack

option = 0
space = ("-"*32)

paciente = Tree(Pessoa("paciente", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" ))
pai =  Tree(Pessoa("pai", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" ))
mae =  Tree(Pessoa("mae", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" ))
nono =  Tree(Pessoa("nono", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" ))
nona =  Tree(Pessoa("nona", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" ))
pessoa5 =  Tree(Pessoa("nonamae", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" ))

paciente.addPais(pai,mae)
pai.addPais(nono, nona)
filadePessoas = Quee()
filaPrioritaria = Quee()
filaPrioritaria.inserir(pai)
database = Quee()

while option != 6:


    time.sleep(0.5)
    print (space + "\n|        Atendimento Upa        |\n" + space +"\n")
    time.sleep(0.5)

    option = int(input("Digite a opção desejada:\n[1] Cadastrar paciente\n[2] Consulta de paciente\n[3] Chamar proximo da fila\n[4] Adicionar a pilha do youtube\n[5] Tocar youtube\n[6] Sair\n "))
    print(option)
    if option == 1: #FInalizado

        time.sleep(0.5)
        print ("\n" + space + "\n|     Cadastro de paciente     |\n" + space + "\n")

        nome = str(input("Nome: "))
        sexo = str(input("Sexo\n[M]Masculino\n[F]Feminino\n "))
        cpf = str(input("CPF: "))
        rg = str(input("RG: "))
        dia = str(input("Dia Nascimento: "))
        mes = str(input("Mes Nascimento: "))
        ano = str(input("Ano Nascimento: "))
        ctsus = int(input("Cartao SUS: "))
        sintomas = str(input("Quais os sintomas: "))
        
        paciente = Pessoa(nome,sexo ,cpf , rg, dia, mes, ano, ctsus, sintomas)
        treePaciente = Tree(paciente)
        tmp = int(input("É prioritario? (Acima de 60 anos ou febre?)\n[0] Não \n[1] Sim "))
        if tmp==1:
            filaPrioritaria.inserirPrioritario(treePaciente)
        else:
            filadePessoas.inserir(treePaciente)
            database.inserir(treePaciente)
        time.sleep(0.5)

        print("\n" + space + "\n|CADASTRO REALIZADO COM SUCESSO|\n" + space + "\n")

    elif option == 2: #Finalizado
        print ("\n" + space + "\n|     Consulta de paciente     |\n" + space + "\n")
        time.sleep(0.5)
        #cpf = int(input("Digite o CPF a ser consultado: "))
        filadePessoas.printarTodos()
        filaPrioritaria.printarTodos()

    elif option == 3: #Finalizado
        filadePessoas.atender(filaPrioritaria)
        time.sleep(1.5)
    elif option == 4:#usando a opçao 4 so para testar
        database.searchByIndex().addPais(pai, mae)
        pai = database.searchByIndex()
        mae = database.searchByIndex()
    elif option == 5:
        

    elif option == 6:
        print("\n" + space + "\n|        Até a Proxima!        |\n" + space + "\n")
        time.sleep(1.5)
        exit()

'''
paciente = Tree(paciente)
filadePessoas.inserir(paciente)
#filadePessoas.printarTodos()
filadePessoas.inserir(filaPrioritaria)

'''
#id = math.ceil(9999999 * random.random())