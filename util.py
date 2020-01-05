TYPE = [

]

keyword = [
	'var',
	'print',
	'pass',
	'class',
	'pass'
]

assignment = [
	'=', '==',
	':',
]


class Token:
	
	def __init__(self, source, typ):
		self.source = source
		self.type = typ


class Line:
	
	def __init__(self, num, source):
		self.num = num
		self.level = self.level_detector(source)
		self.source = self.check_last_back_n(source)
	
	def get_parts(self):
		pass
	
	def level_detector(self, line: str) -> int:
		level = 0
		
		for w in line:
			if w != '\t':
				break
			
			level += 1
		
		return level
	
	def check_last_back_n(self, line: str) -> str:
		position = len(line) - 1
		
		last_back_n = line[position:]
		
		if last_back_n == '\n':
			line = line[:position]
		
		return line
