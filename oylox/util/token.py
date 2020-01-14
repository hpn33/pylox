class Token(object):
	def __init__(self, typ, lexeme, literal, line):
		self.typ = typ
		self.lexeme = lexeme
		self.literal = literal
		self.line = line
	
	def __str__(self):
		return f'{self.typ} {self.lexeme} {self.literal} {self.line}'
