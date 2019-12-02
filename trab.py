import os
from peewee import *

arq = "SistemaEspacial.db"
db = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
        database = db


class Jogador (BaseModel):

    nome = CharField ()
    idade = CharField ()

    def __str__(self):
        return self.nome + self.idade


class Penalidade (BaseModel):

    numero_de_partidas = CharField()
    nivel_gravidade = CharField ()

    def __str__(self):

        return self. numero_de_partidas + self.nivel_gravidade

class Campeonato (BaseModel):

    nome = CharField ()
    nivel = CharField ()
    premio = ForeignKeyField (Premio)

    def __str__(self):
    
        return self.nome + self.nivel + self.premio

class Round (BaseModel):

    tempo = CharField()
    numero = CharField()

    def __str__(self):
        return self.tempo + self.numero

class Partida (BaseModel):

    narrador = ForeignKeyField (Narrador)
    rounds = ForeignKeyField (Round)
    times = ForeignKeyField (Time)
    jogadores = ForeignKeyField (Jogador)
    pausa = ForeignKeyField (Pause)
    data = CharField ()

    def __str__(self):

        return self.narrador + self.rounds + self.times + self.jogadores + self.pausa + self.data
    

class Narrador (BaseModel):

    nome = CharField ()
    lingua = CharField()

    def __str__(self):

        return self.nome + self.lingua

class Tecnico (BaseModel):

    nome = CharField ()
    time = ForeignKeyField (Time)

    def __str__(self):

        return self.nome + self.time

class Premio (BaseModel):

    campeoes = CharField()
    vice_campeoes = CharField()

    def __str__(self):

        return self.campeões + self.vice_campeoes

class Pause (BaseModel):

    motivo = CharField ()
    tempo = CharField()

    def __str__(self):

        return self.motivo + self.tempo

class Time (BaseModel):

    jogadores = ForeignKeyField (Jogador)
    tecnico = ForeignKeyField (Tecnico)
    nacionalidade = CharField ()

    def __str__(self): 

        return self.jogadores + self.tecnico + self.nacionalidade
