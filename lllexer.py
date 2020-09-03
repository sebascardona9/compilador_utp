import re
from errors import error

NAME_PAT = re.compile('[a-zA-Z_][a-zA-Z0-9_]*') #patron del nombre
TWO_CHAR_PAT = re.compile(r'<=|>=|==|~=|\.{2}')
FLOAT_PAT = re.compile(r'(\d+\.\d*)|(\d*\.\d+)')#patron de numero flotante esta incompleto
INT_PAT = re.compile(r'\d+')#patron del numero entero
STRINGS_PAT = re.compile(r'\"(.+?)\"')
COMMENTS_PAT = re.compile(r'-{2}\[{2}[^]]+\]{2}|-{2}.*')
COMMENTS_UNCLOSED = re.compile(r'-{2}\[{2}[^]]+')


#LARGE_COMMENTS_PAT = re.compile(r'\-\[\[(.|\n)*\]\].*')
#SHORT_COMMENTS_PAT = re.compile(r'\-\-.*')


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
    name                = NAME_PAT.match(text, index)
    message             = STRINGS_PAT.match(text, index)
    number              = INT_PAT.match(text,index)
    number_float        = FLOAT_PAT.match(text, index)
    comments_unclosed   = COMMENTS_UNCLOSED.match(text, index)
    comments            = COMMENTS_PAT.match(text, index)
    two_char_regex      = TWO_CHAR_PAT.match(text, index)

    if name:
        value = name.group(0)
        if value in KEYWORDS:
            return value, value.upper()
        else:
            return name.group(0), 'NAME'
    # Comentarios Cortos y largos
    elif comments:
        if comments_unclosed and "]]" not in comments.group(0):
            return comments_unclosed.group(0), 'COMMENTS' #DEFINIR NOMBRE DE COMENTARIOS
        else:
            return comments.group(0), 'COMMENTS' #DEFINIR NOMBRE DE COMENTARIOS
    elif number_float:
        return number_float.group(0), 'FLOAT'
    elif number:
        return number.group(0), 'INTEGER' #DEFINIR EL NOMBRE DEL TYPE PARA LOS ENTEROS
    elif message:
        return message.group(0), 'STRING'
    elif two_char_regex:
        value_twochar = two_char_regex.group(0)
        if value_twochar in TWO_CHAR:
            return value_twochar, TWO_CHAR[value_twochar]
    elif text[index] in ONE_CHAR:
        return text[index], ONE_CHAR[text[index]]
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
            if type_token not in ["COMMENTS"]:
                yield Token(type_token, value, lineno)
            elif type_token in ["COMMENTS"]:
                lineincommnet = value.count('\n')
                lineno += lineincommnet
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
