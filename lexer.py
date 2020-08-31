# ----------------------------------------------------
# Analizador Lexico para MiniLua
# ----------------------------------------------------
from errors import error
import sly

class LuaLexer(sly.Lexer):

    tokens = {
        # Palabras reservadas
        AND, BREAK, DO, ELSE, ELSEIF,

        # Delimitadores y operadores
        EQ, NE,

        # Identificadores
        NAME,

        # Constantes
        NUMBER, STRING
    }
    literals = '+-*/^'

    # patrones ignorados
    ignore = ' \t\r'

    # Expresiones Regulares
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # palabres reservadas
    NAME['and']    = AND
    NAME['break']  = BREAK
    NAME['do']     = DO
    NAME['else']   = ELSE
    NAME['elseif'] = ELSEIF

    # operadores
    EQ  = r'=='
    NE  = r'~='

    NUMBER = r'\d+'
    STRING = r'".*"'

    def NUMBER(self, t):
        '''
        t.type   = 'NUMBER'
        t.value  = '45'
        t.lineno = 1
        t.index  = 0
        '''
        t.value = int(t.value)
        return t

    def STRING(self, t):
        # Revisar secuencias de escape
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Comentarios largos

    # Comentarios cortos

    def error(self, t):
        print(t.lineno, "Caracter ilegal '%s'" % t.value[0])
        self.index += 1

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} filename')

    lexer = LuaLexer()
    with open(argv[1]) as file:
        for tok in lexer.tokenize(file.read()):
            print(tok)

if __name__ == '__main__':
    import sys
    main(sys.argv)
