from flask import Flask, render_template, request, redirect
from jinja2 import *
from questao import Questao
from listas_questoes import listas

app= Flask(__name__)

user = {'questoes_corretas':[]}


@app.route("/menu")
def menu():
    return render_template("MENU.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/atividades")
def atividade():
    return render_template("atividades.html", range_len_listas=range(len(listas)))

@app.route("/realizar_atividade")
def realizar_atividade():
    questao_id = request.args.get('questao_id')
    lista_id = int(request.args.get('lista_id'))
    if questao_id==None:
        user['questoes_corretas']=[]
        return render_template("realizar_atividade.html", questao=listas[lista_id][0], lista_id=lista_id)
    else:
        questao_id = int(questao_id)
        q = listas[lista_id][questao_id]
        a = request.args.get('alternativa')
        if a==q.resposta:
            user['questoes_corretas'].append(q)
        if questao_id==len(listas[lista_id])-1:
            print(user['questoes_corretas'])
            return render_template("atividade_realizada.html", questoes_corretas=user['questoes_corretas'], lista_id=lista_id, lista=listas[lista_id])
        else:
            return render_template("realizar_atividade.html", questao=listas[lista_id][questao_id+1],lista_id=lista_id)

@app.route("/conteudo")
def conteudo():
    pagina = request.args.get("pagina")
    if pagina==None:
        return render_template("conteudo.html")
    return render_template("{}.html".format(pagina))

@app.route("/mais")
def mais():
    return render_template("mais.html")




app.run(host="127.0.0.1")
