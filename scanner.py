import util


class scanner:

	def __init__(self, lines = []):
		self.tokens = []
		
		self.set_lines(fr)
	
	def set_lines(self, fr):
		
		self.tokens = []
		
		
		self.get_tokens(fr.lines)
	
	def get_tokens(self, lines):
		for line in lines:
			line = line.source
			
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
			# print(w, ' ', text)
			
			if text in util.keyword:
				tok = util.Token(text, 'keyword')
				self.tokens.append(tok)
				text = ''
			
			if text == ' ':
				text = ''
			
			if text in util.assignment:
				tok = util.Token(text, 'assign')
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
		return word in ['\'', '\"']
	


class FileReader:
	
	def __init__(self, path):
		self.lines = []
		self.length = 0
		
		self.set_file_name(path)
	
	def set_file_name(self, file_name):
		f = open(file_name, 'r')
		
		self.set_file(f)
		
		f.close()
	
	def set_file(self, file):
		self.length = len(file.read())
		
		count = 1
		for line in file:
			lin = util.Line(count, line)
			self.lines.append(lin)
			
			del lin
			count += 1
