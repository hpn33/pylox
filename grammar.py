from scanner import Scanner
from token import Token


class Expr:
	def accept(self, visitor):
		pass


class Binary(Expr):
	def __init__(self, left: Expr, operator: Token, right: Expr):
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		visitor.visitBinaryExpr(self)


class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression = expression

	def accept(self, visitor):
		visitor.visitGroupingExpr(self)


class Literal(Expr):
	def __init__(self, value: object):
		self.value = value

	def accept(self, visitor):
		visitor.visitLiteralExpr(self)


class Unary(Expr):
	def __init__(self, operator: Token, right: Expr):
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		visitor.visitUnaryExpr(self)
