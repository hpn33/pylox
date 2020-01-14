from oylox.ast_printer import AstPrinter
from oylox.core.parser import Parser
from oylox.util.error_handler import ErrorHandler
from oylox.core.scanner import Scanner


class Lox:
	
	def __init__(self):
		self.source = ''
		self.error_handler = ErrorHandler()
	
	def run(self):
		tokens = Scanner(self.source, self.error_handler).scan_tokens()
		expression = Parser(tokens, self.error_handler).parse()
		
		if self.error_handler.had_error:
			return
		
		print(AstPrinter().print(expression))
	
	def run_file(self, file_path: str):
		f = open(file_path)
		
		self.source = f.read()
		
		f.close()
		
		self.run()
