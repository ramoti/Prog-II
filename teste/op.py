from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
from peewee import *

db = SqliteDatabase ('lista_pessoa.db')

class Pessoa (Model):

    nome = CharField ()
    enredeco = CharField ()
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
 
    return render_template ("inicio.html" , pessoas = lista)

@app.route ("/add_pessoa")
def add ():

    nome = request.args.get("nome") 
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    cpf = request.args.get ("cpf")
    nova_pessoa = Pessoa (nome, endereco, telefone, cpf)
    lista.append (nova_pessoa)
    r = "os dados recebidos foram"
    r += nome + "," + endereco + "," + telefone
    return redirect ("/")
    return redirect ("/")

@app.route ("/excluir_pessoa")
def excluir ():

    nome = request.args.get ("nome")
    cpf = request.args.get ("cpf")
    for pessoa in lista :
        if nome == pessoa.nome or cpf == pessoa.cpf :
            lista.remove (pessoa)
            return redirect("/")
    return "erro ao excluir, não achei:"


@app.route ("/form_add_pessoa")
def form ():

    return render_template ("add_pessoa.html")

@app.route ("/danesse")
def tralar ():

    return render_template ("danesse.html", pessoas = lista)

@app.route ("/form_editar") 
def editar_form ():

    nome = request.args.get ("nome")
    cpf = request.args.get ("cpf")
    for i in range (len(lista)):
        if nome == lista[i].nome or cpf == lista[i].cpf:
            return render_template ("editar.html", person = lista[i] )
    return "pessoa n encontrada"

@app.route ("/editar")            
def editar_pessoa ():

    nome = request.args.get ("nome")
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    cpf = request.args.get ("cpf")
    for i in range(len(lista)):
        if lista[i].cpf == cpf :
            nova_pessoa = Pessoa (nome, endereco, telefone, cpf)
            lista [i] = nova_pessoa
            break
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
    