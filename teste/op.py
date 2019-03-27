from flask import Flask, render_template, request
app = Flask (__name__)
from opa import Pessoa

pessoas = [Pessoa ("Mariana" , "araçai" , "1234-1234"), Pessoa ("Lucas", "patos", "5443-7346")]  


@app.route ("/")
def listar_pessoa ():
    return render_template ("inicio.html" , lista = pessoas)

@app.route ("/add_pessoa")
def add ():
    nome = request.args.get("nome")
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    nova_pessoa = Pessoa (nome, endereco, telefone)
    pessoas.append (nova_pessoa)
    r = "os dados recebidos foram"
    r += nome + "," + endereco + "," + telefone
    return render_template ("nova.html", mensagem = "pessoa inserida")

@app.route ("/form_add_pessoa")
def form ():

    return render_template ("add_pessoa.html")

@app.route ("/danesse")
def tralar ():
    return render_template ("danesse.html", lista = pessoas)


app.run(debug = True)