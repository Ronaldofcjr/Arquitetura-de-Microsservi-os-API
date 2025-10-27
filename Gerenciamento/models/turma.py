from config import db
from sqlalchemy import ForeignKey

class Turma(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    ativo = db.Column(db.Boolean, nullable=False, default=True)

    professor = db.relationship(
        "Professor", 
        back_populates="turmas"
    )

    alunos = db.relationship(
        "Aluno", 
        back_populates="turma", 
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Turma {self.descricao}>"