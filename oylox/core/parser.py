from oylox.grammar.Expr import *
from oylox.util.error_handler import ErrorHandler
from oylox.util.token import Token
from oylox.util.token_type import TokenType, Hook


class Parser:
	
	def __init__(self, tokens: [], error_handler: ErrorHandler):
		self.tokens = tokens
		self.error_handler = error_handler
		self.current = 0
	
	def parse(self):
		try:
			return self.expression()
		except ParseError as e:
			return None
	
	def expression(self):
		return self.equality()
	
	def equality(self):
		expr = self.comparison()
		
		while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
			operator = self.previous()
			right = self.comparison()
			expr = Binary(expr, operator, right)
		
		return expr
	
	def comparison(self):
		expr = self.addition()
		
		while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
			operator = self.previous()
			right = self.addition()
			expr = Binary(expr, operator, right)
		
		return expr
	
	def addition(self):
		expr = self.multiplication()
		
		while self.match(TokenType.MINUS, TokenType.PLUS):
			operator = self.previous()
			right = self.multiplication()
			expr = Binary(expr, operator, right)
		
		return expr
	
	def multiplication(self):
		expr = self.unary()
		
		while self.match(TokenType.SLASH, TokenType.STAR):
			operator = self.previous()
			right = self.unary()
			expr = Binary(expr, operator, right)
		
		return expr
	
	def unary(self):
		if self.match(TokenType.BANG, TokenType.MINUS):
			operator = self.previous()
			right = self.unary()
			return Unary(operator, right)
		
		return self.primary()
	
	def primary(self):
		if self.match(TokenType.FALSE):
			return Literal(False)
		
		if self.match(TokenType.TRUE):
			return Literal(True)
		
		if self.match(TokenType.NIL):
			return Literal(None)
		
		if self.match(TokenType.NUMBER, TokenType.STRING):
			return Literal(self.previous())
		
		if self.match(TokenType.LEFT_PAREN):
			expr = self.expression()
			self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
			return Grouping(expr)
		
		raise self.error(self.peek(), 'Expect expression.')
	
	def match(self, *types):
		for typ in types:
			if self.check(typ):
				self.advance()
				return True
		
		return False
	
	def check(self, typ: TokenType):
		if self.is_at_end():
			return False
		
		return self.peek() == typ
	
	def consume(self, typ: TokenType, message: str):
		if self.check(typ):
			return self.advance()
		
		raise self.error(self.peek(), message)
	
	def error(self, token: Token, message: str):
		self.error_handler.error_on_token(token, message)
		
		return ParseError('')
	
	def synchronize(self):
		self.advance()
		
		while not self.is_at_end():
			if self.previous().typ is TokenType.SEMICOLON:
				return
			
			if self.peek().type in Hook.statement:
				return
			
			self.advance()
	
	def advance(self):
		if not self.is_at_end():
			self.current += 1
		return self.previous()
	
	def is_at_end(self):
		return self.peek().typ == TokenType.EOF
	
	def peek(self):
		return self.tokens[self.current]
	
	def previous(self):
		return self.tokens[self.current - 1]


class ParseError(RuntimeError):
	def __init__(self, message):
		super().__init__(self, message)
