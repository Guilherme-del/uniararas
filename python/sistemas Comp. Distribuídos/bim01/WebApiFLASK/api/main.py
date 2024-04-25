from flask import Flask, request, jsonify

app = Flask(__name__)

# Estrutura de dados para representar usuários e carrinhos
usuarios = [
    {
        'usuario': 'marcilio',
        'nome': 'Marcilio F Oliveira',
        'id': 1,
        'carrinho': {
            'total': 42.53,
            'produtos': [
                {
                    'codigo': 1,
                    'nome': 'película de celular',
                    'valor': 30.00
                },
                {
                    'codigo': 22,
                    'nome': 'caneta de quadro branco',
                    'valor': 12.53
                }
            ]
        }
    }
]

# Endpoint para listar os produtos do carrinho por usuário
@app.route('/usuarios/<string:usuario>/carrinho', methods=['GET'])
def listar_produtos_carrinho(usuario):
    for user in usuarios:
        if user['usuario'] == usuario:
            return jsonify(user['carrinho']['produtos'])
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Endpoint para remover algum produto do carrinho de um determinado usuário através do código
@app.route('/usuarios/<string:usuario>/carrinho/<int:codigo>', methods=['DELETE'])
def remover_produto_carrinho(usuario, codigo):
    for user in usuarios:
        if user['usuario'] == usuario:
            produtos = user['carrinho']['produtos']
            for produto in produtos:
                if produto['codigo'] == codigo:
                    produtos.remove(produto)
                    return jsonify({'message': 'Produto removido do carrinho'}), 200
    return jsonify({'message': 'Usuário ou produto não encontrado'}), 404

# Endpoint para adicionar algum produto no carrinho de um determinado usuário
@app.route('/usuarios/<string:usuario>/carrinho', methods=['POST'])
def adicionar_produto_carrinho(usuario):
    data = request.json
    for user in usuarios:
        if user['usuario'] == usuario:
            user['carrinho']['produtos'].append(data)
            return jsonify({'message': 'Produto adicionado ao carrinho'}), 201
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Endpoint para atualizar o nome do usuário
@app.route('/usuarios/<string:usuario>', methods=['PUT'])
def atualizar_nome_usuario(usuario):
    data = request.json
    for user in usuarios:
        if user['usuario'] == usuario:
            user['nome'] = data['nome']
            return jsonify({'message': 'Nome do usuário atualizado'}), 200
    return jsonify({'message': 'Usuário não encontrado'}), 404

# Endpoint para criar um usuário no servidor
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    usuarios.append(data)
    return jsonify({'message': 'Usuário criado'}), 201

# Endpoint para exibir o total de usuários existentes
@app.route('/usuarios/total', methods=['GET'])
def total_usuarios():
    return jsonify({'total_usuarios': len(usuarios)})

# Endpoint para exibir a somatória de todos os carrinhos existentes no servidor
@app.route('/carrinhos/total', methods=['GET'])
def total_carrinhos():
    total = sum(user['carrinho']['total'] for user in usuarios)
    return jsonify({'total_carrinhos': total})

if __name__ == '__main__':
    app.run(debug=True)
