from flask import Flask, render_template, request, redirect, session, url_for
from flask_admin import helpers
from flask_login import loginManeger, Userminix, current_user, login_required, login_user, logout_user
from peewee import *
from modelo import Pessoa, Config
import os
from wtforms import Form , StringField, PasswordField, FileField
from wtforms.validators import input_required , emamil
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash , check_password_hash

app = Flask (__name__)
app.config.uupdate (UPLOAD_FOLDER = os.path.join(app.root_path, 'static'),
                    ALLOWED_EXTENSIONS = set (['jpg' , 'jpeg' , 'png']))
@app.route ("/")
def listar_pessoa ():

    return render_template ("inicio.html" , lista = Pessoa.select())

@app.route ("/add_pessoa", methods = ["GET" ,"POST" ])
def add ():

    nome = request.args.get("nome") 
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    email = request.args.get ("email")
    cpf = request.args.get ("cpf")
    if request.method == "POST" :
        if request.files :
            imagem = request.files ["imagem"]
            print (imagem)

    nova_pessoa = Pessoa.create (nome = nome, endereco = endereco, telefone = telefone, email = email, cpf = cpf)

    return redirect ("/")

@app.route ("/excluir_pessoa")
def excluir ():

    id = request.args.get ("id")
    Pessoa.delete_by_id (id)

    return redirect("/")


@app.route ("/form_add_pessoa")
def form ():

    return render_template ("add_pessoa.html")


@app.route ("/form_editar") 
def editar_form ():

    id = request.args.get ('id')
    pessoa_a_ser_alterada = Pessoa.get_by_id (id)
    return render_template ("editar.html", pessoa = pessoa_a_ser_alterada)

@app.route ("/editar")            
def editar_pessoa ():

    id = request.args.get ("id")
    nome = request.args.get ("nome")
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    email = request.args.get ("email")
    cpf = request.args.get ("cpf")
    pessoa_alterada = Pessoa.get_by_id (id)
    pessoa_alterada.nome = nome
    pessoa_alterada.endereco = endereco
    pessoa_alterada.telefone = telefone
    pessoa_alterada.email = email
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

@app.route ("/buscar")
def buscar ():

    nome_procurado = request.args.get ("nome")

    return render_template ("pessoa_encontrada.html" , lista = Pessoa.select(), nome = nome_procurado)


app.config["SECRET_KEY"] = "51726.0"
app.run(debug= True)
