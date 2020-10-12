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

filadePessoas = Quee()
filaPrioritaria = Quee()
database = Quee()

while option != 5:
    time.sleep(0.5)
    print (space + "\n|        Atendimento Upa        |\n" + space +"\n")
    time.sleep(0.5)

    option = int(input("Digite a opção desejada:\n[1] Cadastrar paciente\n[2] Consulta de paciente\n[3] Chamar proximo da fila\n[4] Pesquisar Gerações\n[5] Sair\n "))
    print(option)
    if option == 1: #FInalizado
        opt2= int(input("[1] Cadastrar Pessoa\n[2] Vincular pais"))
        time.sleep(0.5)
        if opt2 == 1:
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
                database.inserir(treePaciente)
            else:
                filadePessoas.inserir(treePaciente)
                database.inserir(treePaciente)
            time.sleep(0.5)
        else:
            print("Selecione de quem voce vai adicionar os pais")
            eu = database.searchByIndex()
            print("Selecione quem é o pai")
            pai = database.searchByIndex()
            print("Selecione quem é a mãe")
            mae = database.searchByIndex()
            eu.addPais(pai, mae)

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
        print("Selecione a pessoa na qual você quer ver a arvore genalogica:")
        database.searchByIndex().mostrarTodaGeracao()

    elif option == 5:
        print("\n" + space + "\n|        Até a Proxima!        |\n" + space + "\n")
        time.sleep(1.5)
        exit()
