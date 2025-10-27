from flask import Flask
from flasgger import Swagger

from config import db, ma

def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Minha API Escolar',
        'uiversion': 3,
        'openapi': '3.0.2'
    }
    swagger = Swagger(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Importar modelos para registrar no SQLAlchemy
    from models import professor, aluno, turma
    with app.app_context():
        db.create_all()

    # Registrar rotas
    from routes.aluno_routes import aluno_bp
    from routes.professor_routes import professor_bp
    from routes.turma_routes import turma_bp


    app.register_blueprint(aluno_bp)
    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
