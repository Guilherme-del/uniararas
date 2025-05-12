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

# ===================
# 4️⃣ EXECUÇÃO FINAL
# ===================

if __name__ == "__main__":
    # 📥 Entrada da linguagem customizada (pode vir de arquivo ou string)
    entrada = """
    mochila capacidade=50
    item nome=livro peso=10 valor=60
    item nome=notebook peso=20 valor=100
    item nome=jaqueta peso=30 valor=120
    resolver
    """
    
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
