from peewee import *

db = SqliteDatabase ('./lista_pessoa.db')

class Pessoa (Model):

    nome = CharField ()
    endereco = CharField ()
    telefone = CharField ()
    cpf = CharField ()

    class Meta: 
        database = db

try:
    db.connect()
    db.create_tables ([Pessoa])

except OperationalError as error :

    print ("erro ao criar tabelas: " +str(error))

for p in Pessoa.select():
    print(p.nome)