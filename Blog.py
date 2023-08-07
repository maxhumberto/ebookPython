from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para armazenar as tarefas
tarefas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        tarefas.append({'titulo': titulo, 'descricao': descricao})

    return render_template('3index.html', tarefas=tarefas)