import time
import random
import math
import os

from BinaryTree import Tree
from Quee import Quee
from pessoa import Pessoa
from Stack import Stack

option = 0
space = ("-"*32)

while option != 6:

    paciente = Pessoa("paciente", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
    pai = Pessoa("pai", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
    mae = Pessoa("mae", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
    nono = Pessoa("nono", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
    nona = Pessoa("nona", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
    pessoa5 = Pessoa("nonamae", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )

    filadePessoas = Quee()
    filaPrioritaria = Quee()

    time.sleep(0.5)
    print (space + "\n|        Atendimento Upa        |\n" + space +"\n")
    time.sleep(0.5)

    option = int(input("Digite a opção desejada:\n[1] Cadastrar paciente\n[2] Consulta de paciente\n[3] Chamar proximo da fila\n[4] Adicionar a pilha do youtube\n[5] Tocar youtube\n[6] Sair\n "))

    if option == 1: 

        time.sleep(0.5)
        print ("\n" + space + "\n|     Cadastro de paciente     |\n" + space + "\n")

        paciente.nome = str(input("Nome: "))
        paciente.sexo = str(input("Sexo\n[M]Masculino\n[F]Feminino\n "))
        paciente.cpf = str(input("CPF: "))
        paciente.rg = str(input("RG: "))
        paciente.dia = str(input("Dia Nascimento: "))
        paciente.mes = str(input("Mes Nascimento: "))
        paciente.ano = str(input("Ano Nascimento: "))
        paciente.ctsus = int(input("Cartao SUS: "))
        paciente.sintomas = str(input("Quais os sintomas: "))
        
        time.sleep(0.5)
        print("\n" + space + "\n|CADASTRO REALIZADO COM SUCESSO|\n" + space + "\n")
        option = int(input("Digite a opção desejada:\n[1] Cadastrar paciente\n[2] Consulta de paciente\n[3] Chamar proximo da fila\n[4] Adicionar a pilha do youtube\n[5] Tocar youtube\n[6] Sair\n "))


    elif option == 2:
        print ("\n" + space + "\n|     Consulta de paciente     |\n" + space + "\n")
        time.sleep(0.5)
        cpf = int(input("Digite o CPF a ser consultado: "))

    elif option == 3:
        filadePessoas.atender(filaPrioritaria)
    #elif option == 4:
    #elif option == 5:

    elif option == 6:
        print("\n" + space + "\n|        Até a Proxima!        |\n" + space + "\n")
        time.sleep(1.5)
        exit()


paciente = Tree(paciente)
filadePessoas.inserir(paciente)
#filadePessoas.printarTodos()
filadePessoas.inserir(filaPrioritaria)


#id = math.ceil(9999999 * random.random())