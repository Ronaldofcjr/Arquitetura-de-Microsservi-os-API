from flask import Blueprint, request, jsonify
from controllers.professor_controller import ProfessorController

professor_bp = Blueprint('professores', __name__, url_prefix='/professores')

@professor_bp.route('/', methods=['GET'])
def listar_professores():
    """
    Listar todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Retorna a lista de professores cadastrados
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nome:
                type: string
                example: "Carlos Silva"
              idade:
                type: integer
                example: 40
              materia:
                type: string
                example: "Matemática"
              observacoes:
                type: string
                example: "Professor com 15 anos de experiência"
    """
    professores = ProfessorController.listar()
    return jsonify([{'id': p.id, 'nome': p.nome, 'idade': p.idade, 'materia': p.materia, 'observacoes': p.observacoes} for p in professores])

@professor_bp.route('/', methods=['POST'])
def criar_professor():
    """
    Criar um novo professor
    ---
    tags:
      - Professores
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
            - idade
            - materia
          properties:
            nome:
              type: string
              example: "Ana Souza"
            idade:
              type: integer
              example: 35
            materia:
              type: string
              example: "História"
            observacoes:
              type: string
              example: "Professora especialista em história moderna"
    responses:
      201:
        description: Professor criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 2
            nome:
              type: string
              example: "Ana Souza"
            idade:
              type: integer
              example: 35
            materia:
              type: string
              example: "História"
            observacoes:
              type: string
              example: "Professora especialista em história moderna"
    """
    data = request.get_json()  # só JSON, sem fallback para form
    if not data:
        return jsonify({'erro': 'Nenhum dado enviado ou JSON mal formatado'}), 400
    try:
        professor = ProfessorController.criar(data)
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
    return jsonify({
        'id': professor.id,
        'nome': professor.nome,
        'idade': professor.idade,
        'materia': professor.materia,
        'observacoes': professor.observacoes
    }), 201

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    """
    Atualizar um professor existente
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: ID do professor a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Carlos Oliveira"
            idade:
              type: integer
              example: 42
            materia:
              type: string
              example: "Física"
            observacoes:
              type: string
              example: "Atualizado com nova disciplina"
    responses:
      200:
        description: Professor atualizado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: "Carlos Oliveira"
            idade:
              type: integer
              example: 42
            materia:
              type: string
              example: "Física"
            observacoes:
              type: string
              example: "Atualizado com nova disciplina"
      404:
        description: Professor não encontrado
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Professor não encontrado"
    """
    data = request.get_json(silent=True) or request.form.to_dict()
    professor = ProfessorController.atualizar(id, data)

    if not professor:
        return jsonify({'error': 'Professor não encontrado'}), 404

    return jsonify({'id': professor.id, 'nome': professor.nome, 'idade': professor.idade, 'materia': professor.materia, 'observacoes': professor.observacoes})

@professor_bp.route('/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    """
    Deletar um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: ID do professor a ser deletado
    responses:
      200:
        description: Professor deletado com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Professor deletado"
      404:
        description: Professor não encontrado
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Professor não encontrado"
    """
    professor = ProfessorController.deletar(id)
    if not professor:
        return jsonify({'error': 'Professor não encontrado'}), 404
    return jsonify({'message': 'Professor deletado'})
