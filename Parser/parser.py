#parser.py: un archivo de especificación SLY-Yacc para analizar programas Mini-Lua.
#Las acciones de este analizador deben construir nodos del AST.

# ----------------------------------------
# Analisis Sintatico para Lua 5.1
#
# (c) Angel A Agudelo Z
# ----------------------------------------
#from model import *
from errors import error
from lexer import tokenize 
import sly


class LuaParser(sly.Parser):

	# Si el lexer hubiese sido construido con Sly.
	#tokens = Lexer.tokens

	"""
	Tengo un problema al crear la variable de tipo LuaParser sly se esta realizando una validación de tokens
	Sale el siguiente error -> token is empty
	¿Como pasar los tokens creados con el lexer custom al Parser del Sly? 
	¿Cómo se podría crear los tokens en el lexer custom como se estan creando y utilizando en el lexer de Sly?
	¿Podría crear el lexer con el Sly?
	¿Cúal es la solución más viable en este caso?
	"""
	tokens = []

	def __init__(self, tokens):
		self.tokens = tokens     

	debugfile = 'afd.txt'

	precedence = (
		('left', 'OR'),
		('left', 'AND'),
		('left', 'LT', 'GT', 'LE', 'GE', 'NE', 'EQ'),
		('right', 'CONCAT'),
		('left', '+', '-'),
		('left', '*', '/', '%'),
		('left', 'NOT', 'UMINUS'),
		('right', '^'),
	)
	
	@_('stmts')
	def start(self, p):
		pass

	@_("empty")
	def stmts(self, p):
		pass

	@_("stmt ';' stmts")
	def stmts(self, p):
		pass

	@_("vars '=' exps")
	def stmt(self, p):
		pass

	@_("functioncall")
	def stmt(self, p):
		pass#return p.functioncall

	@_("DO stmts END")
	def stmt(self, p):
		pass

	@_("WHILE exp DO stmts END")
	def stmt(self, p):
		pass

	@_("IF exp THEN stmts elsepart END")
	def stmt(self, p):
		pass

	@_("RETURN")
	def stmt(self, p):
		pass

	@_("RETURN exps")
	def stmt(self, p):
		pass

	@_("BREAK")
	def stmt(self, p):
		pass

	@_("FOR NAME '=' exp ',' exp DO stmts END")
	def stmt(self, p):
		pass

	@_("FOR NAME '=' exp ',' exp ',' exp DO stmts END")
	def stmt(self, p):
		pass

	@_("FOR names IN exps DO stmts END")
	def stmt(self, p):
		pass

	@_("FUNCTION function")
	def stmt(self, p):
		pass

	@_("LOCAL FUNCTION function")
	def stmt(self, p):
		pass

	@_("LOCAL names")
	def stmt(self, p):
		pass

	@_("LOCAL names '=' exps")
	def stmt(self, p):
		pass

	@_("empty")
	def elsepart(self, p):
		pass

	@_("ELSE stmts")
	def elsepart(self, p):
		pass

	@_("ELSEIF exp THEN stmts elsepart")
	def elsepart(self, p):
		pass

	@_("NAME funcbody")
	def function(self, p):
		pass

	@_("NAME ':' NAME funcbody")
	def function(self, p):
		pass

	@_("'(' params ')' stmts END")
	def funcbody(self, p):
		pass

	@_("empty")
	def params(self, p):
		pass

	@_("names")
	def params(self, p):
		pass

	@_("NAME")
	def names(self, p):
		pass

	@_("NAME ',' names")
	def names(self, p):
		pass

	@_("var")
	def vars(self, p):
		pass

	@_("var ',' vars")
	def vars(self, p):
		pass

	@_("NAME")
	def var(self, p):
		pass

	@_("prefixexp '[' exp ']'")
	def var(self, p):
		pass

	@_("prefixexp '.' NAME")
	def var(self, p):
		pass

	@_("exp")
	def exps(self, p):
		pass #return [p.expr]

	@_("exp ',' exps")
	def exps(self, p):
		pass

	#@_(#"exp OR exp",
	   #"exp AND exp",
	  # "exp LT exp",
	  # "exp LE exp",
	  # "exp GT exp",
	  # "exp GE exp",
	  # "exp EQ exp",
	   #"exp NE exp",
	  # "exp CONCAT exp",
	  # "exp '+' exp",
	 #  "exp '-' exp",
	  # "exp '*' exp",
	  # "exp '/' exp",
	  # "exp '%' exp",
	  # "exp '^' exp")
	#def exp(self, p):
	#	pass

	@_("exp OR exp")
	def exp(self, p):
		pass

	@_("exp AND exp")
	def exp(self, p):
		pass

	@_("exp LT exp")
	def exp(self, p):
		pass

	@_("exp LE exp")
	def exp(self, p):
		pass

	@_("exp GT exp")
	def exp(self, p):
		pass

	@_("exp GE exp")
	def exp(self, p):
		pass

	@_("exp EQ exp")
	def exp(self, p):
		pass

	@_("exp NE exp")
	def exp(self, p):
		pass

	@_("exp CONCAT exp")
	def exp(self, p):
		pass

	@_("exp '+' exp")
	def exp(self, p):
		pass

	@_("exp '-' exp")
	def exp(self, p):
		pass

	@_("exp '*' exp")
	def exp(self, p):
		pass

	@_("exp '/' exp")
	def exp(self, p):
		pass

	@_("exp '^' exp")
	def exp(self, p):
		pass

	@_("exp '%' exp")
	def exp(self, p):
		pass

	@_("'-' exp %prec UMINUS",
	   "NOT exp")
	def exp(self, p):
		pass

	@_("exp '!'")
	def exp(self, p):
		pass

	@_("NIL",
	   "TRUE",
	   "FALSE",
	   "STRING")
	def exp(self, p):
		pass

	@_("NUMBER")
	def exp(self, p):
		pass

	@_("FUNCTION funcbody")
	def exp(self, p):
		pass

	@_("prefixexp")
	def exp(self, p):
		pass

	@_("'{' fields '}'")
	def exp(self, p):
		pass

	@_("NAME")
	def prefixexp(self, p):
		pass

	@_("prefixexp '[' exp ']'")
	def prefixexp(self, p):
		pass

	@_("prefixexp '.' NAME")
	def prefixexp(self, p):
		pass

	@_("functioncall")
	def prefixexp(self, p):
		pass

	@_("'(' exp ')'")
	def prefixexp(self, p):
		pass

	@_("prefixexp args")
	def functioncall(self, p):
		pass

	@_("prefixexp '.' NAME args")
	def functioncall(self, p):
		pass

	@_("'(' ')'")
	def args(self, p):
		pass

	@_("'(' exps ')'")
	def args(self, p):
		pass

	@_("'{' fields '}'")
	def args(self, p):
		pass

	@_("empty")
	def fields(self, p):
		pass

	@_("field ',' fields")
	def fields(self, p):
		pass

	@_("'[' exp ']' '=' exp")
	def field(self, p):
		pass

	@_("NAME '=' exp")
	def field(self, p):
		pass

	@_("")
	def empty(self, p):
		pass

	def error(self, p):
		if p:
			print(p.lineno, "Error de sintaxis en la entrada en el token '%s'" % p.value)
		else:
			print('EOF','Error de sintaxis. No mas entrada.')


def parse(source):
	
	#Parser el código fuente en un AST. Devuelve la parte superior del árbol AST.
	
	tokens = tokenize(source)
	p = LuaParser()
	
	#return p.parse(tokens)
	

def main(argv):
	
	if len(argv) != 2:
		raise SystemExit(f'Usage: {argv[0]} filename')

	src = open(sys.argv[1]).read()
	ast = parse(src)

	# print(ast)


if __name__ == '__main__':
	print("Hola mundo")
	import sys
	main(sys.argv)
