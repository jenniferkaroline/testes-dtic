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
        if data is None: #verificando se o usuário não inseriu nenhum dado
            return 'Nenhum dado recebido'

        nome = data.get('nome')
        idade = data.get('idade')
        
        if nome is None or idade is None: #verificando se deixou algum campo nulo
            return 'Nome e Idade não podem ser nulos'

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
        return jsonify(pessoas) #retornando as colunas da tabela pessoa
    
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

        if 'nome' not in data or 'idade' not in data: #caso o usuário não tenha enviado os dados para a atualização e solicitou mesmo assim
            return 'Dados incompletos para atualização'

        novoNome = data['nome']
        novaIdade = data['idade']
        print("Novo nome: ", novoNome)
        print("Nova idade: ", novaIdade)

        cursor.execute("UPDATE pessoa SET nome = %s, idade = %s WHERE id = %s", (novoNome, novaIdade, id))
        connection.commit()
        return 'Dados Atualizados'
    
    except (Exception, psycopg2.Error) as error:
        print("Erro:", error)
        return 'Erro ao atualizar pessoa'


if __name__ == "__main__":
    app.run(debug=True)
