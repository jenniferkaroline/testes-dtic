from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(14), nullable=False, unique=True)  
    nome = db.Column(db.String(14), nullable=False)
    senha = db.Column(db.String(100), nullable=False)  