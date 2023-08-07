from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para armazenar os usuários cadastrados
usuarios = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        email = request.form['email']
        usuarios.append({'nome': nome, 'idade': idade, 'email': email})

    return render_template('index.html', usuarios=usuarios)
