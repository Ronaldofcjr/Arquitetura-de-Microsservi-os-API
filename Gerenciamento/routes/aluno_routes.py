from flask import Blueprint, request, jsonify
from controllers.aluno_controller import AlunoController

aluno_bp = Blueprint ('alunos', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['GET'])
def listar_alunos():
    """
    Listar todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Retorna a lista de alunos cadastrados
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
                example: "Maria Silva"
              idade:
                type: integer
                example: 20
              turma_id:
                type: integer
                example: 3
              data_nascimento:
                type: string
                example: "2005-03-14"
              nota_primeiro_semestre:
                type: number
                example: 8.5
              nota_segundo_semestre:
                type: number
                example: 9.0
              media_final:
                type: number
                example: 8.75
    """
    alunos = AlunoController.listar()
    return jsonify([
        {
            'id': aluno.id,
            'nome': aluno.nome,
            'idade': aluno.idade,
            'turma_id': aluno.turma_id,
            'data_nascimento': aluno.data_nascimento.isoformat() if aluno.data_nascimento else None,
            'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
            'nota_segundo_semestre': aluno.nota_segundo_semestre,
            'media_final': aluno.media_final
        }
        for aluno in alunos
    ]), 200

@aluno_bp.route('/', methods=['POST'])
def criar_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
            - idade
          properties:
            nome:
              type: string
              example: "Ronaldo Cavalcante"
            idade:
              type: integer
              example: 22
            data_nascimento:
              type: string
              example: "2003-10-05"
            nota_primeiro_semestre:
              type: number
              example: 8
            nota_segundo_semestre:
              type: number
              example: 9
            turma_id:
              type: integer
              example: 1
    responses:
      201:
        description: Aluno criado com sucesso
      400:
        description: Campos obrigatórios ausentes
    """
    data = request.get_json(silent=True) or request.form.to_dict()
    
    if not data or 'nome' not in data or 'idade' not in data:
        return jsonify({'erro': 'Campos obrigatórios: nome e idade'}), 400

    # Passando todos os campos opcionais
    novo_aluno = AlunoController.criar({
        'nome': data['nome'],
        'idade': data['idade'],
        'data_nascimento': data.get('data_nascimento'),
        'nota_primeiro_semestre': data.get('nota_primeiro_semestre'),
        'nota_segundo_semestre': data.get('nota_segundo_semestre'),
        'turma_id': data.get('turma_id')
    })

    return jsonify({
        'mensagem': 'Aluno criado com sucesso!',
        'id': novo_aluno.id,
        'nome': novo_aluno.nome,
        'idade': novo_aluno.idade
    }), 201

@aluno_bp.route('/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    """
    Atualizar dados de um aluno existente
    ---
    tags:
      - Alunos
    parameters:
      - in: path
        name: aluno_id
        required: true
        type: integer
        description: ID do aluno a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Ronaldo Atualizado"
            idade:
              type: integer
              example: 23
    responses:
      200:
        description: Aluno atualizado com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Aluno atualizado com sucesso!"
            id:
              type: integer
              example: 1
    """
    data = request.get_json(silent=True) or request.form.to_dict()
    aluno_atualizado = AlunoController.atualizar(aluno_id, data)
    return jsonify({
        'mensagem': 'Aluno atualizado com sucesso!',
        'id': aluno_atualizado.id,
        'nome': aluno_atualizado.nome,
        'idade': aluno_atualizado.idade
    }), 200

@aluno_bp.route('/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    """
    Deletar um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - in: path
        name: aluno_id
        required: true
        type: integer
        description: ID do aluno a ser removido
    responses:
      200:
        description: Aluno deletado com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Aluno deletado com sucesso!"
    """
    AlunoController.deletar(aluno_id)
    return jsonify({'mensagem': 'Aluno deletado com sucesso!'}), 200

