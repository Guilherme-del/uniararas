#Nome: Guilherme Cavenaghi RA: 109317

import ply.lex as lex

# Lista de tokens reconhecidos pelo lexer
tokens = (
    'NUMBER',  # Números inteiros
    'PLUS',    # +
    'MINUS',   # -
    'TIMES',   # *
    'DIVIDE',  # /
    'LPAREN',  # (
    'RPAREN',  # )
)

# Regras para tokens simples
t_ignore = ' \t'  # Ignorar espaços e tabulações
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = 
r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Criar o lexer
lexer = lex.lex()

# Exemplo de uso
def test_lexer(data):
    lexer.input(data)
    while tok := lexer.token():
        print(tok)

if __name__ == "__main__":
    test_lexer("3 + 5 * ( 10 - 2 )")