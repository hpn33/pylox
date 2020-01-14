from abc import ABC

from oylox.grammar.Expr import ExprVisitor, Expr, Grouping, Unary
from oylox.util.token_type import TokenType


class Interpreter(ExprVisitor, ABC):
	
	def visit_literal_expr(self, expr):
		return expr.value
	
	def visit_unary_expr(self, expr: Unary):
		right = self.evaluate(expr.right)
		
		if expr.operator.typ == TokenType.MINUS:
			return -right
		elif expr.operator.typ == TokenType.BANG:
			return not self.is_truthy(right)
		
		return None
	
	def is_truthy(self, object):
		if object is None:
			return False
		if object is bool:
			return bool(object)
		
		return True
	
	def visit_grouping_expr(self, expr: Grouping):
		return self.evaluate(expr.expression)
	
	def evaluate(self, expr: Expr):
		return expr.accept(self)
