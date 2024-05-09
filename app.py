from flask import Flask, request, jsonify
import psycopg2 

app = Flask(__name__)

#a conexão com o banco não está dando certo -> RESOLVER

connection = psycopg2.connect(
        dbname = 'banco',
        user = 'postgres',
        password = '2005jenni',
        host = 'localhost',
        encoding = 'UTF8' #codificação das caracteres do banco (importante p o postgres e o py usarem o mesmo tipo de codificação)
        )
    
cursor = connection.cursor()
    
    
cursor.close()
connection.close()



'''
@app.route('/pessoa', methods=['POST'])
def criar_pessoa():
    data = request.json 
    nome = data['nome']
    idade = data['idade']

    cursor.execute("INSERT INTO pessoa (nome, idade) VALUES (%s, %s)", (nome, idade))
'''

    