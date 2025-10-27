from models import Professor
from config import db

class ProfessorController:
    @staticmethod
    def listar():
        return Professor.query.all()
    
    @staticmethod
    def consultar_professor(professor_id):
        return Professor.query.filter_by(id=professor_id).first()

    @staticmethod
    def criar(data):
        for campo in ['nome', 'idade', 'materia']:
            if campo not in data:
                raise ValueError(f"Campo obrigatório {campo} ausente")

        novo = Professor(
            nome=data['nome'],
            idade=int(data['idade']),
            materia=data['materia'],
            observacoes=data.get('observacoes')
        )
        db.session.add(novo)
        db.session.commit()
        return novo

    @staticmethod
    def atualizar(professor_id, data):
        professor = Professor.query.get_or_404(professor_id)
        professor.nome = data.get('nome', professor.nome)
        professor.idade = data.get('idade', professor.idade)
        professor.materia = data.get('materia', professor.materia)
        professor.observacoes = data.get('observacoes', professor.observacoes)
        db.session.commit()
        return professor

    @staticmethod
    def deletar(professor_id):
        professor = Professor.query.get_or_404(professor_id)
        db.session.delete(professor)
        db.session.commit()
        return {}
