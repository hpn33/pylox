import util
from token import Token, TokenType, symbol


class Scanner:
	
	def __init__(self, source: str):
		self.source = source
		self.tokens = []
		
		self.start = 0
		self.current = 0
		self.line = 1
	
#	def init(self, fr):
#		self.tokens = []
#		
#		self.start = 0
#		self.current = 0
#		self.line = 1
#		
#		self.get_tokens(fr.lines)
	
	def get_tokens(self, lines):
		
		for line in lines:
			line = line.source
			# print(line)
			
			self.set_tokens(line)
		
		for tok in self.tokens:
			print(tok.type[:6], '\t', tok.source)
	
	def set_tokens(self, line):
		text = ''
		counter = 0
		
		while counter <= len(line) - 1:
			
			w = line[counter]
			
			if w in [' ', '\t']:
				text = ''
				counter += 1
				continue
			
			text += w
			# print(counter, ' ', w, ' ', text)
			
			if text in util.keyword:
				tok = Token(text, 'keyword')
				self.tokens.append(tok)
				text = ''
			
			if text == ' ':
				text = ''
			
			if text in util.assignment:
				tok = Token(text, 'assign')
				self.tokens.append(tok)
				text = ''
			
			if text in ["\'", '\"']:
				callback = self.string_action(line, counter)
				counter = callback['counter']
				text = callback['string']
				
				tok = util.Token(text, 'string')
				self.tokens.append(tok)
				text = ''
				continue
			
			counter += 1
	
	def string_action(self, line, counter):
		string = ''
		is_string = False
		counter = counter
		
		while counter <= len(line):
			w = line[counter]
			
			if is_string:
				if self.check_mark(w):
					is_string = False
					counter += 1
					break
			
			else:
				if self.check_mark(w):
					is_string = True
					counter += 1
					continue
			
			string += w
			counter += 1
		
		return {'counter': counter, 'string': string}
	
	def check_mark(self, word):
		return word in ["'", '"']
	
	def scan_tokens(self):
		while not self.is_at_end():
			self.start = self.current
			self.scan_token()
		
		self.tokens.append(Token(TokenType.EOF, '', None, self.line))
		return self.tokens
	
	def scan_token(self):
		
		char = self.advance()
		
		if char in symbol and self.match('='):
			# print('d symbol')
			# c = f'{char}='
			# print(c, ' ', symbol[c])
			
			self.add_token(symbol[f'{char}='])
		
		elif char in symbol:
			# print('symbol')
			# print(char, ' ', symbol[char])
			
			self.add_token(symbol[char])
		elif char == '/':
			if mathc('/'):
				while peek != '\n' and not is_at_end():
					advance()
			else:
				add_token(TokenType.SLASH)
		else:
			# Lox.error(line, 'Unexpected character')
			print(char, ' is wrong')
			pass
	
	def peek(self):
		if is_at_end():
			return
		
		return self.source[self.current]
	
	def match(self, expected: str):
		if self.is_at_end():
			return False
		if self.source[self.current] != expected:
			return False
		
		self.current += 1
		return True
	
	def current_char(self):
		return self.source[self.current]
	
	def add_token(self, typ, literal=None):
		text = self.source[self.start: self.current]
		self.tokens.append(Token(typ, text, literal, self.line))
	
	def advance(self):
		self.current += 1
		return self.source[self.current - 1]
	
	def is_at_end(self):
		return self.current >= len(self.source)


class FileReader:
	
	def __init__(self, path):
		self.source = ''
		self.lines = []
		self.length = 0
		
		self.set_file_name(path)
	
	def set_file_name(self, file_name):
		f = open(file_name, 'r')
		
		self.set_file(f)
		
		f.close()
	
	def set_file(self, file):
		self.source = file.read()
		self.length = len(self.source)
		
		count = 1
		
		for line in self.source.splitlines():
			lin = util.Line(count, line)
			self.lines.append(lin)
			
			del lin
			count += 1
