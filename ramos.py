from peewee import *
import os

db = peewee.SqliteDatabase ('Pizada.db')
arq = 'pode_cre.db'


class Pi(BaseModel):
    def __init__(self, titulo, ano, nomes_alunos, nome_professor):
        self.titulo = titulo
        self.ano = ano
        self.nomes_alunos = nomes_alunos
        self.professores = nome_professor

class Aluno(BaseModel):
    def __init__(self, turma, nome, idade):
        self.turma = turma
        self.nome = nome
        self.idade = idade

class Professor(BaseModel):
    def __init__(self, nome, idade, area_atua):
        self.nome = nome
        self.idade = idade
        self.area_atua= area_atua

class Area(BaseModel):
    def __init__(self, periodico, evento):
        self.periodico = periodico
        self.evento = evento

class BaseModel (Model):
    class meta :
        database = db

if __name__=="__main__":
    alunos=[Aluno("302 INFO", "Piske", 18),Aluno("302 INFO", "Ravi", 18)]
    val=Pi("jogo de plataforma",2019,alunos,"Hylson")
    professor=[Professor("Hylson",34,"programção")]


    print()
    print("__________PROJETO INTEGRADOR ___________")
    print()
    print("Título do trabalho:", val.titulo)
    print("Ano:", val.ano)
    print("Alunos:")
    print()
    for i in alunos:
        print("nome: ", i.nome)
        print("idade: ", i.idade)
        print("turma: ", i.turma)
        print()
    print("Professores coordenadores:")
    print()
    for i in professor:
        print("nome: ", i.nome)
        print("idade: ", i.idade)
        print("Área de Atuação: ", i.area_atua)
        print()
