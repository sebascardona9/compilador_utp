import re
from errors import error

NAME_PAT = re.compile('[a-zA-Z_][a-zA-Z0-9_]*') #patron del nombre
FLOAT_PAT = re.compile(r'(\d+\.\d*)|(\d*\.\d+)')#patron de numero flotante esta incompleto
INT_PAT = re.compile(r'\d+')#patron del numero entero
STRINGS_PAT = re.compile(r'\"(.+?)\"')
LARGE_COMMENTS_PAT = re.compile(r'^-{2}\[{2}.*\]{2}|^-{2}.*')
#LARGE_COMMENTS_PAT = re.compile(r'\-\[\[.*\]\].*')
SHORT_COMMENTS_PAT = re.compile(r'\-\-.*')


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

def find_match(text, index):
    name    = NAME_PAT.match(text, index)
    message = STRINGS_PAT.match(text, index)
    number  = INT_PAT.match(text,index)
    number_float = FLOAT_PAT.match(text, index)
    short_comments = SHORT_COMMENTS_PAT.match(text, index)
    large_comments = LARGE_COMMENTS_PAT.match(text, index) 
    if name:
        value = name.group(0)
        if value in KEYWORDS:
            return value.upper(), value
        else:
            return name.group(0), 'NAME'  
    # Comentarios Cortos
    elif short_comments:
        return short_comments.group(0), 'COMMENTS' #DEFINIR NOMBRE DE COMENTARIOS
    elif number_float:
        return number_float.group(0), 'FLOAT'
    elif number:
        return number.group(0), 'INTEGER' #DEFINIR EL NOMBRE DEL TYPE PARA LOS ENTEROS
    elif message:        
        return message.group(0), 'STRING'
    elif large_comments:
        return large_comments.group(0), 'LARGECOMMENTS'
    else:
        return None, ''
        

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

        

        # Coincidencia de simbolos a traves de expresiones regulares


        
        value, type_token = find_match(text, index)
        
        if value:
            if type_token not in ["COMMENTS", "LARGECOMMENTS"]:
                yield Token(type_token, value, lineno)   
            index += len(value)
            continue
        else:
            error("caracter ilegal '%s'" % text[index], lineno)
            index += 1

                

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} filename')
    with open(argv[1]) as file:
        tokens = tokenize(file.read())
        for tok in tokens:
            print(tok)


if __name__ == '__main__':
    import sys
    main(sys.argv)
