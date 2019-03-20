from flask import Flask, render_template
app = Flask (__name__)
from opa import Pessoa

@app.route ("/")
def trelar ():
    return render_template ("inicio.html")

@app.route ("/danesse")
def tralar ():
    pessoas = [Pessoa ("Mariana" , "araçai" , "1234-1234"), Pessoa ("Lucas" , "patos", "5443-7346")]  
    return render_template ("danesse.html", lista = pessoas)


app.run(debug = True)