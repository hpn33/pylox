import sys

from oylox.util.token import Token
from oylox.util.token_type import TokenType


# TODO: Probably refactor to have a single error function
class ErrorHandler:
	def __init__(self):
		self.had_error = False
		self.had_runtime_error = False
	
	def error(self, line: int, message: str):
		self.report(line, "", message)
	
	def error_on_token(self, token: Token, message: str):
		if token.typ == TokenType.EOF:
			self.report(token.line, " at End", message)
		else:
			self.report(token.line, f" at {token.lexeme} ", message)
	
	def report(self, line: int, where: str, message: str):
		print(f"[{line}] Error{where}: {message}", file=sys.stderr)
		self.had_error = True
