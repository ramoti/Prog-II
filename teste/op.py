from flask import Flask, render_template, request
app = Flask (__name__)
from opa import Pessoa

pessoas = [Pessoa ("Mariana" , "araçai" , "1234-1234", "456.456.456-35"), Pessoa ("Lucas", "patos", "5443-7346", "456.456.456-33")]  


@app.route ("/")
def listar_pessoa ():

    return render_template ("inicio.html" , lista = pessoas)

@app.route ("/add_pessoa")
def add ():

    nome = request.args.get("nome")
    endereco = request.args.get ("endereco")
    telefone = request.args.get ("telefone")
    cpf = request.args.get ("cpf")
    nova_pessoa = Pessoa (nome, endereco, telefone, cpf)
    pessoas.append (nova_pessoa)
    r = "os dados recebidos foram"
    r += nome + "," + endereco + "," + telefone
    return render_template ("nova.html", mensagem = "pessoa inserida")

@app.route ("/excluir_pessoa")
def excluir ():

    nome = request.args.get ("nome")
    cpf = request.args.get ("cpf")
    for pessoa in pessoas :
        if nome == pessoa.nome or cpf == pessoa.cpf :
            pessoas.remove (pessoa)
            break
    return render_template ("velha.html", mensagem = "pessoa excluida")


@app.route ("/form_add_pessoa")
def form ():

    return render_template ("add_pessoa.html")

@app.route ("/danesse")
def tralar ():

    return render_template ("danesse.html", lista = pessoas)

@app.route ("/form_editar") 
def editar_form ():

    nome = request.args.get ("nome")
    cpf = request.args.get ("cpf")
    for i in range (len(pessoas)):
        if nome == pessoa.nome or cpf == pessoa.cpf:
            pass


app.run(debug = True)