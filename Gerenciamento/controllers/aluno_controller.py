from models import Aluno
from config import db
from datetime import datetime

class AlunoController:
    @staticmethod
    def listar():
        return Aluno.query.all()
    
    @staticmethod
    def criar(data):
        # Converter string para datetime.date
        data_nascimento_str = data.get('data_nascimento')
        if not data_nascimento_str:
            raise ValueError("Campo data_nascimento é obrigatório")
        
        data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()
        
        novo = Aluno(
            nome=data['nome'],
            idade=data['idade'],
            turma_id=data.get('turma_id'),
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=data.get('nota_primeiro_semestre'),
            nota_segundo_semestre=data.get('nota_segundo_semestre'),
            media_final=data.get('media_final')
        )

        db.session.add(novo)
        db.session.commit()
        return novo
    
    @staticmethod
    def atualizar(aluno_id, data):
        aluno = Aluno.query.get_or_404(aluno_id)
        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        db.session.commit()
        return aluno
    
    @staticmethod
    def deletar(aluno_id):
        aluno = Aluno.query.get_or_404(aluno_id)
        db.session.delete(aluno)
        db.session.commit()
        return {}
    
        
    

        
