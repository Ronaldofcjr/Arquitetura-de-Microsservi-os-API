from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Atividades(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome_atividade = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100))
    peso_porcento = db.Column(db.Integer, nullable=False)
    data_entrega = db.Column(db.Date, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (
            f"<Atividades id={self.id}, nome='{self.nome_atividade}', "
            f"peso={self.peso_porcento}%, data_entrega={self.data_entrega}, "
            f"turma_id={self.turma_id}, professor_id={self.professor_id}>"
        )
