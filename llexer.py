import re
from errors import error

NAME_PAT = re.compile('[a-zA-Z_][a-zA-Z0-9_]*') #patron del nombre
FLOAT_PAT = re.compile(r'(\d+\.\d*)|(\d*\.\d+)')#patron de numero flotante esta incompleto
INT_PAT = re.compile(r'\d+')#patron del numero entero

TWO_CHAR = {
     '<=' : 'LE',
     '>=' : 'GE',
     '==' : 'EQ',
     '~=' : 'NE',
     '..' : 'CONCAT'
}
ONE_CHAR = {
     '+' : '+',
     '-' : '-',
     '*' : '*',
     '/' : '/',
     '^' : '^',
     '%' : '%',
     '=' : '=',
     '<' : 'LT',
     '>' : 'GT',
     '(' : '(',
     ')' : ')',
     '{' : '{',
     '}' : '}',
     '[' : '[',
     ']' : ']',
     ';' : ';',
     ':' : ':',
     ',' : ',',
     ';' : ';',
}

KEYWORDS = {
     'and', 'break', 'do', 'else', 'elseif',
     'end', 'false', 'for', 'function', 'if',
     'in', 'local', 'nil', 'not', 'or',
     'repeat', 'return', 'then', 'true', 'until', 'while'
}
class Token:
     def __init__(self,type, value, lineno):
         self.type = type
         self.value = value
         self.lineno = lineno

     def __repr__(self):
         return f'Token({self.type!r}, {self.value!r}, {self.lineno})'#retorna el string en formato la f lo da

def tokenize(text):
     index = 0 # Posición actual
     lineno = 1

     while index < len(text): #condicion para comparar la longitud del texto
         # Produce un token
         if text[index] in ' \t':
             index += 1
             continue

         elif text[index] == '\n':
             lineno += 1
             index += 1
             continue
         #print('sebas')

     # Comentarios Largos

     # Comentarios Cortos

     # Coincidencia de simbolos a traves de expresiones regulares
         m = NAME_PAT.match(text, index)
         if m:
             value = m.group(0)
             if value in KEYWORDS:
                yield Token(value.upper(), value, lineno)
             else:
                yield Token('NAME', m.group(0), lineno)
             index += len(value)
             continue

def main(argv):
     if len(argv) != 2:
         raise SystemExit(f'Usage: {argv[0]} filename')
     with open(argv[1]) as file:
         for tok in tokenize(file.read()):
             print(tok)

if __name__ == '__main__':
    import sys
    main(sys.argv)
