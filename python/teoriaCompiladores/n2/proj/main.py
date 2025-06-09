import re

# ==========  
# 1️⃣ LEXER  
# ==========

def lexer(linhas):
    tokens = []
    for linha in linhas:
        linha = linha.strip()
        if linha.startswith('mochila'):
            match = re.match(r'mochila\s+capacidade=(\d+)', linha)
            if match:
                tokens.append(('MOCHILA', int(match.group(1))))
        elif linha.startswith('item'):
            match = re.match(r'item\s+nome=(\w+)\s+peso=(\d+)\s+valor=(\d+)', linha)
            if match:
                nome = match.group(1)
                peso = int(match.group(2))
                valor = int(match.group(3))
                tokens.append(('ITEM', nome, peso, valor))
        elif linha.startswith('resolver'):
            tokens.append(('RESOLVER',))
    return tokens

# =============  
# 2️⃣ PARSER  
# =============

def parser(tokens):
    estrutura = {"capacidade": None, "itens": []}
    for token in tokens:
        if token[0] == 'MOCHILA':
            estrutura["capacidade"] = token[1]
        elif token[0] == 'ITEM':
            _, nome, peso, valor = token
            estrutura["itens"].append({"nome": nome, "peso": peso, "valor": valor})
        elif token[0] == 'RESOLVER':
            estrutura["resolver"] = True
    return estrutura

# ==========================  
# 3️⃣ INTERPRETADOR / ALGORITMO  
# ==========================

def resolver_mochila(capacidade, itens):
    n = len(itens)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        peso = itens[i-1]["peso"]
        valor = itens[i-1]["valor"]
        for w in range(1, capacidade + 1):
            if peso <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - peso] + valor)
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacidade]

# ==========================  
# 4️⃣ FUNÇÃO DE LEITURA DE ARQUIVO  
# ==========================

def ler_entrada_arquivo(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return ""
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return ""

# ===================  
# 5️⃣ EXECUÇÃO PRINCIPAL  
# ===================

if __name__ == "__main__":
    print("Escolha o modo de entrada:")
    print("1 - Input manual")
    print("2 - Exemplo")
    
    modo = input("Digite 1 ou 2: ").strip()

    if modo == '1':
        print("Digite sua entrada (termine com a palavra 'FIM'):")
        linhas_input = []
        while True:
            linha = input()
            if linha.strip().upper() == 'FIM':
                break
            linhas_input.append(linha)
        entrada = '\n'.join(linhas_input)
    elif modo == '2':
        entrada = """
        mochila capacidade=50
        item nome=livro peso=10 valor=60
        item nome=notebook peso=20 valor=100
        item nome=jaqueta peso=30 valor=120
        resolver
        """
        print(entrada.strip())

    else:
        print("Modo inválido.")
        exit(1)

    linhas = entrada.strip().split('\n')

    # Passo 1: lexer
    tokens = lexer(linhas)
    print("[TOKENS]", tokens)

    # Passo 2: parser
    estrutura = parser(tokens)
    print("[ESTRUTURA]", estrutura)

    # Passo 3: interpretador
    if estrutura.get("resolver"):
        resultado = resolver_mochila(estrutura["capacidade"], estrutura["itens"])
        print("Valor máximo que cabe na mochila:", resultado)
    else:
        print("Nenhum comando de resolução encontrado.")
