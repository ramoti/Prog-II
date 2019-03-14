from flask import Flask, render_template
app = Flask (__name__)

@app.route ("/")
def trelar ():
    return render_template ("inicio.html")

@app.route ("/danesse")
def tralar ():
    return render_template ("danesse.html")

app.run(host="0.0.0.0")