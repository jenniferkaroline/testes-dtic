from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "1234"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/banco'


db = SQLAlchemy(app)

class Pessoa(db.Model): #como os dados têm que ser na tabela pessoa
    __tablename__ = 'pessoa'
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False, primary_key=True)

@app.route('/')
def index():
    return 'Home'

@app.route('/criarPessoa')
def criarPessoa():
    try:
        novaPessoa = Pessoa(nome="Jennifer", idade=18)

        db.session.add(novaPessoa)
        db.session.commit()
        
        return 'Pessoa criada'

    except UnicodeDecodeError as e:
        return ("F Tropa", e)

if __name__ == "__main__":
    app.run(debug=True)
