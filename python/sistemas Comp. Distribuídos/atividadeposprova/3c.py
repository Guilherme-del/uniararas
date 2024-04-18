from flask import Flask, jsonify, request

app = Flask(__name__)

# Variável global para armazenar os dados
global_data = []

# Endpoint para receber um JSON e salvar na variável global
@app.route('/receber_json', methods=['POST'])
def receber_json():
    global global_data
    json_data = request.json
    global_data.append(json_data)
    return jsonify({"message": "JSON recebido e salvo com sucesso!"}), 201

# Endpoint para retornar todos os itens da variável global
@app.route('/todos_itens', methods=['GET'])
def todos_itens():
    return jsonify(global_data)

# Endpoint para filtrar e retornar um único item sob a chave "dados"
@app.route('/item/<int:index>', methods=['GET'])
def item(index):
    global global_data
    if index < len(global_data):
        return jsonify(global_data[index]['dados'])
    else:
        return jsonify({"message": "Índice fora do intervalo"}), 404

if __name__ == '__main__':
    app.run(debug=True)
