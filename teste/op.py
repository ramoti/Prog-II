from flask import Flask, render_template, request
app = Flask (__name__)
from opa import Pessoa

@app.route ("/")
def trelar ():
    return render_template ("inicio.html")

@app.route ("/add_pessoa")
def add ():
    nome = request.args.get("nome")
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    r = "os dados recebidos foram"
    r += nome + "," + endereco + "," + telefone
    return r

@app.route ("/form_add_pessoa")
def form ():

    return render_template ("add_pessoa.html")

@app.route ("/danesse")
def tralar ():
    pessoas = [Pessoa ("Mariana" , "araçai" , "1234-1234"), Pessoa ("Lucas" , "patos", "5443-7346")]  
    return render_template ("danesse.html", lista = pessoas)


app.run(debug = True)