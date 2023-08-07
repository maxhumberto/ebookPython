import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect('banco_de_dados.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Executar comandos SQL
cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)')

# Salvar as alterações no banco de dados
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()
