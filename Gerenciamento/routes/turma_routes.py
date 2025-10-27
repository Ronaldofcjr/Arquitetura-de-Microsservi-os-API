from flask import Blueprint, request, jsonify
from controllers.turma_controller import TurmaController
from controllers.professor_controller import ProfessorController

turma_bp = Blueprint('turma', __name__, url_prefix='/turma')

@turma_bp.route('/',methods=['GET'])
def listar_turmas():
  """
    Listar todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Retorna a lista de turmas cadastradas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              descricao:
                type: string
                example: "Turma A - 1º Ano"
              ativo:
                type: boolean
                example: true
    """
  turmas = TurmaController.listar_turmas()
  return jsonify([{'id': t.id, 'descricao': t.descricao, 'ativo': t.ativo} for t in turmas])

@turma_bp.route('/', methods=['POST'])
def criar_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
              example: "Turma de Python Avançado"
            professor_id:
              type: integer
              example: 1
    responses:
      201:
        description: Turma criada com sucesso
      400:
        description: Professor não encontrado
    """
    data = request.get_json(silent=True) or request.form.to_dict()
    professor = ProfessorController.consultar_professor(data.get("professor_id"))

    if professor:  
        turma = TurmaController.criar(data)
        return jsonify([{
            'id': turma.id,
            'descricao': turma.descricao,
            'professor_id': turma.professor_id,
            'ativo': turma.ativo
        }]), 201
    else:
        return jsonify([{'msg': 'Professor não encontrado'}]), 400
    
@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    """
    Atualizar uma turma existente
    ---
    tags:
      - Turmas
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: ID da turma a ser atualizada
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
              example: "Turma A - 3º Ano"
            professor_id:
              type: integer
              example: 2
            ativo:
              type: boolean
              example: false
    responses:
      200:
        description: Turma atualizada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            descricao:
              type: string
              example: "Turma A - 3º Ano"
            professor_id:
              type: integer
              example: 2
            ativo:
              type: boolean
              example: false
      404:
        description: Turma não encontrada
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Turma não encontrada"
    """
    data = request.get_json(silent=True) or request.form.to_dict()
    turma = TurmaController.atualizar(id, data)

    if not turma:
      return jsonify({'error': 'Turma não encontrada'}), 404

    return jsonify({'id': turma.id, 'descricao': turma.descricao, 'professor_id': turma.professor_id, 'ativo': turma.ativo})


@turma_bp.route('/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    """
    Deletar uma turma pelo ID
    ---
    tags:
      - Turmas
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: ID da turma a ser deletada
    responses:
      200:
        description: Turma deletada com sucesso
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Turma deletada"
      404:
        description: Turma não encontrada
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Turma não encontrada"
    """
    turma = TurmaController.deletar(id)

    if not turma:
      return jsonify({'error': 'Turma não encontrada'}), 404

    return jsonify({'message': 'Turma deletada'})