from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
from peewee import *

db = SqliteDatabase ('./Prog-II/teste/lista_pessoa.db')

class Pessoa (Model):

    nome = CharField ()
    endereco = CharField ()
    telefone = CharField ()
    cpf = CharField ()

    class Meta : 
        database = db

lista = []

try :

    db.connect()
    db.create_tables ([Pessoa])


except OperationalError as error :

    print ("erro ao criar tabelas: " +str(error))


@app.route ("/")
def listar_pessoa ():
 
    return render_template ("inicio.html" , lista = Pessoa.select())

@app.route ("/add_pessoa")
def add ():

    nome = request.args.get("nome") 
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    cpf = request.args.get ("cpf")
    nova_pessoa = Pessoa.create (nome = nome, endereco = endereco, telefone = telefone, cpf = cpf)
    r = "os dados recebidos foram"
    r += nome + "," + endereco + "," + telefone
    return redirect ("/")
    return redirect ("/")

@app.route ("/excluir_pessoa")
def excluir ():

    id = request.args.get ("id")
    Pessoa.delete_by_id (id)

    return redirect("/")


@app.route ("/form_add_pessoa")
def form ():

    return render_template ("add_pessoa.html")

@app.route ("/danesse")
def tralar ():

    return render_template ("danesse.html", pessoas = lista)

@app.route ("/form_editar") 
def editar_form ():

    id = request.args.get ('id')
    pessoa_a_ser_alterada = Pessoa.get_by_id (id)
    return render_template ("editar.html", person = pessoa_a_ser_alterada)
    
@app.route ("/editar")            
def editar_pessoa ():

    id = request.args.get ("id")
    nome = request.args.get ("nome")
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    cpf = request.args.get ("cpf")
    pessoa_alterada = Pessoa.get_by_id (id)
    pessoa_alterada.nome = nome
    pessoa_alterada.endereco = endereco
    pessoa_alterada.telefone = telefone
    pessoa_alterada.cpf = cpf
    pessoa_alterada.save()
    return redirect ("/")

@app.route ("/form_login")
def form_login ():
    
    return render_template ("form_login.html")

@app.route ("/login", methods = ["POST"])
def login ():

    login = request.form ["login"]
    senha = request.form ["senha"]

    if login and senha:
        session["usuario"] = login
        return redirect ("/")

    else :
        return "login ou senha inválidos"

@app.route ("/logout")
def logout ():

    session.pop ("usuario")
    return redirect ("/")

app.config["SECRET_KEY"] = "51726.0"
app.run(debug= True)