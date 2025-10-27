from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Notas(db.Model):
    __tablename__ = 'notas'

    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Float, nullable=False)
    aluno_id = db.Column(db.Integer, nullable=False)
    atividade_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Notas id={self.id}, nota={self.nota}, aluno_id={self.aluno_id}, atividade_id={self.atividade_id}>"
