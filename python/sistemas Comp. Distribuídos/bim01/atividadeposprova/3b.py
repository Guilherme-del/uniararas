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

if __name__ == '__main__':
    app.run(debug=True)