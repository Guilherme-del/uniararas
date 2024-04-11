from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemplo de dados (poderiam ser armazenados em um banco de dados)
produtos = [
    {"id": 1, "nome": "Produto A", "descricao": "Descrição do Produto A", "preco": 10.0},
    {"id": 2, "nome": "Produto B", "descricao": "Descrição do Produto B", "preco": 20.0},
]

# Endpoint para listar todos os produtos (GET)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# Endpoint para obter um produto específico (GET)
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto)
    return jsonify({"mensagem": "Produto não encontrado"}), 404

# Endpoint para adicionar um novo produto (POST)
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    novo_produto = request.json
    produtos.append(novo_produto)
    return jsonify({"mensagem": "Produto adicionado com sucesso"})

# Endpoint para atualizar um produto existente (PUT)
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        dados_atualizados = request.json
        produto.update(dados_atualizados)
        return jsonify({"mensagem": "Produto atualizado com sucesso"})
    return jsonify({"mensagem": "Produto não encontrado"}), 404

# Endpoint para remover um produto existente (DELETE)
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    global produtos
    produtos = [p for p in produtos if p.get('id') != id]
    return jsonify({"mensagem": "Produto deletado com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
