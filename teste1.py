from flask import Flask, request, jsonify
import psycopg2 

app = Flask(__name__)

app.secret_key = "teste"


try:
    connection = psycopg2.connect(
        dbname = 'banco',
        user = 'postgres',
        password = '2005jenni',
        host = 'localhost',
        port = "5433",
        encoding = 'UTF8' 
        #codificação das caracteres do banco (importante p o postgres e o py usarem o mesmo tipo de codificação)
    )
    cursor = connection.cursor()
    print("conexao ok")
except (Exception, psycopg2.Error) as error:
    print("F tropa", error)
finally:
    if 'cursor' in locals() and 'connection' in locals():
        cursor.close()
        connection.close()








    