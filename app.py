from flask import Flask, request, jsonify
import psycopg2 

app = Flask(__name__)
app.secret_key = "teste"

try:
    connection = psycopg2.connect(
        dbname='banco',
        user='postgres',
        password='2005jenni',
        host='localhost',
        port="5433",
    )
    
    cursor = connection.cursor()
    print("Conexão ok")

except (Exception, psycopg2.Error) as error:
    print("Erro ao conectar ao banco de dados: ", error)

@app.route('/')
def index():
    return 'Home'

@app.route('/criarPessoa', methods=['POST'])
def criarPessoa():
    try:
        data = request.json 
        nome = data['nome']
        idade = data['idade']

        #add dados na tabela pessoa
        cursor.execute("INSERT INTO pessoa (nome, idade) VALUES (%s, %s)", (nome, idade))
        connection.commit()

        return 'Pessoa criada com sucesso'
    except (Exception, psycopg2.Error) as error:
        return ('Erro ao criar pessoa: ', error) 

@app.route('/listarPessoas', methods=['GET'])
def listarPessoas():
    try:
        cursor.execute("SELECT * FROM pessoa")
        pessoas = cursor.fetchall()
        return jsonify(pessoas)
    except (Exception, psycopg2.Error) as error:
        return ('Erro ao listar pessoas: ', error)

@app.route('/excluirPessoa/<int:id>', methods=['DELETE'])
def excluirPessoa(id):
    try:
        cursor.execute("DELETE FROM pessoa WHERE id = %s", (id,))
        connection.commit()

        return 'Pessoa excluída com sucesso'
    except (Exception, psycopg2.Error) as error:
        return ('Erro ao excluir pessoa: ', error)


@app.route('/atualizarPessoa/<int:id>', methods=['PUT'])
def atualizarPessoa(id):
    try:
        data = request.json 
        novaIdade = data['idade']

        cursor.execute("UPDATE pessoa SET idade = %s WHERE id = %s", (novaIdade, id))
        connection.commit()

        return 'Pessoa atualizada com sucesso'
    except (Exception, psycopg2.Error) as error:
        return ('Erro ao atualizar pessoa: ', error)


if __name__ == "__main__":
    app.run(debug=True)
