import time
#import random
#import math
import os

from BinaryTree import Tree
from quee import Quee
from pessoa import Pessoa
from stack import Stack

option = 0

paciente = Pessoa("paciente", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
pai = Pessoa("pai", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
mae = Pessoa("mae", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
nono = Pessoa("nono", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
nona = Pessoa("nona", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )
pessoa5 = Pessoa("nonamae", "sexo","99", "99", "99", "99", "99", "ctsus", "sintomas" )



filadePessoas = Quee()
filaprioritariadePessoas = Quee()

paciente.nome = str(input("Qual o seu nome: "))
paciente.sexo = str(input("Sexo\n[M]Masculino\n[F]Feminino\n "))
paciente.cpf = str(input("CPF: "))
paciente.rg = str(input("RG: "))
paciente.dia = str(input("Dia Nascimento: "))
paciente.mes = str(input("Mes Nascimento: "))
paciente.ano = str(input("Ano Nascimento: "))
paciente.ctsus = int(input("Cartao SUS: "))
paciente.sintomas = str(input("Quais os sintomas: "))

paciente = Tree(paciente)
filadePessoas.inserir(paciente)
#filadePessoas.printarTodos()
filadePessoas.excluir()

















"""
space = ("-"*32)
option = 0
febre = 0
nomecompleto = 0
nomepai = 0
nomemae = 0
cpf = 00000000000
rg = 0000000
datanascimento = 0 
cartaosus = 0
idp = 0
idm = 0
sintoma = 0
idade = 0

#id = math.ceil(9999999 * random.random())

"""
time.sleep(0.5)
print (space + "\n|        Atendimento Upa        |\n" + space +"\n")
time.sleep(0.5)

option = int(input("Digite a opção desejada:\n[1] Cadastrar paciente\n[2] Consulta de paciente\n[3] Chamar proximo da fila\n[4] Adicionar a pilha do youtube\n[5] Tocar youtube\n[6] Sair\n "))

if option == 1: 
    print ("\n" + space + "\n|     Cadastro de paciente     |\n" + space + "\n")
    time.sleep(0.5)
    nomecompleto = str(input("Nome Completo: "))
    cpf = int(input("CPF: "))
    rg = int(input("RG: "))
    datanascimento = int(input("Data De nascimento (dd/mm/aaaa): "))
    cartaosus = int(input("Cadastro SUS: "))
    nomepai = str(input("Nome do pai: "))
    idp = int(input("ID Pai: "))
    nomemae = str(input("Nome da mãe: "))
    idm = int(input("ID Mãe: "))
    sintoma = str(input("Sintoma: "))
    time.sleep(0.5)
    print("\n" + space + "\n|CADASTRO REALIZADO COM SUCESSO|\n" + space)

elif option == 2:
    print ("\n" + space + "\n|     Consulta de paciente     |\n" + space + "\n")
    time.sleep(0.5)
    cpf = int(input("Digite o CPF a ser consultado: "))

#elif option == 3:
#elif option == 4:
#elif option == 5:

elif option == 6:
    print("\n" + space + "\n|        Até a Proxima!        |\n" + space + "\n")
    time.sleep(1.5)
    exit()


