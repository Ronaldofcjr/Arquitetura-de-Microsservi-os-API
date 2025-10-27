from .professor_routes import professor_bp
#from .aluno_routes import aluno_bp
#from .turma_routes import turma_bp

def register_routes(app):
    app.register_blueprint(professor_bp, url_prefix="/professores")
    #app.register_blueprint(aluno_bp, url_prefix="/alunos")
    #app.register_blueprint(turma_bp, url_prefix="/turmas")