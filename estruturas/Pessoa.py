class Pessoa:
    def __init__(self, nome, cpf, rg, dia, mes, ano, idpessoa, ctsus, idpai, idmae, sintomas ):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.idpessoa = idpessoa
        self.ctsus = ctsus
        self.idpai = idpai
        self.idmae = idmae
        self.sintomas = sintomas

class Diagnostico:
    def __init__(self, pessoa, febre):
        self.pessoa = pessoa
        self.febre = febre
