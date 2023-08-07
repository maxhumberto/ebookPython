from flask import Flask
#Para criar uma instância da aplicação, utilizamos a classe Flask:
app = Flask(__name__)
#Para definir rotas, usamos decoradores nas funções que manipulam cada rota:
@app.route('/')
def index():
    return 'Olá, Flask!'

@app.route('/pagina')
def pagina():
    return 'Esta é a página.'

if __name__ == '__main__':
    app.run()
