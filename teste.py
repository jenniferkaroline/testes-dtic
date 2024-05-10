from flask import Flask

import psycopg2

app = Flask(__name__)

conexao = psycopg2.connect(database  = "banco", host= "localhost", user = "postgres", password = "2005jenni", port = "5433")


@app.route("/")
def index():
    return conexao.dsn


if __name__ == "__main__":
    app.run(debug=True)