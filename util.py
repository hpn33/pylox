

TYPE = [
	
]



class token:
	
	def __init__(self, source, type):
		self.source = source
		self.type = type
	

class line:
	
	def __init__(self, num, source):
		self.num = num
		self.level = self.level_detector(source)
		self.source = self.check_last_back_n(source)
	
	def get_parts(self):
		pass
	
	def level_detector(self, line):
		level = 0
		
		for w in line:
			if w != '\t':
				break
			
			level += 1
		
		return level
	
	def check_last_back_n(self, line):
		position = len(line)-1
	
		last_back_n = line[position:]
			
		if last_back_n == '\n':
			line = line[:position]
		
		return line



