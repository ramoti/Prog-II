from peewee import *

db = SqliteDatabase ('lista_pessoa.db')


class Pessoa (Model):

    nome = CharField ()
    endereco = CharField ()
    telefone = CharField ()
    email = CharField ()
    cpf = CharField ()
    ###foto = FileField ('imagem', validators = [FileRequired (), 
                                             ###FileAllowed (['jpg', 'png' , 'jpeg'])])

    class Meta: 
        database = db


class Config :
    SQLALCHEMY_DATABASE_URI = 'sqlite:gravar'
    upload_folder = '/Documentos/GitHub/Prog-II/teste/static/upload'

try :

    db.connect()
    db.create_tables ([Pessoa])


except OperationalError as error :

    print ("erro ao criar tabelas: " +str(error))
